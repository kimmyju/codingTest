#3시 24분 시작 / 4: 09분 마무리 (40분)
import sys

input = sys.stdin.readline
print = sys.stdout.write

N,M = map(int, input().split())

edgeL = [[]]
D = [sys.maxsize]*(N+1)
D[1] = 0
for _ in range(1, M+1):
    abc = list(map(int, input().split()))
    edgeL.append(abc)

#벨만포드 알고리즘
isCycle = False
for i in range(1,N+1): #N-1만큼 반복 후 음수 사이클을 위해 한번 더 수행
    for j in range(1,M+1): #에지 수만큼 반복
        s,e,w = edgeL[j] #파이썬에서는 리스트나 튜플은 요소갯수가 일치하면 각 변수에 매핑 가능

        if D[s] != sys.maxsize and D[e] > (D[s] + w):
            D[e] = D[s] + w
            
            if i == N:
                isCycle = True
                break


if isCycle == True:
    print('-1\n')

else:
    for i in range(2, N+1):
        if D[i] == sys.maxsize:
            print('-1\n')
        else:
            print(str(D[i])+'\n')