import random
import heapq
import math 

# Dữ liệu bản đồ Romania
name =  ["Oradea", "Zerind", "Arad", "Timisoara", "Sibiu", 
        "Lugoj", "Rimnicu Vilcea", "Fagaras", "Pitesti", "Mehadia", 
        "Dobreta", "Craiova", "Bucharest", "Giurgiu", "Urziceni", 
        "Hirsova", "Eforie", "Vaslui", "Iasi", "Neamt"]

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
    return a, n

def calculate_distance_dijkstra(city1, city2, adj_matrix, num_cities):
    if city1 == city2:
        return 0
    distances = {city: float('inf') for city in range(num_cities)}
    distances[city1] = 0
    priority_queue = [(0, city1)]

    while priority_queue:
        current_distance, current_city = heapq.heappop(priority_queue)
        if current_distance > distances[current_city]:
            continue
        for neighbor, distance in adj_matrix[current_city]: 
            if neighbor == -1:
                break
            new_distance = current_distance + distance
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances[city2]

def calculate_total_distance(route, total_cities, adj_matrix):
    total_distance = 0
    for i in range(len(route) - 1): 
        dist = calculate_distance_dijkstra(route[i], route[i + 1], adj_matrix, total_cities)
        if dist == float('inf'):
            return float('inf')
        total_distance += dist

    dist = calculate_distance_dijkstra(route[-1], route[0], adj_matrix, total_cities)
    if dist == float('inf'):
        return float('inf')
    total_distance += dist
    return total_distance  

def generate_neighbors(route):   
    neighbors = []

    for i in range(len(route)): 
        for j in range(i + 1, len(route)): 
            neighbor = route[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

def hill_climbing(adj_matrix, total_cities, max_iterations = 1000):
    current_route = list(range(total_cities))
    random.shuffle(current_route)

    best_route = current_route[:]
    best_distance = calculate_total_distance(best_route, total_cities, adj_matrix)

    for _ in range(max_iterations):
        neighbors = generate_neighbors(best_route)
        improved = False
        for neighbor in neighbors:
            distance = calculate_total_distance(neighbor, total_cities, adj_matrix)
            if distance < best_distance:
                best_distance = distance
                best_route = neighbor[:]
                improved = True
                break

        if not improved:
            break

    return best_route, best_distance

def main():
    adj_matrix, num_cities = load_data()
    best_route, best_distance = hill_climbing(adj_matrix, num_cities)
    # dem = 0
    # for i in range(len(best_route)):
    #     city = best_route[i]
    #     if dem > 0:
    #         prev_city = best_route[i - 1]  
    #         print(name[prev_city], name[city], calculate_distance_dijkstra(prev_city, city, adj_matrix, num_cities))
    #     else:
    #         print(name[city])
    #     dem += 1
    print(" -> ".join(name[city] for city in best_route))
    print(best_distance)


if __name__ == "__main__":
    main()