def espalhaLava(mapa, linha, coluna, n, f):
  fila= [(linha, coluna)]
  while len(fila)>0:
      x, y = fila.pop(0)
      if mapa[x][y] == '*':
        continue
      if mapa[x][y] > f:
        continue
      mapa[x][y] = '*'
      if x > 0:
        fila.append((x-1, y))
      if x < n - 1:
        fila.append((x+1, y))
      if y > 0:
        fila.append((x, y-1))
      if y < n - 1:
        fila.append((x, y+1))

n, f = map(int, input().split())
mapa = []

for _ in range(n):
  entrada = input()
  linha=[]
  for i in entrada:
    linha.append(int(i))
  mapa.append(linha)

espalhaLava(mapa, 0, 0, n, f)

for linha in mapa:
  for coluna in linha:
    print(coluna, end='')
  print()