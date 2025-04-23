#Desenvolvido por Gabriel Garcia e Thiago Soares

#Importa Biblioteca para implementar no(s) modo(s) Computador(es)
from random import randint

#Variáveis para controle de estatísticas
total_partidas_modo1 = 0
total_partidas_modo2 = 0 
total_partidas_modo3 = 0  

vitorias_jogadorA = 0
vitorias_jogadorB = 0
vitorias_jogador = 0
vitorias_computador = 0
vitorias_computador1 = 0
vitorias_computador2 = 0

empates_modo1 = 0
empates_modo2 = 0
empates_modo3 = 0

#Interface inicial do nosso jogo
print("\n")
print("!!!BEM VINDO AO JOKENPO!!!")
print("\n")
print("O nosso jogo possui três modos distintos, sendo eles: ")
print("1 = Jogador X Jogador")
print("2 = Jogador X Computador")
print("3 = Computador X Computador")
print("\n")

#Recebe se jogar quer ir iniciar o jogo
comecar_jogo = int(input("Para iniciar o jogo digite 1, e vá a seleção de modos: "))

#Verifica se jogar quer iniciar o jogo( verifica se váriavel comecar_jogo é diferente de 1)
while comecar_jogo != 1:
    comecar_jogo = int(input("Para iniciar o jogo digite 1, e vá a seleção de modos: "))

#Escolhe qual será o modo de jogo
escolha_modo = int(input("Escolha o modo de jogo seguindo os respectivos números apresentados no começo, 1, 2 ou 3: "))

#Loop principal do nosso jogo(Verifica se o modo de jogo é válido)
while comecar_jogo == 1 or escolha_modo == 1 or escolha_modo == 2 or escolha_modo == 3:

        if escolha_modo < 1 or escolha_modo > 3:
            escolha_modo = int(input("Escolha o modo de jogo seguindo os respectivos números apresentados no começo, 1, 2 ou 3: "))
        
        #MODO: Jogador x Jogador
        elif escolha_modo == 1 :

            #Mostra as items que podem ser escolhidos
            print('\n----------------------------------------------------------------')
            print("\n")
            print("DIGITE 1 PARA ESCOLHER PEDRA")
            print("DIGITE 2 PARA ESCOLHER PAPEL")
            print("DIGITE 3 PARA ESCOLHER TESOURA")
            print('\n')

            #Mostra o Modo Escolhido
            print("Você escolheu o modo de Jogador X Jogador")
            print("\n")

            #Escolhas dos Jogadores
            jogador_A = int(input("Jogador A faça sua escolha entre pedra, papel ou tesoura! "))
            jogador_B = int(input("Jogador B faça sua escolha entre pedra, papel ou tesoura! "))

            if jogador_A < 1 or jogador_A > 3:
                jogador_A = int(input("\nEscolha Inválida! Jogador A refaça sua escolha entre pedra, papel ou tesoura! "))

            if jogador_B < 1 or jogador_B > 3:
                jogador_B = int(input("\nEscolha Inválida! Jogador A refaça sua escolha entre pedra, papel ou tesoura! "))

            if jogador_A == jogador_B :
                print("\nO jogo empatou!")
                empates_modo1 = empates_modo1 + 1

            elif (jogador_A == 1 and jogador_B == 3) or (jogador_A == 2 and jogador_B == 1) or (jogador_A == 3 and jogador_B == 2):
                print("\nVitória do jogador A")
                vitorias_jogadorA = vitorias_jogadorA + 1

            else:
                print("\nVitória do jogador B")
                vitorias_jogadorB = vitorias_jogadorB + 1

            total_partidas_modo1 = total_partidas_modo1 + 1
            print("\n")
            comecar_jogo = int(input("----------------------------------------------------------------\nVocê quer começar um novo jogo nesse mesmo modo? Se sim digite 1, caso queira trocar de modo digite 2, caso queira parar de jogar digite 3: "))            
            if comecar_jogo == 2:
                print("\n")
                print("1 = Jogador X Jogador")
                print("2 = Jogador X Computador")
                print("3 = Coputador X Computador")
                print('\n')
                escolha_modo = int(input("Escolha o modo de jogo seguindo os respectivos números apresentados no começo, 1, 2 ou 3:  "))
            elif comecar_jogo == 3:
                break
            elif comecar_jogo > 1:
                print("\n")
                comecar_jogo = int(input("----------------------------------------------------------------\nVocê quer começar um novo jogo nesse mesmo modo? Se sim digite 1, caso queira trocar de modo digite 2, caso queira parar de jogar digite 3: "))                    

        #MODO: Jogador x Computador
        elif escolha_modo == 2:

            #Mostra as items que podem ser escolhidos
            print('\n----------------------------------------------------------------')
            print("\n")
            print("DIGITE 1 PARA ESCOLHER PEDRA")
            print("DIGITE 2 PARA ESCOLHER PAPEL")
            print("DIGITE 3 PARA ESCOLHER TESOURA")
            print('\n')

            #Mostra o Modo Escolhido
            print("\n")
            print("Você escolheu o modo de Jogador X Computador")

            #Escolhas do Jogador e Escolhas aleatórias do computador
            jogador = int(input("\nJogador faça sua escolha entre pedra, papel ou tesoura! "))
            computador = randint(1,3)
            print ("Escolha aleatória do computador: ", computador)

            if jogador < 1 or jogador > 3:
                 jogador = int(input("\nEscolha Inválida! Jogador refaça sua escolha entre pedra, papel ou tesoura! "))

            if jogador == computador :
                print("O jogo empatou!")
                empates_modo2 = empates_modo2 + 1

            elif (jogador == 1 and computador == 3) or (jogador == 2 and computador == 1) or (jogador == 3 and computador == 2):
                print("Vitória do jogador")
                vitorias_jogador = vitorias_jogador + 1

            else:
                print("Vitória do computador")
                vitorias_computador = vitorias_computador + 1

            total_partidas_modo2 = total_partidas_modo2 + 1
            print("\n")

            #Pergunta se o usuário quer começar uma nova partida
            comecar_jogo = int(input("----------------------------------------------------------------\nVocê quer começar um novo jogo nesse mesmo modo? Se sim digite 1, caso queira trocar de modo digite 2, caso queira parar de jogar digite 3: "))

            if comecar_jogo == 2:

                print("\n")
                print("1 = Jogador X Jogador")
                print("2 = Jogador X Computador")
                print("3 = Coputador X Computador")
                print("\n")

                escolha_modo = int(input("Escolha o modo de jogo seguindo os respectivos números apresentados no começo, 1, 2 ou 3:  "))

            elif comecar_jogo == 3:
                print("\n")
                print("VOCÊ ENCERROU O JOGO, AGORA VOCÊ IRÁ VER AS ESTATÍSTICAS!!")
                break
            elif comecar_jogo > 1:
                ("\n")
                comecar_jogo = int(input("----------------------------------------------------------------\nVocê quer começar um novo jogo nesse mesmo modo? Se sim digite 1, caso queira trocar de modo digite 2, caso queira parar de jogar digite 3: "))
  
        #MODO: Computador x Computador
        elif escolha_modo == 3:

            #Mostra as items que podem ser escolhidos
            print('\n----------------------------------------------------------------')
            print("\n")
            print("DIGITE 1 PARA ESCOLHER PEDRA")
            print("DIGITE 2 PARA ESCOLHER PAPEL")
            print("DIGITE 3 PARA ESCOLHER TESOURA")
            print('\n')

            #Mostra as items que podem ser escolhidos
            print("\n")
            print("Você escolheu o modo de Computador X Computador")
            print("\n")

            #Escolhas aleatórias para ambos computadores
            computador1 = randint(1,3)
            print("A escolha aleatória do computador 1 foi: ", computador1)
            computador2 = randint(1,3)
            print("A escolha aleatória do computador 2 foi: ", computador2)

            if computador1 == computador2 :
                print("O jogo empatou!")
                empates_modo3 = empates_modo3 + 1

            elif (computador1 == 1 and computador2 == 3) or (computador1 == 2 and computador2 == 1) or (computador1 == 3 and computador2 == 2):
                print("Vitória do computador 1")
                vitorias_computador1 = vitorias_computador1 + 1

            else:
                print("Vitória do computador 2")
                vitorias_computador2 = vitorias_computador2 + 1

            total_partidas_modo3 = total_partidas_modo3 + 1
            print("\n")

            #Pergunta se o usuário quer começar uma nova partida
            comecar_jogo = int(input("----------------------------------------------------------------\nVocê quer começar um novo jogo nesse mesmo modo? Se sim digite 1, caso queira trocar de modo digite 2, caso queira parar de jogar digite 3: "))

            if comecar_jogo == 2:
                print("\n")
                print("1 = Jogador X Jogador")
                print("2 = Jogador X Computador")
                print("3 = Coputador X Computador")
                print("\n")

                escolha_modo = int(input("Escolha o modo de jogo seguindo os respectivos números apresentados no começo, 1, 2 ou 3: "))

            elif comecar_jogo == 3:
                print("\n")
                print("VOCÊ ENCERROU O JOGO, AGORA VOCÊ IRÁ VER AS ESTATÍSTICAS!!")
                break

            elif comecar_jogo > 1:
                ("\n")
                comecar_jogo = int(input("----------------------------------------------------------------\nVocê quer começar um novo jogo nesse mesmo modo? Se sim digite 1, caso queira trocar de modo digite 2, caso queira parar de jogar digite 3: "))         

#Apresentação de estatísticas ao final de cada modo

#ESTATÍSTICAS Modo Jogador X Jogador
if total_partidas_modo1 >= 1 and total_partidas_modo1 != empates_modo1:
    taxa_vitorias_jogadorA = vitorias_jogadorA/(total_partidas_modo1 - empates_modo1) * 100
    taxa_vitorias_jogadorB = vitorias_jogadorB/(total_partidas_modo1 - empates_modo1) * 100
    print("\n")
    print("Após", total_partidas_modo1 , " partida(s) essas são as estatísticas de vitórias no modo Jogador X Jogador!!")
    print("\n")

    print("A taxa de vitórias do jogador A é:  ", taxa_vitorias_jogadorA, "%")
    print("A taxa de vitórias do jogador B é:  ", taxa_vitorias_jogadorB, "%")
    print("Também tivemos", empates_modo1, "empate(s)!! ")
    print("\n")

elif total_partidas_modo1 >= 1 and total_partidas_modo1 == empates_modo1:
    print("\n")
    print("No modo Jogador x Jogador só teve empates, logo a taxa de vitóia de ambos é de 0%")
    print("\n")
    print('----------------------------------------------------------------')

#ESTATÍSTICAS Modo Jogador X Computador
if total_partidas_modo2 >= 1 and total_partidas_modo2 != empates_modo2:
    taxa_vitorias_jogador = (vitorias_jogador)/(total_partidas_modo2 - empates_modo2) * 100
    taxa_vitorias_computador = (vitorias_computador)/(total_partidas_modo2 - empates_modo2) * 100
    print("\n")
    print("Após", total_partidas_modo2 , " partida(s) essas são as estatísticas de vitórias no modo Jogador X Computador!!")
    print("\n")

    print("A taxa de vitórias do jogador é:  ", taxa_vitorias_jogador, "%")
    print("A taxa de vitórias do computador é:  ", taxa_vitorias_computador, "%")
    print("Também tivemos", empates_modo2, "empate(s)!! ")
    print("\n")

elif total_partidas_modo2>= 1 and total_partidas_modo2 == empates_modo2:
    print("\n")
    print("No modo Jogador x Computador só teve empates, logo a taxa de vitóia de ambos é de 0%")
    print("\n")
    print('----------------------------------------------------------------')

#ESTATÍSTICAS Modo Computador x Computador
if total_partidas_modo3 >= 1 and total_partidas_modo3 != empates_modo3:
    taxa_vitorias_computador1 = (vitorias_computador1/(total_partidas_modo3 - empates_modo3)) * 100
    taxa_vitorias_computador2 = (vitorias_computador2/(total_partidas_modo3 - empates_modo3)) * 100

    print("\n")
    print("Após", total_partidas_modo3 , " partida(s) essas são as estatísticas de vitórias no modo Computador X Computador")
    print("\n")

    print("A taxa de vitórias do jogador A é:  ", taxa_vitorias_computador1)
    print("A taxa de vitórias do computador é:  ", taxa_vitorias_computador2)
    print("Também tivemos", empates_modo3, "empate(s)!! ")
    print("\n")

elif total_partidas_modo3 >= 1 and total_partidas_modo3 == empates_modo3:
    print("\n")
    print("No modo Computador x Computador só teve empates, logo a taxa de vitóia de ambos é de 0%")
    print("\n")
    print('----------------------------------------------------------------')

print("!!!OBRIGADO POR JOGAR!!!")
