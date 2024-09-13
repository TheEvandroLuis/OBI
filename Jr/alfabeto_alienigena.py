k, n = map(int, input().split())
alfabeto = input()
mensagem = input()
m_alien = True

for letra in mensagem:
 if letra not in alfabeto:
   m_alien = False
   break
   
if m_alien:
  print("S")
else:
  print("N")