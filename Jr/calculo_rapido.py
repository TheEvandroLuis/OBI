s = int(input())
a = int(input())
b = int(input())
qtdNumeros = 0

for i in range(a,b+1):
  numero = i
  somaDigitos = 0
  while (numero>=10):
    somaDigitos += numero % 10
    numero = numero // 10
  somaDigitos += numero
  if(somaDigitos==s):
    qtdNumeros += 1

print(qtdNumeros)