class Node: #노드 정의
	def __init__(self, data, next=None): # 두 개의 입력(노드의 값, 다음 노드의 주소)
		self.data = data				 
		self.next = next

class SimplyLinkedList:
	def __init__(self):
		self.head = None

	def link(self, prev, next):
		prev.next = next

	def append(self, data):
		currentNode = self.head
		while currentNode.next:
			currentNode = currentNode.next
		currentNode.next = Node(data)
	def printList(self):
		currentNode = self.head
		while currentNode.next:
			print(currentNode.data)
			currentNode = currentNode.next
		print(currentNode.data)

List1 = SimplyLinkedList()
Node1 = Node(1)
Node2 = Node(8)
List1.head = Node1
List1.append(3)
print(List1.printList())