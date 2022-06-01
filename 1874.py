n = int(input())
cnt = 1
stack = []
arr = []
tmp = 1
for i in range(n):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        arr.append("+")
        cnt += 1
    
    if num == cnt:
        stack.pop()
        arr.append("-")
        
    else :
        tmp == 0
        break
        
if tmp == 0:
    print("No")
    
for i in arr:
    print(i)
