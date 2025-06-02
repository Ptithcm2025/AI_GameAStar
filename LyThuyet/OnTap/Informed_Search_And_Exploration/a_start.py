import heapq

def read_data():
    # n, m = map(int, input().split())
    a = {
        1: [(2, 1), (3, 4), (4, 3)],
        2: [(5, 5), (6, 6)],
        3: [],
        4: [(7, 8), (8, 2), (9, 3)],
        5: [],
        6: [(10, 7), (11, 4)],
        7: [(11, 2)],
        8: [(12, 5), (13, 6)],
        9: [(13, 7), (14, 4)],
        10: [],
        11: [],
        12: [],
        13: [],
        14: []
    }
    # a = [[] for _ in range(n + 1)]
    # for i in range(m): 
    #     u, v = map(int, input().split())
    #     a[u].append(v)
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
    return a, heuristics

def a_start(start, goal, h, a):
    priority_queue = []
    heapq.heappush(priority_queue, (0 + h[start], start, 0))
    came_from = {}
    cost_so_far = {start: 0}

    while priority_queue: 
        _, current, g_current = heapq.heappop(priority_queue)

        for neighbor, cost in a[current]:
            new_cost = g_current + cost

            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                f  = new_cost + h[neighbor]

                heapq.heappush(priority_queue, (f, neighbor, new_cost))
                came_from[neighbor] = current

    print(cost_so_far)
                

def main():
    a, h = read_data()
    a_start(1, 14, h, a)

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