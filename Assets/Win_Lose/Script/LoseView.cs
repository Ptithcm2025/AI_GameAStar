namespace UI {
    using UnityEngine;
    using UnityEngine.UI;

    public class LoseView : MonoBehaviour
    {
        public Button Replay;
        public Button Exit;
        public Button Exit2;


        private void Start()
        {
            this.Exit.onClick.AddListener(() =>
            {
                HomeUIController.Instance.LoadLevel(2);
            });
            this.Exit2.onClick.AddListener(() =>
            {
                HomeUIController.Instance.LoadLevel(2);
            });
            this.Replay.onClick.AddListener(() =>
            {
                Time.timeScale = 1;
                UIManager.Instance.PauseGame.SetActive(true);
                HomeUIController.Instance.LoadLevel(1);
            });
        }
    }
}
