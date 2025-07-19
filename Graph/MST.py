#3: 25 분 시작
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
print = sys.stdout.write

def find(a): # 대표노드를 찾는다
    if a == uf_L[a]:
        return a
    else:
        uf_L[a] = find(uf_L[a])
        return uf_L[a]
def union(a,b): #두 노드를 연결한다
    a = find(a)
    b = find(b)

    if a != b:
        uf_L[b] = a

v,e = map(int, input().split())

EdgeL = []
uf_L = [i for i in range(v+1)]

for _ in range(1,e+1):
    abc = list(map(int, input().split()))
    EdgeL.append(abc)

EdgeL.sort(key = lambda x: x[2])
EdgeL.insert(0,[])

weightL = []

for i in range(1,e+1): #123
    if len(weightL) == v-1:
        break

    n1,n2,w = EdgeL[i]
    a = find(n1)
    b = find(n2)
    #대표노드가 일치한다면 패스
    if a == b:
        continue
    #부모노드가 일치하지 않는다면 연결
    else:
        union(n1,n2)
        weightL.append(w) 

sum = 0
for n in weightL:
    sum+= n
print(str(sum)+'\n')


#답안
import sys
from queue import PriorityQueue

input = sys.stdin.readline
N, M = map(int, input().split())
pq = PriorityQueue()
parent = [0] * (N + 1)
for i in range(N + 1):
    parent[i] = i

for i in range(M):
    s, e, v = map(int, input().split())
    pq.put((v, s, e))  # 제일 앞 순서로 정렬되므로 가중치를 제일 앞 순서로 함

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

useEdge = 0
result = 0
while useEdge < N - 1:  # MST는 한상 N-1의 에지를 사용함
    v, s, e = pq.get()
    if find(s) != find(e):  # 같은 부모가 아닌 경우만 연결
        union(s, e)
        result += v
        useEdge += 1

print(result)
