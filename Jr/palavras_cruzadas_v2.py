def encontra_cruzamento(horizontal, vertical):
  for i in range(len(horizontal)-1, -1, -1):
    for j in range(len(vertical)-1, -1, -1):
      if horizontal[i] == vertical[j]:
        print(i+1, j+1)
        return  # Sai da função
  print(-1 , -1)

horizontal = input()
vertical = input()
encontra_cruzamento(horizontal, vertical)