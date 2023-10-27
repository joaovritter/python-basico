#Desafio
print ("* Digite Ctrl + Shift + V para colar o texto\n\n")
texto = input ("Digite o Texto: ")
palavras= texto.split()
qtd_palavras=len(palavras)

print ("quantidade de palavras: ", qtd_palavras)


qtd_artigos = 0

artigos = ["o", "a", "os", "as", "um", "uma", "uns", "umas"] #aqui é uma lista


for recebe_palavra in palavras: #recebe_palavra vai receber os valores de palavras
    if recebe_palavra.lower() in artigos: #se tiver alguma palavra igual no artigo, vai contar artigo++
        qtd_artigos+= 1
        

print ("quantidade de artigos: ", qtd_artigos)


#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

preposicoes = ["a", "ante", "após", "até", "com", "contra", "de", "desde", "em", "entre", "para", "perante", 
"por", "sem", "sob", "sobre", "trás"]


qtd_preposicoes=0
prep_vazia = []
for recebe_palavra in palavras:
    if recebe_palavra.lower() in preposicoes:
        prep_vazia.append(recebe_palavra) #append (....) poe a palavra pra dentro da lista
        qtd_preposicoes+=1
    
print ("Quantidade de preposicoes: ",qtd_preposicoes," \n" "preposicoes: ", prep_vazia)
    
