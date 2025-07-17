#12:44분 시작
import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
m = int(input())
arr = [[sys.maxsize for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1,n+1):
        if i == j:
            arr[i][j] = 0

for _ in range(1, m+1):
    a,b,w = map(int, input().split())
    if arr[a][b] > w:
        arr[a][b] = w
#print(arr)

#플로이드 워셜
for k in range(1,n+1):
    for s in range(1,n+1):
        for e in range(1,n+1):
            arr[s][e] = min(arr[s][e], arr[s][k]+arr[k][e])

#print(arr)
for i in range(1, n+1):
    for j in range(1,n+1):
        if arr[i][j] == sys.maxsize:
            print('0 ')
        else:
            print(str(arr[i][j])+' ')
    print('\n')
