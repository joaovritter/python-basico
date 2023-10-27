#declarar clase
from datetime import date

class Tipo:
    #descricao é o titulo
    #categoria é doce, salgado ou agridoce
    def __init__(self, descricao, categoria):
        self.descricao = descricao
        self.categoria = categoria
