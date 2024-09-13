n = int(input())
sequencia = []

sequencia.append(int(input()))

for _ in range(n-1):
  entrada = int(input())
  if(entrada!=sequencia[-1]):
    sequencia.append(entrada)

print(len(sequencia))