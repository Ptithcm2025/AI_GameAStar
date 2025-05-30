namespace UI
{
    using CustomUtils;
    using UnityEngine;

    public class UIManager : SingletonMono<UIManager>
    {
        [Header("UI")]
        public GameObject PlayGame;
        public LoseView LoseGame;
        public WinView WinGame;
        public GameObject PauseGame;
        public GameObject HomePage;


        public void ShowPauseGame(int state)
        {
            if (state == 0)
            {
                Time.timeScale = 0;
            }
            else
            {
                Time.timeScale = 1;
            }
        }

        public void ShowWinGame()
        {
            this.ShowPauseGame(0);
            this.PauseGame.SetActive(false);
            this.PlayGame.SetActive(false);
            this.WinGame.gameObject.SetActive(true);
            this.LoseGame.gameObject.SetActive(false);
        }

        public void ShowLoseGame()
        {
            this.ShowPauseGame(0);
            this.PauseGame.SetActive(false);
            this.PlayGame.SetActive(false);
            this.WinGame.gameObject.SetActive(false);
            this.LoseGame.gameObject.SetActive(true);
        }
    }
}