# 1: 49분 시작
import sys
sys.setrecursionlimit(10000)
def preorder(v): #루트-왼-오
    if ((len(tree)-1) // 2) < v < len(tree):
        if tree[v] != '.' and tree[v] != '':
            print(str(tree[v]))
        return
        
    print(str(tree[v]))    
    if tree[v*2] != '.' and tree[v*2] != '':
        preorder(v*2)
    if tree[v*2+1] != '.' and tree[v*2+1] != '':
        preorder(v*2+1) 

def inorder(v):#왼-루트-오
    if ((len(tree)-1) // 2) < v < len(tree):
        if tree[v] != '.' and tree[v] != '':
            print(str(tree[v]))
        return
                
    if tree[v*2] != '.' and tree[v*2] != '':
        inorder(v*2)
    
    print(str(tree[v]))

    if tree[v*2+1] != '.' and tree[v*2+1] != '':
        inorder(v*2+1)

def postorder(v):#왼-오-루트
    if ((len(tree)-1) // 2) < v < len(tree):
        if tree[v] != '.' and tree[v] != '':
            print(str(tree[v]))
        return
                
    if tree[v*2] != '.' and tree[v*2] != '':
        postorder(v*2)
    
    if tree[v*2+1] != '.' and tree[v*2+1] != '':
        postorder(v*2+1)
    print(str(tree[v]))
    

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
tree = ['']* ((n+1)*2) # 1-n+1번째까지의 노드들이 각각 2개의 자식을 가짐
tree[1] = 'A'
for _ in range(n):
    subT = input().split()
    idx = tree.index(subT[0])
    if ((len(tree)-1) // 2) < idx < len(tree): # 마지막 레벨일 경우에는 걍 pass / 또는 아예 마지막레벨 전 레벨까지만 채워주는 전략도 괜찮음
            continue
        
    tree[idx*2] = subT[1]
    tree[idx*2+1] = subT[2]


preorder(1)
print('\n')
inorder(1)
print('\n')
postorder(1)
print('\n')
# 답안

import sys
input = sys.stdin.readline
N = int(input())
tree = {}  # 딕셔너리 형태로 선언
for _ in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]

def preOrder(now):
    if now == '.':
        return
    print(now, end='')  # 1.현재 노드
    preOrder(tree[now][0])  # 2.왼쪽 탐색
    preOrder(tree[now][1])  # 3.오른쪽 탐색

def inOrder(now):
    if now == '.':
        return
    inOrder(tree[now][0])  # 1.왼쪽 탐색
    print(now, end='')  # 2.현재 노드
    inOrder(tree[now][1])  # 3.오른쪽 탐색

def postOrder(now):
    if now == '.':
        return
    postOrder(tree[now][0])  # 1.왼쪽 탐색
    postOrder(tree[now][1])  # 2.오른쪽 탐색
    print(now, end='')  # 3.현재 노드

preOrder('A')
print()
inOrder('A')
print()
postOrder('A')
