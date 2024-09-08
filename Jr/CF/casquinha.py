n = int(input())
s = int(input())
sabores = []
n_bolas = 0

for _ in range(n):
    sabores.append(int(input()))

for i in range(n):
    casquinha = []
    #FICO UM POUCO NA DUVIDA SE A FILA PODE DAR A "VOLTA",
    #NO CASO DE CHEGAR AO FINAL VOCE PUDER VOLTAR PARA O COMEÇO DA FILA E CONTINUAR ESCOLHENDO SABORES
    #FIZ O EXERCICIO SEM ESSA POSSIBILIDADE
    for j in range(i, n):
        if sabores[j] not in casquinha:
            casquinha.append(sabores[j])
    if n_bolas<len(casquinha):
        n_bolas = len(casquinha)
    
print(n_bolas)