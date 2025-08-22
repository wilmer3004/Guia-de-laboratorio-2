class Calculator:
    def __init__ (self):
        self.x = 0  
        self.y= 0

    def solicitar_numeros(self):
            try:
                self.x = int(input("Digite x: "))
                self.y = int(input("Digite y: "))
            except ValueError:
                print("Error: Por favor ingrese números enteros.")
                self.solicitar_numeros()

    def suma(self, a, b):
        return a + b
    
    def resta(self, a, b):
        return a - b
    
if __name__ == "__main__":
    g = Calculator() 
    g.solicitar_numeros()
    print("Suma: ", g.suma(g.x, g.y))
    print("Resta: ", g.resta(g.x, g.y))
