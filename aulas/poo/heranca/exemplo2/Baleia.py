# from -> nome do arquivo
# import -> nome da Classe
from Animal import Animal

class Baleia(Animal):
    def __init__(self, tipo, idade, regiao):
        super().__init__(tipo, idade, regiao)