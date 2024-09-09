v = int(input())
p = int(input())
parcelas = [v//p for _ in range(p)]
if v%p>0:
    for i in range(v%p):
        parcelas[i]+=1
print(parcelas)