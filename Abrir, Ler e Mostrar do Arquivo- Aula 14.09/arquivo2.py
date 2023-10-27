lista_email = []
while(True):
    try:
        nome_arquivo = input ("Digite o nome de arquivo com dados de usuario (.dat): \n")
        leitor = open(nome_arquivo, 'r', encoding='utf8')

        for linha in leitor:
            #vetor_linha [0]= nome
            #vetor_linha [1]= email
            #vetor_linha [2]= profissao
        
            vetor_linha = linha.split(';')
            lista_email.append(vetor_linha[1])

        leitor.close()
        lista_email.sort()
        print(lista_email)

        escritor = open('emails.dat', 'w') #cria um novo arquivo
        for e in lista_email:
            escritor.write(e+"\n") # + \n pra por um \n a cada vez que percorre

        escritor.close()
        
        break

    except:
        print ("Problema com a leitura\n")
