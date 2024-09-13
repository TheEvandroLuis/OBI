a = int(input())
b = int(input())
c = int(input())

if (a<b and b<c or a+b<c):
  print(1)
elif(a<b or b<c):
  print(2)
else:
  print(3)