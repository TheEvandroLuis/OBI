d = int(input())
andar = d % 400
if andar>200:
  andar = 400 - andar
print(andar)