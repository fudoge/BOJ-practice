class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        
class Tree():
    def __init__(self):
        self.root = None
        
    def _search(self, key):
        currentNode = self.root
        while currentNode:
            if currentNode.key == key:
                return True
            elif currentNode.key > key:
                if currentNode.left:
                    currentNode = currentNode.left
                else:
                    return False
            else:
                if currentNode.right:
                    currentNode = currentNode.right
                else:
                    return False
                
    def _insert(self, key):
        currentNode = self.root
        while currentNode:
            if currentNode.key == key:
                print("data ", key, " is already exist!")
                return False
            elif currentNode.key > key:
                if currentNode.left:
                    currentNode = currentNode.left
                else:
                    currentNode.left = Node(key)
                    return
            else:
                if currentNode.right:
                    currentNode = currentNode.right
                else:
                    currentNode.right = Node(key)
                    return
                    
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
                print("민노드는, 패런트 ", minNode.key,",", parentOfmin.key)
            print("민노드는, 패런트 ", minNode.key,",", parentOfmin.key)
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

BST.inorder_traversal(BST.root)
print()

BST._delete(11)

BST.inorder_traversal(BST.root)

print("이 트리의 루트는: ",BST.root.key)
print(BST.root.left.key)
print(BST.root.right.key)