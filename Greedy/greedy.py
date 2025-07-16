import sys
input = sys.stdin.readline
#print = sys.stdout.write
n,k = map(int, input().split())
coin = []

for c in range(n):
    coin.append(int(input().strip()))
print(coin)
count = 0
for c in reversed(coin):
    if k == 0:
        break
    if c <= k:
        count += (k // c)
        k = k % c

print(str(count))

