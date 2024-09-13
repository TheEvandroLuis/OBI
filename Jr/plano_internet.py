quota = int (input())
n_meses = int (input())
sobra = 0

for i in range(n_meses):
  sobra += quota - int(input())

print(quota+sobra)