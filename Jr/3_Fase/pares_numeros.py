n, inicio, fim = map(int, input().split())
vetor = list(map(int, input().split()))
qtd=0
for i in range(n):
    for j in range (i+1, n):
        soma = vetor[i]+vetor[j]
        if soma >= inicio and soma <= fim:
            qtd+=1
print(qtd)