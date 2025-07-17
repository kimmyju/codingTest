# 7: 35
import sys
sys.setrecursionlimit(10000)
def union(a,b):
    if a==b:
        return
    a = find(a)
    b = find(b)

    if a < b:
        uf_L[b] = a
    else:
        uf_L[a] = b


def find(a):
    root_node = -1
    # 대표 노드를 찾았을 경우 /  결국 같아질때 멈추고 그 값으로 이 전 재귀 오기 전에 봤던 배열 요소들도 다 같이질때의 노드 번호로 덮어씌우니까, 반환값은 if else문 둘다 같은셈
    if a == uf_L[a]:
        root_node = uf_L[a]
        return root_node
    
    else:
        root_node = find(uf_L[a])
        uf_L[a] = root_node
        return root_node

    #대표노드가 아직 안나온 경우
input = sys.stdin.readline
#print = sys.stdout.write

n,m = map(int, input().split())
uf_L = [i for i in range(n+1)]
print(uf_L)
#질의 시작
for _ in range(m):
    is_find, a, b = map(int, input().split())

    if is_find:
        a_root = find(a)
        b_root = find(b)
        if a_root == b_root:
            print('YES\n')
        else:
            print('NO\n')

    else:
        union(a,b)

#답안
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
N, M = map(int, input().split())
parent = [0] * (N + 1)


def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])  # 재귀 형태로 구현 -> 경로 압축 부분
        return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a


def checkSame(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return True
    return False


for i in range(0, N + 1):
    parent[i] = i

for i in range(M):
    question, a, b = map(int, input().split())
    if question == 0:
        union(a, b)
    else:
        if checkSame(a, b):
            print("YES")
        else:
            print("NO")