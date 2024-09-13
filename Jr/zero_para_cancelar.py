n = int(input())
numeros = []

for _ in range(n):
  entrada = int(input())
  if(entrada==0 and len(numeros)>0):
    numeros.pop()
  else:
    numeros.append(entrada)

soma = 0

for numero in numeros:
  soma+=numero

print(soma)