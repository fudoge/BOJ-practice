class Node():	#노드 선언
	def __init__(self, data, next = None):
		self.data = data
		self.next = next
        
class SimplyLinkedList():
	def __init__(self):
		self.head = None
    
	def link(self, node, next): #노드 연결
		node.next = next
        
	def getTail(self): #꼬리 노드 불러오기
		currentNode = self.head
		while currentNode.next:
			currentNode = currentNode.next
		return currentNode
    
	def getIndex(self, data): #data의 인덱스 반환
		currentNode = self.head
		index = 0
		while currentNode.data != data:
			currentNode = currentNode.next
			index += 1
		return index
    
	def getNum(self, index):	#index의 값 반환
		currentNode = self.head
		for i in range(index):
			prevNode = currentNode
			currentNode = currentNode.next
		return currentNode.data
    
	def append(self, data): #tail에 추가, 빈 리스트일경우, head에.
		if self.head == None:
			self.head = Node(data)    
		else:
			tail = self.getTail()
			tail.next = Node(data)
        
	def appendhead(self, data): #head에 추가
		self.head = Node(data, self.head)
        
	def insertAt(self, data, index):	#이 인덱스에 삽입
		currentNode = self.head
		for i in range(index):
			prevNode = currentNode
			currentNode = currentNode.next
		prevNode.next = Node(data)
		self.link(prevNode.next, currentNode)
        
	def insertBeforeThisNumber(self, data, target_num): #이 번호 앞에 삽입
		currentNode = self.head
		while currentNode.data != target_num:
			prevNode = currentNode
			currentNode = currentNode.next
		prevNode.next = Node(data)
		self.link(prevNode.next, currentNode)
        
	def insertAfterThisNumber(self, data, target_num): #이 번호 뒤에 삽입
		currentNode = self.head
		while currentNode.data != target_num:
			prevNode = currentNode
			currentNode = currentNode.next
		prevNode = currentNode
		currentNode = currentNode.next
		prevNode.next = Node(data)
		self.link(prevNode.next, currentNode)
        
	def pop(self):	#맨 끝 삭제
		currentNode = self.head
		while currentNode.next:
			prevNode = currentNode
			currentNode = currentNode.next
		prevNode.next = None
        
	def pophead(self):	#맨 앞 삭제
		headNode = self.head
		self.head = self.head.next
		headNode.next = None
        
	def popAt(self, index):	#특정 인덱스 pop
		currentNode = self.head
		for i in range(index):
			prevNode = currentNode
			currentNode = currentNode.next
		if currentNode.next:
			self.link(prevNode, currentNode.next)
			currentNode = None
            
	def popIt(self, data):	#특정 값 pop
		currentNode = self.head
		while currentNode.data != data:
			prevNode = currentNode
			currentNode = currentNode.next
		prevNode = currentNode
		currentNode = currentNode.next
		if currentNode.data == data:
			self.link(prevNode, currentNode.next)
    
	def printList(self):	#프린트
		currentNode = self.head
		while currentNode.next:
			print(currentNode.data)
			currentNode = currentNode.next
		print(currentNode.data)
        
	def listMerge(self, nextList):	#리스트 병합
		tail = self.getTail()
		self.link(tail, nextList.head)
        
node1 = Node(7)	#7을 가진 노드 생성
node2 = Node(3) #3을 가진 노드 생성

List1 = SimplyLinkedList() #리스트1 생성
List2 = SimplyLinkedList() #리스트2 생성

List1.head = node1   	    #리스트1의 head를 node1로 설정
List1.link(node1, node2)	#node1의 다음 노드를 node2로 지정
List2.append(4)				#리스트2에 4를 가진 노드 추가
List1.appendhead(780)		#리스트1의 head를 780을 가진 노드로 설정
List2.insertAfterThisNumber(60, 4) #리스트2의 4 뒤에 60 삽입
List1.insertAt(68, 1) #List1의 1인덱스자리에 68을 가진 노드 넣기(기존 값들은 밀려남)
List2.append(200)	  #리스트2의 맨 끝에 200을 가진 노드 추가
List2.popAt(1)		  #리스트2의 1인덱스자리의 노드(60을 가진 노드) 제거
List1.listMerge(List2)#리스트1 - 리스트2 합치기(연결)

List1.printList()	  #리스트1 출력