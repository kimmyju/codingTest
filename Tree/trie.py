#7:05시작
import sys
input = sys.stdin.readline
print = sys.stdout.write
class Node(object):
    def __init__(self, isEnd):
        self.isEnd = isEnd
        self.childNode = {}
class Trie(object):
    def __init__(self):
        self.parent = Node(None)

    def insert(self,string):
        currentN = self.parent
        tempL = 0
        for char in string:
            if char not in currentN.childNode: # 딕셔너리 키 값도 이렇게 서칭 가능
                currentN.childNode[char] = Node(char)
            #자식 노드로 이동
            currentN = currentN.childNode[char] # 자식 객체로 바꿔줌
            tempL +=1 #하나 이동했으니까 temp +1
            
            if tempL == len(string): #문자의 마지막이라면 즉 리프라면 끝이라고 표시
                currentN.isEnd = True

    def search(self,string): # 있으면 True, 없으면 False 반환
        currentN = self.parent
        tempL = 0
        
        for char in string:
            if char in currentN.childNode: # char이 현재 노드에 있다면
                currentN = currentN.childNode[char] #현재 노드로 바꿔준다
                tempL += 1

                if tempL == len(string) and currentN.isEnd == True:
                    return True
                
            else: # 일치하는 문자가 없는 순간 stop
                return False
        return False # 문자는 다 만족했지만 isEnd == True 조건을 만족하지 않은 경우 예외 처리 ex)트라이에 gone이 있는데 gon을 검색할 경우


n,m = map(int, input().split())
trie = Trie()
for _ in range(n):
    string = input().strip()
    trie.insert(string)

count = 0
for _ in range(m):
    string = input().strip()
    # 있는지 없는지 비교
    if trie.search(string):
        count +=1
print(str(count)+'\n')

#2번째 방법
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
textList = set([input() for _ in range(n)])
print(textList)
count = 0

for _ in range(m):
    subText = input()
    if subText in textList:
        count+=1
print(count)

