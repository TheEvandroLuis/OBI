n = int(input())
inicial = input()
copos = [0, 0, 0]

if inicial =="A":
  copos[0]=1
elif inicial =="B":
  copos[1]=1
else:
  copos[2]=1

for _ in range(n):
  movimento = int(input())
  if movimento == 1:
    copos[0], copos[1] = copos[1], copos[0]
  elif movimento ==2:
    copos[1], copos[2] = copos[2], copos[1]
  else:
    copos[0], copos[2] = copos[2], copos[0]

if copos[0]==1:
  print("A")
elif copos[1]==1:
  print("B")
else:
  print("C")