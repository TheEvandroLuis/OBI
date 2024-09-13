horizontal = input()
vertical = input()
cruzamentos = []

for i in range(len(horizontal)):
  for j in range(len(vertical)):
    if horizontal[i] == vertical[j]:
      cruzamentos.append([i+1, j+1])

if(len(cruzamentos) == 0):
  print(-1, -1)
else:
  ultimo = cruzamentos[-1]
  print(ultimo[0], ultimo[1])