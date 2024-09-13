numeroVitoria = 0

for i in range(6):
  leitura = input()
  if (leitura == "V"):
    numeroVitoria += 1

if (numeroVitoria >= 5):
  print(1)
elif (numeroVitoria >=3):
  print(2)
elif (numeroVitoria>=1):
  print(3)
else:
  print(-1)