namespace CoreGamePlay.Model
{
    using CoreGamePlay.View;
    using UnityEngine;

    public class EnemyModel
    {
        public EnemyView EnemyView;
        public Vector2Int Position;
        
        public void Init(EnemyView enemyView, Vector2Int position)
        {
            this.EnemyView = enemyView;
            this.SetPosition(position, 0.1f);
            this.EnemyView.IdleState();
        }

        public void SetPosition(Vector2Int position, float moveSpeed)
        {
            Vector2Int dir = position - this.Position;
            if (dir.x == 0 && dir.y == 1)
            {
                this.EnemyView.RightState();
            }
            else if (dir.x == 0 && dir.y == -1)
            {
                this.EnemyView.LeftState();
            }
            else if (dir.x == -1 && dir.y == 0)
            {
                this.EnemyView.UpState();
            }
            else if (dir.x == 1 && dir.y == 0)
            {
                this.EnemyView.DownState();
            }
            else if (dir.y > 0)
            {
                this.EnemyView.RightState();
            }
            else if (dir.y < 0)
            {
                this.EnemyView.LeftState();
            }
            this.Position = position;
            this.EnemyView.SetPosition(position, moveSpeed);
        }
    }
}