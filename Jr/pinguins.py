escala_A, escala_B = input().split()
temp_A, temp_B = map(int, input().split())

if escala_A == "F":
    temp_A = (temp_A-32) * (5/9)
elif escala_B == "F":
    temp_B = (temp_B-32) * (5/9)

if temp_A<temp_B:
    print("A")
else:
    print("B")