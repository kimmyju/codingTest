#8:30분 시작
import sys
import heapq
input = sys.stdin.readline
#print = sys.stdout.write

n,m,k = map(int, input().split())

A = [[] for _ in range(n+1)]
D = [[sys.maxsize for _ in range(k)] for _ in range(n+1)]

D[1][0] = 0

for _ in range(m):
    s,e,w = map(int, input().split())
    A[s].append((e,w))
print(A)
print(D)

#queue에 삽입
pq = [(0, 1)]
#다익스트라 알고리즘
while pq:
    current = heapq.heappop(pq)
    current_node = current[1]
    current_value = current[0]
    for node in A[current_node]:
        next_n, next_v = node[0], node[1]
        temp_value = current_value + next_v
        if D[next_n][k-1] > temp_value:
            D[next_n][k-1] = temp_value
            D[next_n].sort()
            heapq.heappush(pq,(temp_value, next_n))

#출력
for i in range(1,n+1):
    if D[i][k-1] != sys.maxsize:
        print(str(D[i][k-1]) + '\n')
    else:
        print('-1\n')
