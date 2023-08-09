valor = float(input())
doado = 0
while valor != -1:
    doado += valor
    valor = float(input())
print(f'VC$ {doado:.2f}')
print(f'R$ {doado * 2.50:.2f}')
