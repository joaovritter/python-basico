#2 - Faça um programa que ajude motoristas calcular e estimar viagens com diferentes tempos de viagem.
#    O programa deve receber do usuário do sistema (motorista) a distância a ser percorrida e o tempo
#    desejado da viagem. A partir disso, o programa deve calcular e exibir na tela a velocidade média
#    necessária.

distancia = float(input("Qual a distancia em Km? "))
tempo = float(input("Qual o tempo em minutos? "))
vm=distancia/tempo
print ("Velocide media = ", vm)