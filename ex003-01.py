#https://www.onlinegdb.com/online_c_compiler

acumulador = 0
ciclos = 4 #numero de inputs digitado pelo usuário
 
 
for i in range(ciclos):
  print("Digite o valor: ")
  numeros = float(input())
  acumulador += numeros # o mesmo que dizer: acumulador = (acumulador + numeros)
 
media = (acumulador/ciclos)
print("Média dos valores informados: ", media)
