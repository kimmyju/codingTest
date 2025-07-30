# 4:11분 시작
import sys

input = sys.stdin.readline
print = sys.stdout.write

def ques1(k):
    r = [0] * (n+1)
    for i in range(1,n+1):
        cnt = 1
        for j in range(1,n+1): # j는 후보 숫자
            if visited[j] == True:
                continue
            if k <= fact[n-i]*cnt:
                k = k - (fact[n-i]*(cnt-1))
                r[i] = j
                visited[j] = True
                break
            cnt+=1
    return r

def ques2(arr):
    temp_k = 1
    for i in range(1,n+1):
        num = arr[i]
        cnt = 0
        for j in range(1, arr[i]):
            if not visited[j]:
                cnt+=1
        temp_k += (fact[n-i] * cnt)
        visited[num] = True
    return temp_k



n = int(input())
line = list(map(int, input().split()))

fact = [0] * (n+1)
visited = [False] * (n+1)
fact[0] = 1
for i in range(1,n+1):
    fact[i] = fact[i-1] * i

if line[0] == 1: #소문제 1이라면
    k = line[1]
    res = ques1(k)
    for i in range(1,len(res)):
        print(str(res[i])+' ')
    print('\n')

else: #소문제 2라면
    case = line[:] #빈거는 0이라는 뜻 즉끝까지, -1 + 1 -->  하나 덜까지 슬라이싱하는거니까, +1로 끝까지 포함시켜줌
    case[0] = 0
    res = ques2(case)

    print(str(res)+'\n')

