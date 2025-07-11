using CoreGamePlay.Controller;
using UnityEngine;

public class PlayerModel
{
    public Vector2Int gridPosition { get; private set; }

    public PlayerModel(Vector2Int startGrid)
    {
        this.gridPosition = startGrid;
    }
    public bool Move(Vector2Int direction)
    {
        Vector2Int position = this.gridPosition + direction;
        if (MatrixController.Instance.MatrixElementModelList[position.x, position.y].Type == 1) return false;
        this.gridPosition = position;
        return true;
    }
}
