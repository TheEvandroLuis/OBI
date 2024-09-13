alfabeto = "abcdefghijlmnopqrstuvxz"
especiais = " ,:"
contador = [0] * len(alfabeto)
pangrama = True
frase = input()

for c in frase:
  if (c not in especiais):
    contador[alfabeto.index(c)] +=1

for letra in contador:
  if(letra==0):
    pangrama= False

if (pangrama):
  print("S")
else:
  print("N")