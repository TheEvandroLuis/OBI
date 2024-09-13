notas = []
trofeus, placas = 0, 0

for _ in range(5):
  notas.append(int(input()))
notas.sort(reverse = True)

for nota in notas:
  if nota == notas[0]:
    trofeus += 1
  else:
    break

for _ in range(trofeus):
  notas.pop(0)

for nota in notas:
  if nota == notas[0]:
    placas += 1
  else:
    break
    
print(trofeus, placas)