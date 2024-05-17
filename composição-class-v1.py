#https://diveintopython.org/pt/learn/classes/object-instantiation

# composição
#https://www.alura.com.br/artigos/conhecendo-as-tuplas-no-python

class Aluno:
    def __init__(self, nome, idade, cpf, notas ):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.notas = notas

        
    def getMediaNotas(self):
      Media = MediaNotas(self.notas[0], self.notas[1], self.notas[2])
      return Media.calcularMedia()


class MediaNotas:
    def __init__(self, nota1, nota2,nota3):
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
    
    def calcularMedia(self):
      resultado = (self.nota1 + self.nota2 + self.nota3)/3
      return round(resultado,2)

Talilo = Aluno("Talilo", 29, 798499449,[5,5,5])

print(Talilo.nome, ':',Talilo.getMediaNotas())
