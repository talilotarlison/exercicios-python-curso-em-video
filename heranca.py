#https://diveintopython.org/pt/learn/classes/object-instantiation

# class pessoa 
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def setNome(self, nome):
        self.nome = nome

    def setIdade(self, idade):
        self.idade = idade

    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade
        
   # class pessoa fisica   que herda por heraça atributos da super class   
class PessoaFisica(Pessoa):
   def __init__(self, CPF, nome, idade):
       super().__init__(nome, idade)
       self.CPF = CPF

   def getCPF(self):
       return self.CPF

   def setCPF(self, CPF):
       self.CPF = CPF
        
Talilo = Pessoa('Talilo',28)
print([Talilo.nome,Talilo.idade])
print(Talilo.getNome())
print(Talilo.getIdade())

Amanda = PessoaFisica(16469,'Talilo',28)
print([Amanda.CPF, Amanda.nome,Amanda.idade])
