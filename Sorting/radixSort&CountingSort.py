#10,000,000* 10,000 ,천만 + 만 --> counting sort
# 내 answer
import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input().strip())
A = [0]
B = [0]*(10000+1)
C = [0]*(n+1)
for i in range(1,n+1):
    num = int(input().strip())
    A.append(num)

for i in range(1,n+1):
    idx = A[i]
    B[idx] += 1


hap = 0
for i in range(1,len(B)):
    hap += B[i]
    B[i] = hap


for i in range(1,n+1):
    val = A[i]
    C[B[val]] = val
    B[val] -= 1

for i in range(1, n+1):
    print(str(C[i])+'\n')


# gpt
import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input().strip())
A = [0]
B = [0] * (10000 + 1)
C = [0] * (n + 1)

# 입력
for i in range(1, n + 1):
    num = int(input().strip())
    A.append(num)

# 등장 횟수 세기
for i in range(1, n + 1):
    idx = A[i]
    B[idx] += 1

# 누적합 만들기
for i in range(1, len(B)):
    B[i] += B[i - 1]

# 정렬 (Stable을 위해 역순 순회)
for i in range(n, 0, -1):
    val = A[i]
    C[B[val]] = val
    B[val] -= 1

# 결과 출력 (C[1] ~ C[n])
for i in range(1, n + 1):
    print(str(C[i]) + '\n')

# 책
import sys
input = sys.stdin.readline
N = int(input())
count = [0] * 10001
for i in range(N):
    count[int(input())] += 1
for i in range(10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)


