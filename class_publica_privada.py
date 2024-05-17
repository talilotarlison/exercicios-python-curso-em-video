#https://diveintopython.org/pt/learn/classes/object-instantiation

# class com atributos  privados, e metodos tambem podem ser privados
class MediaNotas:
    def __init__(self, nota1, nota2,nota3):
        self.__nota1 = nota1
        self.__nota2 = nota2
        self.__nota3 = nota3
    
    def calcularMedia(self):
      resultado = (self.__nota1 + self.__nota2 + self.__nota3)/3
      return round(resultado,2)
      
Media = MediaNotas(5,5,5)
print(Media.calcularMedia())
