inicio = int(input())
fim = int(input())

quant=0  
for e in range(inicio, fim+1): 
  if e>1: 
    for f in range(2,e): 
        if(e % f==0): 
            break
    else: 
        quant+=1
        print(e) 
        
print(f'primos: {quant}')
