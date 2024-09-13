a, b = map(int, input().split())
c = []

#SENDO A MEDIA E MEDIANA IGUAL A
m = (2*a) - b
c.append(m)

#SENDO A MEDIA E MEDIANA IGUAL B
m = (2*b) - a
c.append(m)

#SENDO A MEDIA E MEDIANA IGUAL C
m = (a+b)//2
c.append(m)

c.sort()
print(c[0])