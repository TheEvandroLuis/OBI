def montaNumero (numero):
    n = "" 
    for i in range(1, len(numero)+1):
        if numero[-i] >= 0:
            n += str(numero[-i])
    if n == "":
        n="-1"
    return int(n)

a = int(input())
b = int(input())

numA = []
numB = []

while a>=10:
    numA.append(a%10)
    a = a // 10
numA.append(a)

while b>=10:
    numB.append(b%10)
    b = b // 10
numB.append(b)

if len(numA)>len(numB):
    for _ in range(len(numA)-len(numB)):
        numB.append(0)
elif len(numB)>len(numA):
    for _ in range(len(numB)-len(numA)):
        numA.append(0)

for i in range(len(numA)):
    if numA[i]>numB[i]:
        numB[i] = -1
    elif numB[i]>numA[i]:
        numA[i] = -1

resultado = [montaNumero(numA), montaNumero(numB)]
resultado.sort()

print(resultado[0], end=" ")
print(resultado[1])