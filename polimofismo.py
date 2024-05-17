#https://diveintopython.org/pt/learn/classes/object-instantiation

class MediaNotas:
    def __init__(self, nota1, nota2,nota3):
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
    
    def calcularMedia(self):
      resultado = (self.nota1 + self.nota2 + self.nota3)/3
      return round(resultado,2)
      
Media = MediaNotas(5,5,5)
print(Media.calcularMedia())

class MediaNotasDoAluno(MediaNotas):
    def __init__(self,aluno, nota1, nota2,nota3, nota_extra):
        super().__init__(nota1, nota2,nota3)
        self.aluno = aluno
        self.nota_extra = nota_extra
        
    def calcularMedia(self):
      resultado = (self.nota1 + self.nota2 + self.nota3 + self.nota_extra)/4
      return round(resultado,2)
        
# https://horadecodar.com.br/como-limitar-numeros-decimais-em-python/
#https://blog.michelelozada.com.br/como-delimitar-casas-decimais-em-python/

MediaJoao = MediaNotasDoAluno("João", 9,5,4.5,9)
print(MediaJoao.aluno,':',MediaJoao.calcularMedia())
