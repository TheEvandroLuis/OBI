alfabeto = "abcdefghijklmnopqrstuvwxyz"

letrasFrase1 = [0]*26
letrasFrase2 = [0]*26

n = int(input())
frase1 = input()
frase2 = input()

for letra in frase1:
  if (letra in alfabeto):
    letrasFrase1[alfabeto.index(letra)] +=1

for letra in frase2:
  if (letra in alfabeto):
    letrasFrase2[alfabeto.index(letra)] +=1

if letrasFrase1 == letrasFrase2:
  print("S")

else:
  print("N")