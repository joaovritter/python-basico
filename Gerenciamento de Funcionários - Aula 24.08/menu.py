import os
lista = []
while (True):
    os.system ("cls")
    print ("\n")
    print ("Menu Funcionarios \n")
    print ("1 - Cadastrar")
    print ("2 - Listar")
    print ("3 - Excluir")
    print ("4 - Sair\n")
    opcao = input("Opção: ")

    if (opcao == "1"):
        print ("Cadastro de Funcionario\n")
        while (True): #while para validar e receber o nome
            nome_completo = input ("Digite o Nome completo: ") 
            vetor_nomes = nome_completo.split (" ")
            if (len(vetor_nomes)<=1):
                print ("Digite um nome com sobrenome")
            else:
                break
        email = vetor_nomes[0]+"."+ vetor_nomes[-1] + "@ufn.edu.br"
        email = email.lower()
        #verificar se ta na lista
        

        if (lista.__contains__(email)): #contains ve se email ta contido na lista
            print ("Funcionario Com este email ja cadastrado!")
        else:
            lista.append(email) #append joga o email pra lista vazia

        #manter ordenado a lista
        lista.sort()

    elif (opcao == "2"):
        print ("Listar Funcionarios\n")
        if (len(lista)== 0):
            print ("Lista vazia")
        else :
            for i in lista:
                print(i)
        
    elif (opcao == "3"):
        print ("Excluir Funcionarios\n")
        if (len(lista)==0):
            print ("lista vazia")

        else: 
            email = input ("Digite o email a ser excluido: ")
            if (lista.__contains__(email)):
                lista.remove(email)
            else:
                print ("email nao localizado")
    
    elif (opcao == "4"):
        print ("Obrigado por usar o programa, Volte sempre!\n")
        break

    else:
        print ("Opcao Invalida! Tente novamente\n")

    os.system("pause")
    
