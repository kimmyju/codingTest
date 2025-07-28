#8:41분 시작
import sys
sys.setrecursionlimit(10000)

def LCA(a,b):
    if depth[a] > depth[b]:  # 더 깊은 depth가 b가 되도록
        temp = a
        a = b
        b = temp

    for k in range(kmax, -1, -1):  # depth 빠르게 맞추기
        if pow(2, k) <= depth[b] - depth[a]: #ex) a= 2, b=15 --> level차이: 4-1 = 3 즉 15에서 2로 맞추려면 3칸은 이동해도 된다는 소리, 몇 칸씩 올릴건지 결정
            if depth[a] <= depth[tree[k][b]]: #tree[k][b] = 5번 노드 / depth[5] = 2 와 depth[2]즉 a를 비교했을때, 여전히 b가 아래에 있다면 b를 이동, b를 이동시켜주는 역할
                b = tree[k][b]

    for k in range(kmax, -1, -1):  # 조상 빠르게 찾기
        if a == b: break # 올려준 a,b가 같으면 break
        if tree[k][a] != tree[k][b]: # a,b노드를 k만큼 위로 올렸을 때 같아지는건 너무 올라간걸수도 있으니까 패스, 다른거만 이동
            a = tree[k][a]
            b = tree[k][b]

    LCA = a
    if a != b:
        LCA = tree[0][LCA] # 바로 하나 위 노드
    return LCA

def DFS(v, d):
    visited[v] = True
    depth[v] = d
    for newN in A[v]:
        if not visited[newN]:
            tree[0][newN] = v
            DFS(newN, d+1)

input = sys.stdin.readline
#print = sys.stdout.write

n = int(input())
A = [[] for _ in range(n+1)] #1-n
visited = [False for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    A[a].append(b)
    A[b].append(a)
#print(A)

temp=1
kmax = 0
while temp <= n: #최대 가능 depth
    temp *= 2
    kmax += 1

print(kmax)
depth = [0 for _ in range(n+1)]
tree = [[0 for _ in range(n+1)] for _ in range(kmax+1)]
DFS(1, depth[0])

#점화식으로 나머지 채우기
for i in range(1, kmax+1):
    for j in range(1,n+1):
        tree[i][j] = tree[i-1][tree[i-1][j]]
print(depth)
print(tree)
#LCA 실행하기
res = []
m = int(input())
for _ in range(m):
    a,b = map(int, input().split())
    res.append(LCA(a,b))

for r in res:
    print(str(r)+'\n')






