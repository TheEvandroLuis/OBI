t = int(input())
posicao = [0,0]
direcao = 0 #vou usar os valores 0, 1, 2 e 3 para apontar a cada direcao 0:N 1:L 2:S 3:O
for _ in range(t):
    k = input()
    valor = int(input())

    if k=="G":
        valor = valor//90 #vamos descobrir quantas vezes precisamos virar
        direcao = (direcao+valor)%4 #para evitar que passe de 3 e volte para 0

    if k=="M":
        if direcao==0:
            posicao[1]+=valor
        elif direcao==1:
            posicao[0]+=valor
        elif direcao==2:
            posicao[1]-=valor
        elif direcao==3:
            posicao[0]-=valor

print(posicao[0], end =" ")
print(posicao[1])