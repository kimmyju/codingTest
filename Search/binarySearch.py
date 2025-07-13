#8:32분,2n+logn --> 200,000 +16
#내 답안
import sys

def binary_search(s,e, search_num):
    res = 0
    if s <= e:
        m = (s+e) // 2
        if N[m] == search_num:
            return 1
        elif N[m] > search_num:
            res = binary_search(s,m-1, search_num)
        else:
            res = binary_search(m+1,e, search_num)
    return res


input = sys.stdin.readline
print = sys.stdout.write

n = int(input().strip())
N = list(map(int, input().split()))
N.sort()

m = int(input().strip())
M = list(map(int, input().split()))


for i in range(m):
    res = binary_search(0,n-1, M[i])
    print(str(res)+'\n')

# 답안
N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
target_list = list(map(int, input().split()))
for i in range(M):
    find = False
    target = target_list[i]
    # 이진탐색 시작
    start = 0
    end = len(A) - 1
    while start <= end:
        midi = int((start + end) / 2)
        midv = A[midi]
        if midv > target:
            end = midi - 1
        elif midv < target:
            start = midi + 1
        else:
            find = True
            break
    if find:
        print(1)
    else:
        print(0)