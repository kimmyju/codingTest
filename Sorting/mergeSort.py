#1,000,000 x 20= 20,000,000 --> 1초 --> nlog 알고리즘
# 9:55분 종료, 9: 59분
#파이썬은 재귀호출의 깊이 최대가 1000
import sys
def mergeSort(s, e):
    #파이썬에서는 while문 안에 처음 선언한 변수가 그 블록을 나가거나 다른 함수에 갔다 오면 사라지는지 아닌지 알아보기: 블록을 나가거나 다른 함수 에 다녀오는건 상관x, 함수 자체가 끝나면 변수가 사라짐
    m = (s+e) // 2
    if e - s < 1:
        return
    
    #계속해서 분할
    mergeSort(s, m)
    mergeSort(m+1, e)

    #임시로 정렬할 배열 할당, 인덱스 할당
    # 1) 정렬되지 않은 배열을 인덱스를 맞춰서 임시로 저장
    for i in range(s,e+1):
        temp[i] = arr[i]

    # 2) 인덱스를 할당
    idx1 = s
    k = s
    idx2 = m+1

    while idx1 <= m and idx2 <= e: # s-m, m+1-e인 이유: m또는 e까지의 배열 요소를 모두 처리해야 하기 때문 (한쪽 중 하나라도 모두 다 넣어야 하니까)
        if temp[idx1] < temp[idx2]: #k는 arr배열에 넣을 요소를 차례대로 찾는 것. idx들은 temp배열의 값들을 탐색하기 위함
            arr[k] = temp[idx1]
            idx1+=1
            k+=1

        else:
            arr[k] = temp[idx2]
            idx2+=1
            k+=1

    # 먼저 한쪽 그룹을 다 넣은 후 나머지 요소 처리 (아직 하나가 작거나 같다는건 나머지 처리할 요소가 있다는 것)
    while idx1 <= m:
        arr[k] = temp[idx1]
        idx1+=1
        k+=1

    while idx2 <= e:
        arr[k] = temp[idx2]
        idx2+=1
        k+=1

 
input = sys.stdin.readline
print = sys.stdout.write

n = int(input().strip())
arr = [0]* n
temp = [0]* n

for i in range(n):
    num = int(input().strip())
    arr[i] = num

mergeSort(0, len(arr)-1) # arr은 함수밖에서 쓰이는건데 함수의 매개변수로 보냈을때 사용 가능한지 --> arr[0] = 99식으로 값을 할당하면 원본 영향 but arr = [1,2,3] 이런식으로 하면 원본 영향x

for num in arr:
    print(str(num) + '\n')

#정답코드
# import sys
# input = sys.stdin.readline
# print = sys.stdout.write

# def merge_sort(s, e):
#     if e - s < 1: return
#     m = int(s + (e - s) / 2)
#     merge_sort(s, m)
#     merge_sort(m + 1, e)
#     for i in range(s, e + 1):
#         tmp[i] = A[i]
#     k = s
#     index1 = s
#     index2 = m + 1
#     while index1 <= m and index2 <= e:
#         if tmp[index1] > tmp[index2]:
#             A[k] = tmp[index2]
#             k += 1
#             index2 += 1
#         else:
#             A[k] = tmp[index1]
#             k += 1
#             index1 += 1
#     while index1 <= m:
#         A[k] = tmp[index1]
#         k += 1
#         index1 += 1
#     while index2 <= e:
#         A[k] = tmp[index2]
#         k += 1
#         index2 += 1

# N = int(input())
# A = [0] * int(N + 1)
# tmp = [0] * int(N + 1)
# for i in range(1, N + 1):
#     A[i] = int(input())
# merge_sort(1, N)
# for i in range(1, N + 1):
#     print(str(A[i]) + '\n')