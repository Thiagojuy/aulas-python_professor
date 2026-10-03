class Valor:
    def __init__(self, valor):
        try:
            self.valor = float(valor)
        except ValueError:
            print("Valor não aceito")


valor1 = Valor("Vinte e três")