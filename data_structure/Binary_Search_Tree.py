class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        
class Tree():
    def __init__(self):
        self.root = None
        
    def _search(self, root, key):    #탐색        
        if root == None:             #만약 root값이 없으면: (찾지 못한 경우)
            return "Not Found!"
        if root.key == key:          #값을 찾으면:
            return root.key
        elif root.key > key:         #root가 더 크다면: (왼쪽으로 이동하는 재귀)
            return self._search(root.left, key)
        else:                        #root가 더 작다면: (오른쪽으로 이동하는 재귀)
            return self._search(root.right, key)
                
    def _insert(self, key):
        def _addNode(root, key):    #노드 추가 정의
            if key == root.key:     #루트와 같은 key라면, False반환
                return False
            elif key < root.key:    #루트보다 작은데..
                if root.left == None:#루트의 왼쪽이 비었다면? 바로 왼쪽에 삽입하면된다.
                    root.left = Node(key)
                    return True
                else:                #아니라면, 루트의 왼쪽 서브트리를 루트로 하고, 재귀적으로 실행시킨다.
                    _addNode(root.left, key)
            else:                    #루트보다 큰데..
                if root.right == None:#루트의 오른쪽이 비었다면? 바로 오른쪽에 삽입하면된다.
                    root.right = Node(key)
                    return True
                else:                #아니라면, 루트의 오른쪽 서브트리를 루트로 하고, 재귀적으로 실행한다.
                    _addNode(root.right, key)        
        if self.root == None:        #만약 루트가 없으면, 루트부터 만들어주자
            self.root = Node(key)
            return True
        else:                        #루트가 없으면? 정의해놓은 노드 추가를 이용하자.
            _addNode(self.root, key)
            
    
    
    def _delete(self, key):
        parentNode = None
        currentNode = self.root
        print("탐색 중: ", end="")
        while currentNode:
            print(currentNode.key, end =" ")
            if currentNode.key == key:
                break
            elif currentNode.key > key:
                parentNode = currentNode
                currentNode = currentNode.left
            else:
                parentNode = currentNode
                currentNode = currentNode.right
        print()
                
        if currentNode.left != None and currentNode.right != None:
            print("서브트리가 두 개이군!")
            minNode = currentNode.right
            parentOfmin = currentNode
            isright = True    #바로 옆의 것인지(while 문을 건너뛰는지)
            while minNode.left != None:
                parentOfmin = minNode
                minNode = minNode.left
                isright = False
            currentNode.key = minNode.key
            if isright is True:
                parentOfmin.right = None
            else:
                parentOfmin.left = None
            
                
        elif currentNode.left != None:
            print("서브트리가 한 개이군!")
            parentNode.right = currentNode.left
        elif currentNode.right != None:
            print("서브트리가 한 개이군!")
            parentNode.left = currentNode.right
        else:
            print("서브트리가 없군!")
            if parentNode.key > key:
                parentNode.left = None
            else:
                parentNode.right = None
                
    def _delete2(self, key):

        
            
    def inorder_traversal(self, node):    #중위 순회
        if node.left:
            self.inorder_traversal(node.left)
        print(node.key, end=" ")
        if node.right:
            self.inorder_traversal(node.right)

a = Node(10)
BST = Tree()
BST.root = a
BST._insert(12)
BST._insert(13)
BST._insert(11)
BST._insert(7)
BST._insert(9)
BST._insert(8)
BST._insert(5)

print(BST._search(BST.root, 5))

BST.inorder_traversal(BST.root)
print()

BST._delete2(10)

BST.inorder_traversal(BST.root)

print("이 트리의 루트는: ",BST.root.key)
print(BST.root.left.key)
print(BST.root.right.key)