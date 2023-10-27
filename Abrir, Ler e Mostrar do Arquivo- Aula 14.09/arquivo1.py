#criar um programa ou metodo que abra,leia e mostre o conteudo de um arquivo


while (True):
    try: 
        nome_arquivo = input ("digite o nome do arquivo que deseja abrir: \n")
        leitor = open(nome_arquivo, 'r', encoding='utf8')
        print ("Arquivo localizado com sucesso\n")

        for i in leitor:
            i = i.replace('\n','') # i = i pq o replace é um metodo com retorno, por isso tem q retornar para o i.
            print (i)
        leitor.close()
        break
    except:
        print ("Problema para localizar ou abrir o arquivo\n")
