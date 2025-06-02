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

def dfs(a, start, goal): 
    print(start, end  = " ")

    for i in a[start] : 
        if not visited[i]:
            visited[i] = True
            dfs(a, i, goal)

def main():
    n, m, a = read_data()

    global visited
    visited = [False] * len(a)
    visited[1] = True
    
    dfs(a, 1, 7)

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