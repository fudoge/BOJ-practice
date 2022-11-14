class Node():    #노드 선언
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class Tree():    #트리 및 순회
    def __init__(self):
        self.root = None

    def preorder_traversal(self, node):    #전위 순회
        print(node.data, end=" ")
        if node.left:
            self.preorder_traversal(node.left)
        if node.right:
            self.preorder_traversal(node.right)

    def inorder_traversal(self, node):    #중위 순회
        if node.left:
            self.inorder_traversal(node.left)
        print(node.data, end=" ")
        if node.right:
            self.inorder_traversal(node.right)

    def postorder_traversal(self, node):    #후위 순회
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node.data, end=" ")
        
#트리 및 노드의 선언
T = Tree()
A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")
G = Node("G")

T.root = A
A.left = B
A.right = C
B.left = D
B.right = E
C.left = F
C.right = G

T.preorder_traversal(T.root)
print()
T.inorder_traversal(T.root)
print()
T.postorder_traversal(T.root)