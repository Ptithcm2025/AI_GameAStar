namespace CoreGamePlay.View
{
    using System.Collections;
    using UI;
    using UnityEngine;

    public class PlayerView : MonoBehaviour
    {
        public float cellSize = 1f;
        public float moveDuration = 0.2f;
        private bool isMoving = false;
        public bool IsMoving => isMoving;

        public Vector2Int GridToWorld(Vector2Int position)
        {
            position.x += 1;
            position.y += 1;
            int yPos =  (1080 / 2) - (50 + position.x * 50 + (position.x - 1) * 4 - 25);
            int xPos = -(1920 / 2) + (98 + position.y * 50 + (position.y - 1) * 4 - 25);

            return new Vector2Int(xPos, yPos);
        }

        public IEnumerator MoveToPosition(Vector2Int targetGrid)
        {
            isMoving = true;
            Vector2Int end = GridToWorld(targetGrid);

            yield return new WaitForSeconds(0.1f);
            if (end.x != - 1)
            {
                gameObject.GetComponent<RectTransform>().anchoredPosition = end;
                isMoving = false;
            }

            if (targetGrid.x == 14 && targetGrid.y == 30)
            {
                UIManager.Instance.ShowWinGame();
            }
        }
    }
}
