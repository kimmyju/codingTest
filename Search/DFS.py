# 2시 46분까지 500,000
import sys
sys.setrecursionlimit(10000)
def dfs(s):
    #현재 노드를 방문처리한다.
    visited[s] = True
    #인접 리스트 확인 후, 방문하지 않은 모든 노드에 접근
    for node in A[s]:
        if not visited[node]:
            dfs(node)


input = sys.stdin.readline
print = sys.stdout.write

n,m = map(int,input().split()) #map의 반환은 객체/ map(함수, 이터러블) / 이터러블:하나씩 값을 꺼낼 수 있는 객체
visited = [False]*(n+1)
A = [[] for _ in range(n+1)] #리스트 컴프리헨션 문법 [값 for 변수 in 반복가능한객체]
for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

count = 0

for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        count+=1

print(str(count))
