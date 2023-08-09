contador = 0
soma = 0
listatempo = []
while True:
    tempo = int(input())
    if tempo > 0:
        soma = soma + tempo
        contador = contador + 1
        listatempo.append(tempo)
    else:
        media = soma / contador
        print (f'MEDIA: {media:.2f}')
        for t in listatempo:
            if t < media:
                print (t)
        break
       



   
