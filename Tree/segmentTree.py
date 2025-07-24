#1:55분시작 3:13분 완성
#a=1일때 b-->c변경 / a=2 b-->c까지의 합
import sys

def hap(s,e):
    select = []
    
    while s <= e:
        #s,e가 왼쪽인지 오른쪽이지 확인하는 작업
        if s % 2 == 1:
            select.append(tree[s])
        if e % 2 == 0:
            select.append(tree[e])

        # s와 e값 업데이트
        s = (s+1) // 2
        e = (e-1) // 2

    sum = 0
    for num in select:
        sum += num
    print(str(sum))

    
def change(idx, value):
    cha = value - tree[idx] #무조건 새로 들어온 값에서 기존 값을 빼야함
    tree[idx] = value

    idx = idx // 2
    while idx >= 1:
        tree[idx] += cha
        idx = idx // 2
        
input = sys.stdin.readline
print = sys.stdout.write

n,m,k = map(int, input().split())

size = 0
if n % 2 == 0:
    size = n // 2
else:
    size = n // 2 + 1

start_idx = 2**size 
size = 2*(2**size) 
tree = [0 for _ in range(size)]

tmp_start = start_idx
for i in range(n):
    if tmp_start < len(tree):
        tree[tmp_start] = int(input())
        tmp_start += 1

tmp_start -= 1
# 나머지 부분 채워야댐 start_idx부터 1번까지
for i in range(tmp_start, 1,-1):
    temp_idx = i // 2
    tree[temp_idx] += tree[i]

#m번 요소값을 변경/k번 합구하기
for i in range(m+k):
    a,b,c = map(int,input().split())
    temp_b = start_idx + b - 1
    
    if a == 1: #요소 변경
        change(temp_b, c)
    else: # 합구하기
        temp_c = start_idx + c - 1
        hap(temp_b,temp_c)

#답안
# import sys
# input = sys.stdin.readline
# N, M, K = map(int, input().split())  # 수의 개수, 변경이 일어나는 횟수, 구간 합을 구하는 횟수
# treeHeight = 0
# lenght = N

# while lenght != 0:
#     lenght //= 2
#     treeHeight += 1

# treeSize = pow(2, treeHeight + 1)
# leftNodeStartIndex = treeSize // 2 - 1
# tree = [0] * (treeSize + 1)

# # 데이터를 리프노드에 저장
# for i in range(leftNodeStartIndex + 1, leftNodeStartIndex + N + 1):
#     tree[i] = int(input())

# # 인덱스 트리 생성 함수
# def setTree(i):
#     while i != 1:
#         tree[i // 2] += tree[i]
#         i -= 1

# setTree(treeSize - 1)


# # 값 변경 함수
# def changeVal(index, value):
#     diff = value - tree[index]
#     while index > 0:
#         tree[index] = tree[index] + diff
#         index = index // 2

# # 구간 합 계산 함수
# def getSum(s, e):
#     partSum = 0
#     while s <= e:
#         if s % 2 == 1:
#             partSum += tree[s]
#             s += 1
#         if e % 2 == 0:
#             partSum += tree[e]
#             e -= 1
#         s = s // 2
#         e = e // 2
#     return partSum

# for _ in range(M + K):
#     question, s, e = map(int, input().split())
#     if question == 1:
#         changeVal(leftNodeStartIndex + s, e)
#     elif question == 2:
#         s = s + leftNodeStartIndex
#         e = e + leftNodeStartIndex
#         print(getSum(s, e))