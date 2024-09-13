n = int(input())
lampadas = []
trechos = []
totalT=[]
tamanhoT =0
for _ in range(n):
  lampadas.append(int(input()))

for i in range(n):
  if (i+1<n):
    trechos.append(lampadas[i]+lampadas[i+1])
  else:
    trechos.append(lampadas[i]+lampadas[0])

for trecho in trechos:
  if(trecho<1000):
    tamanhoT+=1
  else:
    totalT.append(tamanhoT)
    tamanhoT=0
    
totalT.append(tamanhoT)
print(max(totalT))