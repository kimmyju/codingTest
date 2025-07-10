n = int(input())
su_List = []
for _ in range(n):
    su = int(input())
    su_List.append(su)

#print(su_List)

for i in range(len(su_List)-1, 0-1, -1):
    cnt = 0
    for j in range(i):
        if su_List[j+1] < su_List[j]:
            temp = su_List[j]
            su_List[j] = su_List[j+1]
            su_List[j+1] = temp

        else:
            cnt += 1

    
    if cnt == i:
       break

for num in su_List:
    print(num)