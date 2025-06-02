import heapq

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
    return a, n, start, goal

def a_star(adj_matrix, num_cities, heuristics, start, goal):
    frontier = []
    heapq.heappush(frontier, (0, start))
    
    came_from = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        print("Priority Queue (Binary Heap):", frontier)
        cost, current = heapq.heappop(frontier)
        print("Choose min: ", cost, current)
        if current == goal: 
            break

        for neighbor, cost in adj_matrix[current]:
            if  (neighbor != -1):
                print(f"Updating {name[neighbor]}: came from {name[current]}", end = ' ')
                new_cost = cost_so_far[current] + cost
                print(new_cost, end = ' ')
                if (neighbor in cost_so_far):
                    print(cost_so_far[neighbor], end = ' ') 
                if (neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]):
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost + heuristics[name[neighbor]]
                    print(priority)
                    heapq.heappush(frontier, (priority, neighbor))
                    came_from[neighbor] = current
                else: 
                    print()
    
    return came_from, cost_so_far


def create_heuristics():
    return {
        'Oradea': 380, 'Zerind': 374, 'Arad': 366, 'Timisoara': 329,
        'Sibiu': 253, 'Lugoj': 244, 'Rimnicu Vilcea': 193, 'Fagaras': 176,
        'Pitesti': 100, 'Mehadia': 241, 'Drobeta': 242, 'Craiova': 160,
        'Bucharest': 0, 'Giurgiu': 77, 'Urziceni': 80, 'Hirsova': 151,
        'Eforie': 161, 'Vaslui': 199, 'Iasi': 226, 'Neamt': 234
    }

def main(): 
    adj_matrix, num_cities, start, goal = load_data()
    # for i in range(num_cities):
    #     print(name[i], ": ", end = ' ')
    #     for j in adj_matrix[i]:
    #         if j[0] != -1:
    #             print( j, end = ' ')
    #     print()
    heuristics = create_heuristics()
    came_from, cost_so_far = a_star(adj_matrix, num_cities, heuristics, start, goal)
    print("start: ", name[start])
    print("goal : ", name[goal]) 
    print("Route: ", end = ' ')
    print(name[start], end ='')

    start = goal
    route = []
    while came_from[goal] is not None: 
        route.append(goal)
        goal = came_from[goal]

    for value in route[::-1]: 
        print(' -> ', name[value], end = ' ')

    print() 
    print("Cost : ", cost_so_far[start])


if __name__ == "__main__":  
    main()
    