import sys
move = []
def hanoi(start, target, tmp, height):
    if height == 1:
            move.append([start, target])
            return
    hanoi(start, tmp, target, height-1)
    move.append([start, target])
    hanoi(tmp, target, start, height-1)

n = int(sys.stdin.readline().rstrip())

hanoi(1, 3, 2, n)

print(len(move))
for i in range(len(move)):
    print(move[i][0], move[i][1])