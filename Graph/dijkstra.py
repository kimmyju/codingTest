#7:13 시작
import sys
# import math
# print(math.log2(20000)*300000) --> 1초 하고도 남음

input = sys.stdin.readline
#print = sys.stdout.write

v,e = map(int,input().split())
s = int(input().strip())
A = [ [] for _ in range(v+1)]
#print(A)

for _ in range(e):
    n1,n2,w = map(int,input().split())
    A[n1].append((n2,w))
print(A)

max = 100000
D = [max]*(v+1)
D[s] = 0
visited = [0]*(v+1)

while True:
    if visited.count(1) == v:
        break

    if visited.count(1) == 0:
        min_idx = s
        min_val = D[s]    
    else:
        min_idx = -1
        min_val = max
        #최솟값 찾기
        for i in range(1,v+1):
            if i == s:
                continue
            if visited[i] == 0 and D[i] < min_val:
                min_idx = i
                min_val = D[i]

    visited[min_idx] = 1
    for n in A[min_idx]:
        n2, w = n
        if (min_val + w) < D[n2]:
            D[n2] = min_val + w
    print(visited)
    print(D)

#print(D,visited)

for i in range(1,v+1):
    if D[i] == max:
        print('INF')
    else:
        print(D[i])


#답안
# import sys
# input = sys.stdin.readline
# from queue import PriorityQueue

# V, E = map(int, input().split())
# K = int(input())
# distance = [sys.maxsize] * (V + 1)
# visited = [False] * (V + 1)
# myList = [[] for _ in range(V + 1)]
# q = PriorityQueue()

# for _ in range(E):
#     u, v, w = map(int, input().split())  # 가중치가 있는 인접 리스트 저장
#     myList[u].append((v, w))

# q.put((0, K))  # K를 시작점으로 설정 (w,v)형태로 삽입
# distance[K] = 0
# while q.qsize() > 0:
#     current = q.get()
#     c_v = current[1]
#     if visited[c_v]:
#         continue
#     visited[c_v] = True
#     for tmp in myList[c_v]:
#         next = tmp[0] #다음노드
#         value = tmp[1] #가중치
#         if distance[next] > distance[c_v] + value:  # 최소 거리로 업데이트
#             distance[next] = distance[c_v] + value
#             q.put((distance[next], next))
# for i in range(1, V + 1):
#     if visited[i]:
#         print(distance[i])
#     else:
#         print("INF")