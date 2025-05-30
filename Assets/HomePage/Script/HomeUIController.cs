namespace UI
{
    using CustomUtils;
    using UnityEngine;
    using UnityEngine.SceneManagement;

    public class HomeUIController : SingletonMono<HomeUIController>
    {
        [Header("View")]
        public HomeUIView homeView;

        public void LoadLevel(int level)
        {
            Time.timeScale = 1;
            SceneManager.LoadScene(level - 1);
        }
    }
}