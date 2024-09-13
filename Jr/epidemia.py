n = int(input())
r = int(input())
p = int(input())
totalPessoasInfectadas = n
pInfDia = n
i=0
while (totalPessoasInfectadas < p):
  i +=1
  pInfDia = pInfDia * r
  totalPessoasInfectadas += pInfDia

print (i)