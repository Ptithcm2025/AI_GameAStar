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

def bfs(a, start, goal):
    visited = [False] * len(a)
    visited[start] = True
    q = deque([(start, None)])
    while (q): 
        u, parent = q.popleft()
        print(u, parent)
        for i in a[u]: 
            if not visited[i]: 
                q.append((i, u))
                visited[i] = True

def main():
    n, m, a = read_data()
    bfs(a, 1, n)

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