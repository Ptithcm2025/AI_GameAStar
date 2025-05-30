namespace CoreGamePlay.Controller
{
    using CoreGamePlay.Model;
    using CoreGamePlay.View;
    using CustomUtils;
    using Data;
    using UI;
    using UnityEngine;
    using UnityEngine.UI;

    public class MatrixController : SingletonMono<MatrixController>
    {
        [Header("Matrix")]
        public MatrixElementModel[,] MatrixElementModelList;
        public MatrixElementView MatrixElementPrefab;
        public RectTransform MatrixElementParent;
        public Vector2Int Size;

        [Header("Data")]
        public MatrixData MatrixData;

        [Header("Pause")]
        public Button PauseButton;
        private int state = 1;

        private void Start()
        {
            InitMatrix(1);
            this.state = 1;
            PauseButton.onClick.AddListener(() =>
            {
                if (state == 1)
                {
                    this.state = 0;
                }
                else
                {
                    this.state = 1;
                }
                UIManager.Instance.ShowPauseGame(this.state);
            });
        }

        public void InitMatrix(int level)
        {
            int[,] map = MatrixData.GetMap(level - 1);

            Size.x = map.GetLength(0);
            Size.y = map.GetLength(1);

            this.MatrixElementModelList = new MatrixElementModel[Size.x, Size.y];

            //Debug.Log(Size.x + " " + Size.y);

            for (int i = 0; i < Size.x; ++i)
            {
                for (int j = 0; j < Size.y; ++j)
                {
                    // Set View
                    MatrixElementView elementView =  Instantiate(MatrixElementPrefab, MatrixElementParent);

                    // Set Model
                    MatrixElementModel elementModel = new MatrixElementModel();
                    elementModel.Init(new Vector2Int(i, j), elementView);
                    elementModel.SetType(map[i, j]);

                    // Add to List
                    this.MatrixElementModelList[i, j] = elementModel;
                }
            }
            EnemyController.Instance.SpawnListEnemy();
            PlayerController.Instance.SpawnPlayer();
        }
    }
}