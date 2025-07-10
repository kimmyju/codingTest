import sys

input = sys.stdin.readline
n = int(input().strip())
p = list(map(int, input().split()))
print(n, p)

# 정렬
for i in range(1,n):
    idx = -1
    for j in range(i-1, 0-1, -1):
        if p[i] < p[j]:
            idx = j
            continue
        else:
            break
    if idx != -1:
        temp = p[i]
        for j in range(i, idx, -1):
            p[j] = p[j-1]

        p[idx] = temp

        print(p, idx)

sum = []
hap = 0
total_t = 0
for i in range(n):
    hap += p[i]
    total_t += hap
    sum.append(hap)

print(total_t)




            

# 누적합

#출력