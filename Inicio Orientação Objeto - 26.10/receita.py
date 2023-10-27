class Receita:
    def __init__(self, titulo, tipo):
        self.titulo = titulo
        self.tipo = tipo
        self.ingredientes = []
        self.modo_preparo = ""

    def informar_ingredientes (self):
        while (True):
            ingredientes = input ("Escreva SAIR ou o ingrediente: ")
            if ingredientes.upper() == "SAIR":
                break
            
            self.ingredientes.append(ingredientes.upper())

    def mostrar_ingredientes (self):
        for i in self.ingredientes:
            print(i)
            

        
        