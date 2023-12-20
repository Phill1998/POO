class Conta_corrente:

    def __init__(self, dinheiro, percentual):
        self.__dinheiro = dinheiro
        self.__percentual = percentual
    
    @property
    def calc_imposto(self):
        self.__dinheiro * self.__percentual
        return self.__dinheiro - (self.__dinheiro * self.__percentual)
        
    @property
    def valor(self):
        return self.__dinheiro

    @property
    def percentual(self): 
       return self.__dinheiro * self.__percentual

class Poupança(Conta_corrente):

    def valor(self):
        return self.__dinheiro


class ContaImposto(Conta_corrente):
 
    def __init__(self, dinheiro, percentual):
        super().__init__(dinheiro, percentual)


c = Conta_corrente(18000, 0.80)
print(c.calc_imposto)