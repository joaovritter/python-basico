"""1 - Um usuário (diabético) de insulina rápida precisa fazer uso do medicamento sempre que for realizar uma refeição. Assim, faça um programa que receba do usuário sua glicemia do momento (mg/dl),meta pré-refeição (em geral é 100 mg/dl), fator de sensibilidade (valor inteiro entre 20 a 60). 
    A partir desses valores, o programa deve calcular e exibir para o usuário a quantidade de insulina que ele deverá administrar baseada na equação:
#    quantidade_insulina = (glicemia_do_momento - meta_pre_refeicao) / fator_sensibilidade"""


glicemia = int(input("qual a glicemia? "))
pre_refeicao = int(input("qual meta pre refeicao? "))
sensi = int(input("qual o fator de sensibilidade? "))

if sensi <20 or sensi>60 :
    print ("Valor invalida para o fator da sensibilidade")

else :
    qtd_insulina = (glicemia - pre_refeicao)/sensi
    print ("A quantidade de insulina eh: ", qtd_insulina)
