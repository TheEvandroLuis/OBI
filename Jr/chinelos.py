n = int(input())
chinelos = []
totalVendas=0

for _ in range (n):
  chinelos.append(int(input()))

p = int(input())

for _ in range(p):
  tamanho = int(input())
  if(chinelos[tamanho-1]>0):
    chinelos[tamanho-1] -=1
    totalVendas+= 1

print (totalVendas)