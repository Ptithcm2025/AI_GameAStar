from heapq import heappush, heappop
def read_data():
    n, m = map(int, input().split())
    a = [[] for _ in range(n + 1)]
    for i in range(m): 
        u, v = map(int, input().split())
        a[u].append(v)
    # for i in range(1, n + 1): 
    #     print(i, ":", end = " ")
    #     for j in a[i]: 
    #         print(j, end = " ")
    #     print()
    # Mỗi mục tiêu đến Goal
    heuristics = {
        1: 10, 
        2: 8, 
        3: 12, 
        4: 9,
        5: 7, 
        6: 6, 
        7: 4, 
        8: 5,
        9: 3, 
        10: 0, 
        11: 4, 
        12: 5,
        13: 2, 
        14: 0
    }
    # for i in range(1, n + 1): 
    #     print(heuristics[i], end = " ")
    return n, m, a, heuristics

def greedy_best_first_search(start, goal, a, h):
    visited = set()
    pq = []  # (heuristic, node)
    path = []

    heappush(pq, (h[start], start))

    while pq:
        _, nodeCurrent = heappop(pq)
        
        if nodeCurrent in visited:
            continue
        
        visited.add(nodeCurrent)
        path.append(nodeCurrent)

        if nodeCurrent == goal:
            print("Path:", path)
            print("Goal reached!")
            return

        for neighbor in a[nodeCurrent]:
            if neighbor not in visited:
                heappush(pq, (h[neighbor], neighbor))

    print("No Path To Goal!!")

def main():
    n, m, a, h = read_data()
    
    start = 1 
    goal = 10

    greedy_best_first_search(start, goal, a, h)


if __name__ == "__main__":
    main()

"""
14 15
1 2
1 3 
1 4
2 5 
2 6
4 7
4 8
4 9
6 10
6 11
7 11
8 12
8 13
9 13
9 14
"""