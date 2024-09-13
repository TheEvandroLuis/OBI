n = int(input())
camisetas = input().split(" ")
Total_p= int(input())
Total_m= int(input())

p=0
m=0

for camiseta in camisetas:
  if (camiseta=="1"):
    p=p+1
  else:
    m=m+1

if(p<=Total_p and m<=Total_m):
  print("S")
else:
  print("N")