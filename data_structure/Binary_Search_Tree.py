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
            
    
    
    def _delete_beta(self, key):
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
                
    def _delete(self, key):    #삭제
        node = self.root       #루트부터 시작
        parent = None          #없앨 부모 노드를 담을 변수 생성
        while True:            #무한 루프
            if node == None:   #노드가 없으면 중지
                return False
            if node.key == key:#노드의 key값이 일치하면, 루프 탈출
                break
            else:              #같지 않으면..
                parent = node 
                if key < node.key:#찾으려는 값이 현 노드보다 작으면, 왼쪽으로 이동해서 반복
                    node = node.left
                else:            #크면, 오른쪽으로 이동해서 반복
                    node = node.right
                    
        if node.left != None and node.right != None:#서브트리가 두 개일 경우, 자리를 대신할 노드로 오른쪽 서브트리의 가장 작은 자손을 올린다.
            print("서브트리가 두 개!")
            minNode = node.right            #오른쪽 서브트리의 루트부터 시작
            parentOfmin = node              #대신할 노드의 부모노드 선언
            isright = True    #바로 오른쪽 서브트리의 루트가 대신하는지(while 문을 건너뛰는지)
            while minNode.left != None:     #단말 노드까지 왼쪽으로만 내려가기
                parentOfmin = minNode
                minNode = minNode.left
                isright = False
            node.key = minNode.key          #찾은 노드(오른쪽 서브트리의 가장 작은 자손)가 자리를 대신함
            if isright is True:             #오른쪽 서브트리의 루트가 대신한다면:
                parentOfmin.right = None
            else:                           #만약 더 내려간다면:
                parentOfmin.left = None
            
        elif node.left != None:            #서브트리가 왼쪽에만 있다면
            print("서브트리가 한 개!")
            if node.key > parent.key:      #삭제하려는 노드가 부모 노드보다 크면, 부모의 오른쪽을 왼쪽 서브트리의 루트로 연결
                parent.right = node.left
            else:
                parent.left = node.left    #삭제하려는 노드가 부모 노드보다 작으면, 부모의 왼쪽을 왼쪽 서브트리의 루트로 연결
        elif node.right != None:           #서브트리가 오른쪽에 있다면
            print("서브트리가 한 개!")
            if node.key > parent.key:      #삭제하려는 노드가 부모 노드보다 크면, 부모의 오른쪽을 오른쪽 서브트리의 루트로 연결
                parent.right = node.right
            else:
                parent.left = node.right   #삭제하려는 노드가 부모 노드보다 작으면, 부모의 왼쪽을 오른쪽 서브트리의 루트로 연결
        else:        
            print("서브트리 없음!")           #서브트리가 없을 때
            if parent.key > key:           #부모노드가 더 크면, 왼쪽을 없애고, 작으면 오른쪽을 없앰
                parent.left = None
            else:
                parent.right = None
            
    def inorder_traversal(self, node):    #중위 순회
        if node.left:
            self.inorder_traversal(node.left)
        print(node.key, end=" ")
        if node.right:
            self.inorder_traversal(node.right)

BST = Tree()
BST._insert(10)
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

BST._delete(5)

BST.inorder_traversal(BST.root)

print("이 트리의 루트는: ",BST.root.key)
print("루트의 왼쪽 서브 트리의 루트는: ", BST.root.left.key)
print("루트의 오른쪽 서브 트리의 루트는: ", BST.root.right.key)