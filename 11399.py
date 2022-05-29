n = int(input())
p = list(map(int, input().split(" ")))
answer = 0

p.sort()
for i in range(n):
    answer += p[i] * (n-i)

print(answer)