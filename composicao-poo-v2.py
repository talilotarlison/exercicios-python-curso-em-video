#https://diveintopython.org/pt/learn/classes/object-instantiation
#https://www.alura.com.br/artigos/poo-programacao-orientada-a-objetos

# composição com python
#https://www.alura.com.br/artigos/conhecendo-as-tuplas-no-python

class Aluno:
    def __init__(self, nome, idade, cpf, notas ):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.notas = notas

        
    def getMediaNotas(self):
      Media = MediaNotas(self.notas['nota1'], self.notas['nota2'], self.notas['nota3'])
      return Media.calcularMedia()

#https://www.alura.com.br/artigos/trabalhando-com-o-dicionario-no-python
#https://www.alura.com.br/artigos/conhecendo-as-tuplas-no-python
#https://www.alura.com.br/artigos/trabalhando-com-o-dicionario-no-python

class MediaNotas:
    def __init__(self, nota1, nota2,nota3):
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
    
    def calcularMedia(self):
      resultado = (self.nota1 + self.nota2 + self.nota3)/3
      return round(resultado,2)


Talilo = Aluno("Talilo", 29, 798499449,dict([('nota1',5),('nota2',6),('nota3',10)]))

print(Talilo.nome, ':',Talilo.getMediaNotas())

Jose = Aluno("Jose", 29, 798499449,{'nota1':8,'nota2':6,'nota3':10})

print(Jose.nome, ':',Jose.getMediaNotas())
