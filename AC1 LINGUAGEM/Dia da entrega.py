dias = ['domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado']
dia_sem = str(input())
diasentrega = int(input())

dia_entr = dias.index(dia_sem) + diasentrega

if dia_entr > 6:
    dia_entr = dia_entr - 7

entrega = dias[dia_entr]

if diasentrega == 0:
    print('chega hoje!')
else:
    print('sera entregue {}'.format (entrega))
