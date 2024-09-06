n = int(input())
if n>5: 
    esquerda = 5
    direita = n-5
else:
    esquerda = n
    direita = -1

if esquerda<=0:
    print("*")
else:
    print("I"*esquerda)

if direita<0:
    print("*")
else:
    print("I"*direita)