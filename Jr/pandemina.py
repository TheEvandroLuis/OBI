n, m = map(int, input().split())
infectados= [0] * (n+1)

i, r = map(int, input().split())
infectados[i]=1

for _ in range(r-1):
  input()

for _ in range(r, m+1):
  amigos = list(map(int, input().split()))
  reuniaoInfectada = False
  for j in range(1, amigos[0]+1):
    if infectados[amigos[j]]==1:
      reuniaoInfectada = True
      break
  if reuniaoInfectada:
    for j in range(1, amigos[0]+1):
      infectados[amigos[j]]=1

print(sum(infectados))