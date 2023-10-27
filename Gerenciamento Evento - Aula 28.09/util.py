def conexao_base(lista):
    try:
        leitor = open('inscricoes.dat','r')
        for linha in leitor:
            vetor_linha = linha.split(';')
            lista.append(vetor_linha[0])
        leitor.close()
    except:
        pass

def inscricao(lista):
    matricula = input('Informe matrícula: ')
    if matricula in lista:
        print('Esta matrícula já foi inscrita no evento')
    else:
        lista.append(matricula)
        nome = input('Nome: ')
        nome = nome.upper()
        email = input('Email: ')
        email = email.lower()
        escritor = open('inscricoes.dat','a')
        escritor.write(matricula + ';' + nome + ';' + email + '\n')
        escritor.close()

def listagem():
    try:
        leitor = open('inscricoes.dat','r',encoding='utf8')
        for linha in leitor:
            vetor_linha = linha.split(';')
            print('Nome:',vetor_linha[1],'Matrícula:',vetor_linha[0])

        leitor.close()
    except:
        print('Sem inscrições até o momento')


def entrada (lista_entrada, lista_inscritos):
    matricula = input('Informe matrícula: ')
    if matricula in lista_inscritos: 
        if matricula in lista_entrada:
            print('Ja esta no evento')
        else:        
            lista_entrada.append(matricula)
            escritor = open('entrada.dat','a')
            escritor.write(matricula +';'+'\n')
            escritor.close()
            print ("Entrada Registrada!")
    else:
        print ("Nao registrado no evento")


def saida(lista_entrada, lista_saida):
    matricula = input('Informe matrícula: ')
    if matricula in lista_entrada:   
        lista_saida.append(matricula)
        escritor = open('saida.dat','a')
        escritor.write(matricula +';'+'\n')
        escritor.close()
        print ("Saida Registrada!")
    else:
        print ("Nao registrado no evento")



def conexao_entrada(lista):
    try:
        leitor = open('entrada.dat','r')
        for linha in leitor:
            vetor_linha = linha.split(';')
            lista.append(vetor_linha[0])
        leitor.close()
    except:
        pass