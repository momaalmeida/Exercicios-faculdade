divida = int(input())
valor_mensal = int(input())
parcela=1
while divida > 0:
    print("pagamento: {}".format(parcela))
    print("antes = {}".format(divida))
    parcela=parcela+1
    if divida <= valor_mensal:
        divida = 0      
    else:
        divida = divida - valor_mensal
    print("depois = {}".format(divida))   
    print("-----")
