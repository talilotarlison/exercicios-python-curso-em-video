def main():
 opcaoUsuario = input("Você está na 'entrada', deseja ir para esquerda ou direita? Digite E para esquerda ou D para direita: ")

 if opcaoUsuario == 'E' or opcaoUsuario == 'e':
  print("Abrindo a Porta 1\n")
 elif opcaoUsuario == 'D' or opcaoUsuario == 'd':
   print("Abrindo a Porta 2\n")
 else:
   print("Opção Inválida\n")

if __name__ == '__main__':
 main()
