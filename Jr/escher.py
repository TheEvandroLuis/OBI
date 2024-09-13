n = int(input())
sequecia = list(map(int, input().split()))
n_escher = sequecia[0]+sequecia[-1]

for i in range(1,n):
  soma = sequecia[i]+sequecia[-i-1]
  if soma != n_escher:
    n_escher = -1
    break

if n_escher == -1:
  print("N")
else:
  print("S")