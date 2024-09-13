j, p, v, e, d = map(int, input().split())

if j ==-1:
  #SE ALGUMA DAS CONDIÇÕES FOR VERDADEIRA ENTÃO P NÃO É -1 
  #ENTÃO POSSO USAR O P
  if v ==-1:
    v = (p-e)//3
  elif e ==-1:
    e = p-(3*v)
  elif d ==-1:
    d = j-v-e
  j = v+e+d
    
if p ==-1:
  #SE ALGUMA DAS CONDIÇÕES FOR VERDADEIRA ENTÃO J NÃO É -1 
  #ENTÃO POSSO USAR O J
  if v ==-1:
    v = j-e-d
  elif e ==-1:
    e = j-v-d
  elif d ==-1:
    d = j-v-e
  p = (3*v)+e
    
print(j, p, v, e, d)