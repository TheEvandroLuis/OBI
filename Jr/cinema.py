def valor (n):
  if n<=17:
    return 15
  elif n<=59:
    return 30
  else:
    return 20

amiga1= int(input())
amiga2= int(input())
soma = valor(amiga1) + valor(amiga2)
print(soma)