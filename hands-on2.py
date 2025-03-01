
class ModeloPredictivo:
    def __init__(self, dataset):
        self.dataset = dataset
        self.y = self.dataset['sales']
        self.x = self.dataset['advertising']

    def obtenerB0(self):
        # Calculo de la parte superior

        # Sumatoria de X^2
        primera_parte = self.SumXPow()
        
        # Sumatoria de y
        segunda_parte = self.SumY()

        # Construir la primera parte
        FirstPartUpper = primera_parte * segunda_parte

        # Sumatoria de X
        tercera_parte = self.SumX()

        # Sumatoria del producto de X e Y
        cuarta_parte = self.SumProdXY()

        # Construir la segunda parte
        SecondPartUpper = tercera_parte * cuarta_parte

        # Obtener total
        TotalUpper = FirstPartUpper - SecondPartUpper
 
        # Calculo de la parte inferior

        # n producto sumatoria de x cuadrado
        quinta_parte = self.nSumXPow()

        # sumatoria de x, todo al cuadrado
        sexta_parte = self.PowSumX()

        # Obtener total
        TotalLower = quinta_parte-sexta_parte

        return TotalUpper / TotalLower
    
    def obtenerB1(self):
        # Calculo de la parte superior

        # n producto sumatoria del producto de x e y
        primera_parte = self.nProdSumXProdY()

        #Sumatoria de x
        segunda_parte = self.SumX()

        # Sumatoria de y
        tercera_parte = self.SumY()

        # Construir el total
        totalUpper = primera_parte - (segunda_parte * tercera_parte)

        #Calculo de la parte inferior

        # n producto de sumatoria de X al cuadrado
        cuarta_parte = self.nProdXPow()

        #sumatoria de x, todo al cuadrado
        quinta_parte = self.PowSumX()

        # Construir el total
        totalLower = cuarta_parte - quinta_parte

        return totalUpper / totalLower

    def SumXPow(self):
        total = 0
        for value in self.x:
            total += pow(value,2)

        return total
    
    def SumY(self):
        total = 0
        for value in self.y:
            total += value

        return total
    
    def SumX(self):
        total = 0
        for value in self.x:
            total += value

        return total
    
    def SumProdXY(self):
        total = 0
        for value_x, value_y in zip(self.x, self.y):
            total += value_x * value_y

        return total
    
    def nSumXPow(self):
        subtotal = self.SumXPow()
        ocurrencias = len(self.x)
        return ocurrencias * subtotal
    
    def PowSumX(self):
        subtotal = self.SumX()
        return pow(subtotal,2)
    
    
    def nProdSumXProdY(self):
        subtotal = self.SumProdXY()
        ocurrencias = len(self.x)
        return subtotal * ocurrencias

    def nProdXPow(self):
        subtotal = self.SumXPow()
        ocurrencias = len(self.x)
        return subtotal * ocurrencias
    
    def calcularEcuacion(self, B0, B1, Adv):
        resultado =  B1*Adv + B0
        print(f'El resultado de sales para un advertising de {Adv} es: {resultado}')

if __name__ == "__main__":
    dataset = {
        'sales': [651, 762, 856, 1063, 1190, 1298, 1421, 1440, 1518],
        'advertising': [23, 26, 30, 34, 43, 48, 52, 57, 58]
    }

    ejercicio = ModeloPredictivo(dataset)
    B0 = ejercicio.obtenerB0()
    B1 = ejercicio.obtenerB1()
    print(f'Formula obtenida: y = {B0} + {B1}x')
    print(f'También se puede interpretar como sales = {B0} + {B1}(advertising)')
    print(' - - - - -  - -  - - - -')
    ejercicio.calcularEcuacion(B0,B1,20)
    ejercicio.calcularEcuacion(B0,B1,24)
    ejercicio.calcularEcuacion(B0,B1,45)
    ejercicio.calcularEcuacion(B0,B1,54)
    ejercicio.calcularEcuacion(B0,B1,62)
    print(' - - - - -  - -  - - - -')
    print('Programa realizado por: Alejandro Jesus Garcia Covarrubias')
    print('219612627')
    