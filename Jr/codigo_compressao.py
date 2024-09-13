n = int(input())
string = input()
codigo = []
atual = string[0]
count = 1

for i in range(1, n):
  if atual == string[i]:
    count += 1
  else:
    codigo.append(str(count))
    codigo.append(atual)
    atual = string[i]
    count = 1

#ADICIONA O ULTIMO CARACTER NO CODIGO
codigo.append(str(count))
codigo.append(atual)

for c in codigo:
  print(c, end=" ")