def imprime(piramide):
  for i in range(len(piramide)):
    for j in range(len(piramide)):
      print(piramide[i][j], end=" ")
    print()  

n = int(input())
piramide = []
camadas = (n+1)//2
for _ in range(n):
  linha = [1] * n
  piramide.append(linha)

for camada in range(1, camadas+1):
  for i in range(camada, n-camada):
    for j in range(camada, n-camada):
        piramide[i][j]+=1

imprime(piramide)