import sys

stack = []
n = int(sys.stdin.readline())

for i in range(n):
    tmp = sys.stdin.readline()
    if tmp[0] == "p" and tmp[1] == "u":
        stack.append(int(tmp[5:]))
    elif tmp[0] == "p" and tmp[1] == "o":
        if stack == []:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    elif tmp[0] == "s":
        print(len(stack))
    elif tmp[0] == "e":
        if stack == []:
            print(1)
        else:
            print(0)
    elif tmp[0] == "t":
        if stack == []:
            print(-1)
        else:
            print(stack[-1])