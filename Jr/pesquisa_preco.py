n = int(input())
estados = []

for _ in range(n):
  entrada = input().split()
  if float(entrada[1]) <=  float(entrada[2]) * 0.7:
    estados.append(entrada[0])

if(len(estados) == 0):
  print("*")
else:
  for estado in estados:
    print(estado)