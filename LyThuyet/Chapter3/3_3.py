# Đánh số các đỉnh bằng số tự nhiên từ 0 đến n - 1.
name =  ["Oradea", "Zerind", "Arad", "Timisoara", "Sibiu", 
        "Lugoj", "Rimnicu Vilcea", "Fagaras", "Pitesti", "Mehadia", 
        "Dobreta", "Craiova", "Bucharest", "Giurgiu", "Urziceni", 
        "Hirsova", "Eforie", "Vaslui", "Lasi", "Neamt"]
def load_data(): 
    n = 20 
    a = [[[-1, -1] for i in range(4)] for j in range(n)]
    # Tạo danh sách kè của các đỉnh.
    a[0][0] = [1, 71]
    a[0][1] = [4, 151]
    a[1][0] = [0, 71]
    a[1][1] = [2, 75]
    a[2][0] = [1, 75]
    a[2][1] = [3, 118]
    a[2][2] = [4, 140]
    a[3][0] = [2, 118]
    a[3][1] = [5, 111]
    a[4][0] = [0, 151]
    a[4][1] = [2, 140]
    a[4][2] = [7, 99]
    a[4][3] = [6, 80]
    a[5][0] = [3, 111]
    a[5][1] = [9, 70]
    a[6][0] = [4, 80]
    a[6][1] = [8, 97]
    a[6][2] = [11, 146]
    a[7][0] = [4, 99]
    a[7][1] = [12, 211]
    a[8][0] = [6, 97]
    a[8][1] = [11, 138]
    a[8][2] = [12, 101]
    a[9][0] = [5, 70]
    a[9][1] = [10, 75]
    a[10][0] = [9, 75]
    a[10][1] = [11, 120]
    a[11][0] = [6, 146]
    a[11][1] = [8, 138]
    a[11][2] = [10, 120]
    a[12][0] = [7, 211]
    a[12][1] = [8, 101]
    a[12][2] = [13, 90]
    a[12][3] = [14, 85]
    a[13][0] = [12, 90]
    a[14][0] = [12, 85]
    a[14][1] = [15, 98]
    a[14][2] = [17, 142]
    a[15][0] = [14, 98]
    a[15][1] = [16, 86]
    a[16][0] = [15, 86]
    a[17][0] = [14, 142]
    a[17][1] = [18, 92]
    a[18][0] = [17, 92]
    a[18][1] = [19, 87]
    a[19][0] = [18, 87]
    start = 2
    goal = 12   
    return n, a, start, goal

def depth_limited_search(a, current, goal, cost, min_cost, depth, path, min_path, visited_states): 
    # Nếu độ sâu này không thể --> Thoát. 
    if depth < 0: 
        return False

    # Nếu đã duyệt qua và có đường đi tốt hơn --> Thoát.
    if current in visited_states: 
        if visited_states[current] < cost:
            return False

    # Gán cost vào visited_states.
    visited_states[current] = cost
    # Thêm điểm hiện tại vào path.
    path.append(current)

    # Nếu đã đến điểm cuối --> Kiểm tra xem có đường đi tốt hơn không.
    if current == goal: 
        if cost < min_cost[0]: 
            # Nếu tốt hơn, cập nhật lại giá trị.
            min_cost[0] = cost
            min_path[:] = path[:]
        path.pop() # Backtrack trước khi return True để tìm đương tối ưu hơn. 
        # Nếu tìm thấy đường đi tốt hơn --> Thoát.
        return True  

    found = False # Giá trị sẽ return.
    # Duyệt qua các điểm kè của điểm hiện tại.
    for neighbor, _ in a[current]:
        # Nếu tồn tại đường đi và không phải là điểm đã đi qua.
        if neighbor != -1 and neighbor not in path:
            # Thực hiện để tìm đường đi tốt nhất.
            if depth_limited_search(a, neighbor, goal, cost + 1, min_cost, depth - 1, path, min_path, visited_states):
                # Nếu tìm thấy đường đi tốt hơn --> Thoát.
                found = True

    # Backtrack.
    path.pop()
    # Return giá trị tìm được.
    return found

def Iterative_Deepening_DepthFirstSearch(n, a, start, goal):
    limit = 0
    visited_states = {}
    while (limit < n):
        min_path = []
        min_cost = [float('inf')]
        if depth_limited_search(a, start, goal, 1, min_cost, limit, [], min_path, visited_states):
            return min_path, min_cost[0]
        limit += 1
    return [], float('inf')
        
def main(): 
    n, a, start, goal = load_data()
    min_path, min_cost = Iterative_Deepening_DepthFirstSearch(n, a, start, goal)
    print("Cost: ", min_cost, "(Số đỉnh đi qua)")
    print("Path: ", end = "")
    for value in min_path: 
        print(name[value], end = " ")

if __name__ == "__main__":
    main()