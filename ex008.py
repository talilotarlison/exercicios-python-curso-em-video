print("converter Moeda --> Tranforma R$ Real em $Dolar")
numero = float(input("Ecolha o valor em  R$ real que quer converter em $ dolar?"))

dolar = numero * 0.19

print("O valor R${:2f} em Real, corresponde a ${:2f} em dolar!" .format(numero,dolar))
