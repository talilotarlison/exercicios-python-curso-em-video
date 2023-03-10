# modelo de coleta de dados
nome = input("Qual o seu nome?");
print('%s , digite sua data na proxima etapa da coleta:' %nome);

dia = input("Dia: ")
mes = input(f'{nome}, agora escreva o mes: ')
ano = input('{}, agora escreva o ano: ' .format(nome))

print(f'{nome}, {dia}/{mes}/{ano} - Identidade criada com sua data')
