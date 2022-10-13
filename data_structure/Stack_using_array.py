class stack():		#스택 선언
    def __init__(self):
        self.arr = []
    def isEmpty(self):	#스택이 비어있는지 확인
        if len(self.arr) == 0:
            return True
        else:
            return False
        
    def push(self, data):	#스택에 데이터 맨 위에 추가
        self.arr.append(data)
    
    def pop(self):	#스택의 맨 위 값 삭제 및 반환
        if self.isEmpty():
            print("Stack is Empty")
        else:
            return(self.arr.pop())
        
    def top(self):	#스택의 맨 위 값 반환
        if self.isEmpty():
            print("Stack is Empty")
        else:
            return(self.arr[-1])
        
s = stack()
print(s.isEmpty())
s.push(5)
s.push(7)
s.push(2)
s.push(3)
s.push(9)
print(s.isEmpty())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.top())