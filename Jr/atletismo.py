n = int(input())
ranking = [0 for _ in range(n+1)]
for i in range(1, n+1):
  competidor = int(input())
  ranking[competidor] = i
for i in range(1, n+1):
  print(ranking[i])