from math import sqrt


class SegundoGrau:
    def __init__(self, a:int, b:int, c:int):
        self.a = a
        self.b = b
        self.c = c
        self.delta = self._calcula_delta()
        self.raiz_delta = self._calcula_raiz_delta()
        
        if not self.eh_menor_que_zero(self.delta):
            self.raiz = self._calcula_raizes()
    

    def _calcula_delta(self):
        return (self.b**2) - (4 * self.a * self.c)
    

    def _calcula_raiz_delta(self):
        if self.eh_maior_que_zero(self.delta):
            return round(sqrt(self._calcula_delta()), 2)
        
        return 0
    

    def _calcula_raizes(self) -> dict:
        raizes = dict()
        raizes['X1'] = self.calcula_uma_unica_raiz('X1')

        if self.eh_maior_que_zero(self.delta) > 0:
            raizes['X2'] = self.calcula_uma_unica_raiz('X2')
        
        return raizes
    

    def calcula_uma_unica_raiz(self, valor:str):
        if valor == 'X1':
            resultado = ((self.b * -1) + sqrt(self.delta)) / (2*self.a)
        elif valor == 'X2':
            resultado = ((self.b * -1) - sqrt(self.delta)) / (2*self.a)
        
        return round(resultado,2)

    
    def eh_menor_que_zero(self, valor):
        if valor < 0:
            return True
        
        return False
    

    def eh_maior_que_zero(self, valor):
        if valor > 0:
            return True
        
        return False