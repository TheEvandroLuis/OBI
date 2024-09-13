a = int(input())
s = int(input())
d = int(input())
subindo = True
alturaAtual = 0
dias = 1

while (subindo):
  alturaAtual += s
  if (alturaAtual>=a):
    subindo = False
  else:
    alturaAtual -= d
    dias +=1

print(dias)