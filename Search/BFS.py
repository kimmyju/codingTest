# 4:40분까지
import sys
from collections import deque
sys.setrecursionlimit(10000)

def dfs(v):
    visited[v] = True
    print(str(v)+' ')

    for node in A[v]:
        if not visited[node]:
            dfs(node)

    

def bfs(v):
    dq = deque()
    visited[v] = True
    dq.appendleft(v)

    while dq:
        Cnode = dq.pop()
        print(str(Cnode)+' ')
        for node in A[Cnode]:
            if not visited[node]:
                visited[node] = True
                dq.appendleft(node)



input = sys.stdin.readline
print = sys.stdout.write

n, m, v = map(int, input().split())
A = [[] for _ in range(n+1)]
visited = [False]*(n+1)


for _ in range(1,m+1):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

for i in range(1,n+1):
    A[i].sort()


dfs(v)
visited = [False]*(n+1)
print('\n')
bfs(v)