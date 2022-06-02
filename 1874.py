cnt = 0
stack = []
arr = []
tmp = True

n = int(input())
for _ in range(n):
    num = int(input())
    while cnt < num:
        cnt += 1
        stack.append(cnt)
        arr.append("+")
    
    if num == stack[-1]:
        stack.pop()
        arr.append("-")
    else :
        tmp = False
        print("NO")
        exit(0)
        
print(tmp)
        
if tmp == False:
    print("NO")
else:
    print("/n")
    for i in arr:
        print(i)
