#https://pt.stackoverflow.com/questions/173939/gostaria-de-de-saber-qual-%C3%A9-a-fun%C3%A7%C3%A3o-do-na-linguagem-python-e-mais-especific


#modelo 1
nome = input("Digite seu nome");
print ("Seu nome é %s " %nome)

#modelo 2

nome = input("Digite seu nome");
print ("Seu nome é ", nome)

#modelo 3

nome = input("Digite seu nome");
print ("Seu nome é {}" .format(nome))

#modelo 4

nome = input("Escreva seu nome: ")
idade = input(f'{nome}, agora escreva sua idade: ')

print(f'{nome}, {idade} - Identidade criada')
