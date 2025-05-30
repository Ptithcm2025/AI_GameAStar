namespace UI
{
    using UnityEngine;
    using UnityEngine.UI;

    public class HomeUIView : MonoBehaviour
    {
        public Button PlayGame;

        private void Start()
        {
            this.PlayGame.onClick.AddListener(() =>
            {
                HomeUIController.Instance.LoadLevel(1);
            });
        }
    }
}
