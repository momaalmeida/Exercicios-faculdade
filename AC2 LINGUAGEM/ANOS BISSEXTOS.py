def ano_bissexto(inicio):
    return inicio % 4 == 0 and inicio % 100 != 0 or inicio % 400 == 0

inicio = int(input())
fim = int(input())
biss = 0
while inicio < fim + 1:
    if ano_bissexto(inicio):
        print(inicio)
        biss += 1
    inicio += 1
print(f'bissextos: {biss}')
