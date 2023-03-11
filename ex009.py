#calculo de taboada
#https://blog.betrybe.com/python/python-for/


print("Tabuada")
numero = int(input("Ecolha o valor para tabuada?"))

i=1 
for i in range(11):
    print(" Numero {} x {} = {}" .format(numero, i,(numero * i) ))
