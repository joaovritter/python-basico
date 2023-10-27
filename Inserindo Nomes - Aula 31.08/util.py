import random

# def popular (lista,local,qtd):
    # for i in range(0,qtd):
        # lista.append(random.randint(0,100))
# 
    # lista.sort()
    # 
# def exibir(lista):
    # for i in lista:
        # print(i)




def popular_nomes(lista,qtd):
    #while (True):
    for i in range(0,qtd):
        nome= input("Digite o Nome: ")
        nome=nome.upper()
        if (lista.__contains__(nome)):
            print ("Nome ja escrito")
            break

        lista.append(nome)

    lista.sort()
    
def exibir_nomes(lista):
    
    for i in lista:
        print(i)