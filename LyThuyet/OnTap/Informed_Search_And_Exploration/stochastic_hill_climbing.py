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

def hill_climbing(graph, n, max_iterations = 1000):
    current_route = list(range(1, n + 1))
    random.shuffle(current_route)
    current_distance = caculate_total_distance(current_route, graph)

    for _ in range(max_iterations): 
        neighbors = generate_neighbor(current_route)
        random_neighbor = random.choice(neighbors)
        distance_random_neighbor = caculate_total_distance(random_neighbor, graph)

        if (distance_random_neighbor < current_distance): 
            current_route = random_neighbor
            current_distance = distance_random_neighbor

    print(current_distance)
    print(current_route)

def main(): 
    n, m, graph = read_data()
    hill_climbing(graph, n)

if __name__ == "__main__":
    main()

"""
15 20
1 2 1
1 3 79
1 4 29
2 5 47
2 6 82
3 12 10
4 7 91
4 8 73
4 9 96
5 3 10
6 10 66
6 11 99
7 11 22
7 14 22
8 12 49
8 13 8
9 13 44
9 14 93
10 2 10
12 1 10
"""
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