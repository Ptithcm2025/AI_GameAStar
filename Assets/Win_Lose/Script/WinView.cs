namespace UI
{
    using UnityEngine;
    using UnityEngine.UI;

    public class WinView : MonoBehaviour
    {
        public Button NextLevel;
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

            this.NextLevel.onClick.AddListener(() =>
            {
                Debug.Log("NextLevel");
            });
        }
    }
}   