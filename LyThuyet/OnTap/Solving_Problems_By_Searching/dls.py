from collections import deque

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
    return n, m, a

visited = []

def dls(a, start, goal, limit, currentLimit): 
    if currentLimit > limit: return
    print(start, end = " ")

    for i in a[start]: 
        if not visited[i]: 
            visited[i] = True
            dls(a, i, goal, limit, currentLimit + 1)

def main():
    n, m, a = read_data()
    global visited 
    visited = [False] * len(a)

    start = 1 
    goal = 7
    limit = 2
    visited[start] = True

    # IDDFS
    for i in range(limit): 
        currentLimit = 0
        visited = [False] * len(a)
        visited[start] = True
        print(i + 1, "->" , end = " ")
        dls(a, start, goal, i + 1, currentLimit)
        print()

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