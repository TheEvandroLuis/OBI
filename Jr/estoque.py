m, n = map(int, input().split())
estoque=[]

for _ in range(m):
  linha = list(map(int, input().split()))
  estoque.append(linha)

p = int(input())
totalVendas = 0

for _ in range(p):
  i, j = map(int, input().split())
  i = i - 1
  j = j - 1
  if estoque[i][j] > 0:
    estoque[i][j] -=1
    totalVendas +=1

print(totalVendas)