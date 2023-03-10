#https://docs.python.org/pt-br/3/library/stdtypes.html
#https://pythonacademy.com.br/blog/tipos-de-variaveis-no-python

print("Vamos saber os tipos da entra de dados:")
a = input("Digite algo? ")
print("Qual o tipo primitivo? ", type(a))
print("Só tem espaços? ", a.isspace())
print("É um número? ", a.isnumeric())
print("É alfabético? ", a.isalpha())
print("É alfanumérico? ", a.isalnum())
print("Estão em maiúsculas? ", a.isupper())
print("Estão em minúsculas? ", a.islower())
print("Está capitalizada? ", a.istitle())
