# 노드 객체 생성
class Node:
    def __init__(self, value, left_node, right_node):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node
        
def pre_order(node):
    # 루트
    print(node.value, end='')
    # 왼쪽 자식
    if node.left_node != '.':
        pre_order(tree[node.left_node])
    # 오른쪽 자식
    if node.right_node != '.':
        pre_order(tree[node.right_node])

def in_order(node):
    # 왼쪽 자식
    if node.left_node != '.':
        in_order(tree[node.left_node])
    # 루트 
    print(node.value, end='')
    # 오른쪽 자식 
    if node.right_node != '.':
        in_order(tree[node.right_node])

def post_order(node):
    # 왼쪽 자식 
    if node.left_node != '.':
        post_order(tree[node.left_node])
    # 오른쪽 자식 
    if node.right_node != '.':
        post_order(tree[node.right_node])
    # 루트s
    print(node.value, end='')

# 입력값 받기    
n = int(input())
# 트리 생성 
tree = {}
for _ in range(n):
    value, left_node, right_node = input().split(' ')
    tree[value] = Node(value, left_node, right_node)
    
pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])