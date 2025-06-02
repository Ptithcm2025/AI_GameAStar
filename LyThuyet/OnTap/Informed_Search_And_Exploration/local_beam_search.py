import random

def read_data():
    n, m = map(int, input().split())
    a = [[] for _ in range(n + 1)]
    for i in range(m): 
        u, v, w = map(int, input().split())
        a[u].append((v, w))
        a[v].append((u, w))
    for i in range(1, n): 
        print(i, ":", end = " ")
        for j in a[i]: 
            print(j, end = " ")
        print()
    return n, m, a

def caculate_total_distance(route, graph): 
    total_distance = 0

    for i in range(len(route) - 1):
        u, v = route[i], route[i + 1]
        weight = next((w for neighbor, w in graph[u] if neighbor == v), float('inf'))
        if weight == float('inf'):
            return float('inf')
        total_distance += weight

    weight = next((w for neighbor, w in graph[route[-1]] if neighbor == route[0]), float('inf'))
    if weight == float('inf'):
            return float('inf')
    total_distance += weight
    return total_distance

def generate_neighbor(route): 
    neighbors = []
    for i in range(len(route)):
        for j in range(i + 1, len(route)):
            neighbor = route[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

def local_beam(graph, n, k = 3, max_iterations = 1000):
    current_routes = [random.sample(range(1, n + 1), n) for _ in range(k)]
    current_distances = [caculate_total_distance(route, graph) for route in current_routes]
    print("Init Routes:", current_routes)
    print("Distances:", current_distances)
    for _ in range(max_iterations): 
        all_neighbors = []
        for route in current_routes:
            all_neighbors.extend(generate_neighbor(route))

        all_neighbor_distances = [(neighbor, caculate_total_distance(neighbor, graph)) for neighbor in all_neighbors]   
        all_neighbor_distances.sort(key=lambda x: x[1])
        current_routess = [route for route, _ in all_neighbor_distances[:k]]
        current_distancess = [dist for _, dist in all_neighbor_distances[:k]]
        improve = False
        for i, _ in enumerate(current_distances):
            if current_distances[i] < current_distancess[i] or current_distances[i] == float('inf'):
                current_routes = current_routess
                current_distances = current_distancess
                improve = True

        if not improve:
            break

    best_route = current_routes[0]
    best_distance = current_distances[0]
    print("Routes After Cal:", current_routes)
    print("Distances After Cal:", current_distances)
    print("Best Rote: ", current_routes[0])
    print("Best Rote: ", current_distances[0])

def main(): 
    n, m, graph = read_data()
    local_beam(graph, n, 3)

if __name__ == "__main__":
    main()

"""
5 8
1 2 5
1 4 10
1 5 8 
2 3 9 
2 4 14
2 5 22
3 5 98
4 5 1000
"""