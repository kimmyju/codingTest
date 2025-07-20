#7:39시작
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
print = sys.stdout.write

def dfs(n):
    visited[n] = True
    for node in A[n]:
        if not visited[node]: #방문했다는 것은 부모 노드라는거(차례대로 타고 내려가니까), 내 부모 노드의 경우 dfs나 부모노드를 저장하지 않음
            dfs(node)
            answer[node] = n #위에줄이랑 지금 라인 순서 바꿔도 상관 x
        
v = int(input())
A = [[] for _ in range(v+1)]
visited = [False]* (v+1)
answer = [0]* (v+1)

for _ in range(1,v):
    n1, n2 = map(int, input().split())
    A[n1].append(n2)
    A[n2].append(n1)

dfs(1)

for i in range(2, v+1):
    print(str(answer[i])+'\n')
