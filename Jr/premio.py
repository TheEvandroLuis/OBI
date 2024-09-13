p = int(input())
d = int(input())
b = int(input())

pontos_totais = p * 1 + d * 2 + b * 3

if pontos_totais >= 150:
    premio = 'B'
elif pontos_totais >= 120:
    premio = 'D'
elif pontos_totais >= 100:
    premio = 'P'
else:
    premio = 'N'

print(premio)