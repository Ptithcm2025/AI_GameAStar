namespace CoreGamePlay.View
{
    using DG.Tweening;
    using UnityEngine;

    public class EnemyView : MonoBehaviour
    {
        private RectTransform _rectTransform;
        public GameObject enemyIdle;
        public GameObject enemyUp;
        public GameObject enemyDown;
        public GameObject enemyLeft;
        public GameObject enemyRight;
        public bool isMoving = false;

        private void Start()
        {
            this._rectTransform = GetComponent<RectTransform>();
            this.IdleState();
        }

        public void IdleState()
        {
            this.enemyIdle.SetActive(true);
            this.enemyUp.SetActive(false);
            this.enemyDown.SetActive(false);
            this.enemyLeft.SetActive(false);
            this.enemyRight.SetActive(false);
        }

        public void UpState()
        {
            this.enemyIdle.SetActive(false);
            this.enemyUp.SetActive(false);
            this.enemyDown.SetActive(true);
            this.enemyLeft.SetActive(false);
            this.enemyRight.SetActive(false);
        }

        public void DownState()
        {
            this.enemyIdle.SetActive(false);
            this.enemyUp.SetActive(false);
            this.enemyDown.SetActive(true);
            this.enemyLeft.SetActive(false);
            this.enemyRight.SetActive(false);
        }

        public void LeftState()
        {
            this.enemyIdle.SetActive(false);
            this.enemyUp.SetActive(false);
            this.enemyDown.SetActive(false);
            this.enemyLeft.SetActive(true);
            this.enemyRight.SetActive(false);
        }

        public void RightState()
        {
            this.enemyIdle.SetActive(false);
            this.enemyUp.SetActive(false);
            this.enemyDown.SetActive(false);
            this.enemyLeft.SetActive(false);
            this.enemyRight.SetActive(true);
        }

        public void SetPosition(Vector2Int position, float moveSpeed, System.Action onComplete = null)
        {
            if (isMoving) return;
            int yPos =  (1080 / 2) - (50 + position.x * 50 + (position.x - 1) * 4 - 25);
            int xPos = -(1920 / 2) + (98 + position.y * 50 + (position.y - 1) * 4 - 25);

            Vector2 targetPos = new Vector2(xPos, yPos);
            float distance = Vector2.Distance(transform.position, targetPos);

            isMoving = true;

            transform.DOLocalJump(targetPos, jumpPower: 5f, numJumps: 1, duration: moveSpeed)
            .SetEase(Ease.InOutSine)
            .OnComplete(() =>
            {
                isMoving = false;
                onComplete?.Invoke();
            });
            //transform.DOLocalMove(targetPos, moveSpeed)
            //.SetEase(Ease.Linear)
            //.OnComplete(() =>
            //{
            //    isMoving = false;
            //    onComplete?.Invoke();
            //});
            //this._rectTransform.anchoredPosition = new Vector2(xPos, yPos);
        }

        public bool IsMoving()
        {
            return isMoving;
        }
    }
}
