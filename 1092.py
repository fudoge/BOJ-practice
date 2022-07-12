import sys

n = int(sys.stdin.readline().rstrip())
crane = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
box = list(map(int, sys.stdin.readline().rstrip().split()))
cnt = 0

crane.sort(reverse = True)
box.sort(reverse = True)

if crane[0] < box[0]:
    print(-1)
    exit(0)

print(box)
    
while box:
    box.pop(0)
    print(box)
    for i in range(1, n):
        if box == []:
            break
        if crane[i] >= box[0]:
            box.pop(0)
            print(box)
        else:
            for j in range(1, len(box)):
                if crane[i] >= box[j]:
                    box.pop(j)
                    print(box)
                    break
    cnt += 1
    
print(cnt)