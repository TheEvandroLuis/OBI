n, t = map(int, input().split()) #### NÃO USEI O TERMO T PQ USEI A MESMA LÓGICA DO FEIRINHA
tipos = list(map(int, input().split()))
precos = list(map(int, input().split()))
c = int(input())
clientes = list(map(int, input().split()))
estoque = []
total = 0

for i in range(n):
    estoque.append((precos[i], tipos[i]))
estoque.sort()

for cliente in clientes:
    if cliente == 0 and len(estoque)>0:
        venda=estoque.pop(0)
        total+=venda[0]
        #print(f"Indeciso - {venda}")
    else:
        for i in range(len(estoque)):
            if estoque[i][1]==cliente:
                venda=estoque.pop(i)
                #print(f"Decidido - {venda}")
                total+=venda[0]
                break
    
print(total)