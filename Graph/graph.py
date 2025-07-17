import sys
from collections import deque
def BFS(v):
    queue = deque()
    dis = 0
    visited[v] = dis
    queue.appendleft(v)

    while queue:
        val = queue.pop()
        dis+=1
        for node in A[val]: #빈리스트이면 어차피 한번도 실행되지 않음
            if visited[node] == 0:
                visited[node] = dis
                queue.appendleft(node)
               

input = sys.stdin.readline
print = sys.stdout.write
n,m,k,x = map(int, input().split())
A = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(1, m+1):
    a,b = map(int, input().split())
    A[a].append(b)

BFS(x)

answer = []
for i in range(1, n+1):
    if visited[i] == k:
        answer.append(i)

if not answer:
    print(str(-1)+'\n')

else:
    answer.sort()
    for i in answer:
        print(str(i)+'\n')