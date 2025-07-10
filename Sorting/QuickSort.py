# 1. 내 풀이
# import sys
# def quickSort(listB, pivot):
#     left, right = 0, pivot-1
#     #1. left < right 인 경우
#     #2. left와 right가 겹치는 경우
#     while left < right:
#         # start 찾기, pivot값 보다 작으면 오른쪽으로 한 칸
#         if listB[pivot] >= listB[left]:
#             left+=1

#         if listB[pivot] < listB[right]:
#             right-=1

#         if listB[right] < listB[pivot] <= listB[left]:
#             temp = listB[right]
#             listB[right] = listB[left]
#             listB[left] = temp
       
#     # 겹치거나 엇갈려서 끝났다면?
#     if right <= left:
#         temp = listB[pivot]
#         for i in range(pivot,left+1,-1):
#             listB[i] = listB[i-1]
#         listB[left+1] = temp

#         # 재귀 호출
#         if right < left:
#             quickSort(left+1, left+2, right)

#         else:
#             quickSort(pivot, left, right)

        


# input = sys.stdin.readline
# n,k = map(int, input().split())

# listA = list(map(int, input().split()))
# print(listA)

# # 퀵정렬
# pivot = len(listA) - 1
# quickSort(listA, pivot)

#2. 답지 풀이
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 퀵 정렬 수행 함수
def quickSort(S, E, K):
    global A
    if S < E:
        pivot = partition(S, E) # 이작업이 결국, 정렬을 통해 pivot, 즉 고정값을 찾는다는 것
        if pivot == K:  # K번째 수가 pivot이면 더이상 구할 필요 없음
            return
        elif K < pivot:  # K가 pivot보다 작으면 왼쪽 그룹만 정렬
            quickSort(S, pivot - 1, K)
        else:  # K가 pivot보다 크면 오른쪽 그룹만 정렬
            quickSort(pivot + 1, E, K)

# 교환 함수
def swap(i, j):
    global A
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

# pivot 구하기
def partition(S, E):
    global A

    if S + 1 == E: # 재귀 종료조건 (재귀시에는, 중간 pivot구하고 앞으로 바꿔주는 작업이 필요 없으니까)
        if A[S] > A[E]: #결국 두개만 비교해서 정렬하면 되기 때문
            swap(S, E)
        return E

    M = (S + E) // 2
    swap(S, M)
    pivot = A[S]
    i = S + 1
    j = E
    while i <= j:
        while j >= S and pivot < A[j]:
            j = j - 1 # 의미: pivot의 위치는 현재 j보다 왼쪽에서 찾아야해요
        while  i <= E and pivot > A[i] :
            i = i + 1
        if i <= j: # 위치 바꾸는 조건이 일치하지 않을때는, swap후 인덱스 변경
            swap(i, j)
            i = i + 1
            j = j - 1
    #엇갈리는 시점 i>j에서 j: 작은 값들의 끝, i는 큰 값들의 시작 --> j의 위치와 pivot값을 바꿔줘   
    # i == j 피벗의 값을 양쪽으로 분리한 가운데에 오도록 설정하기
    A[S] = A[j]
    A[j] = pivot
    return j #j는 pivot의 최종 인덱스


quickSort(0, N - 1, K - 1)
print(A[K - 1])

