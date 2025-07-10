#내림차순은 max
# 20,000,000
# 000,000,000,0

import sys
input = sys.stdin.readline

n = input().strip()  # 개행 제거
su = list(map(int, n))  # 문자열의 각 글자를 int로 변환해 리스트로 만듦
print(su)

for i in range(len(su)):
    max = i
    for j in range(i+1, len(su)):
        if su[max] < su[j]:
            max = j

    temp = su[i]
    su[i] = su[max]
    su[max] = temp

for s in su:
    print(s,end='')
