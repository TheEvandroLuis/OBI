n = int(input())
estragados = 0

for _ in range(n):
    a, b = map(int, input().split())
    if (a==0) and (b==1):
        estragados+=1

print(n-estragados)