d = int(input())
a = int(input())
n = int(input())
valorDiaria = d

if n>15:
  valorDiaria= d + (14*a)
else:
  valorDiaria= d + (n-1)*a

total = valorDiaria * (32-n)
print(total)