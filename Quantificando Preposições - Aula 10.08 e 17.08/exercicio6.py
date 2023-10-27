#6 - Construa um programa em Python em que o usuário insira a sigla de um estado brasileiro em que 
#    uma pessoa nasceu e, em seguida imprima uma das seguintes mensagens: 
#    Carioca Paulista Mineiro Outros estados

estado = input("digite a sigla de um estado da regiao sul do brasil:  ")
estado = estado.upper()
if estado == "RS":
    print("Rio Grande do Sul, Gaucho")
    
if estado == "SC":
    print ("Santa Catarina, Catarinense")

if estado == "PR":
    print ("Parana, Paranaense")
