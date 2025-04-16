print("\n")
print("!!!BEM VINDO AO JOKENPO!!!")
print("\n")
print("O nosso jogo possui três modos distintos, sendo eles: ")
print("1 = Jogador X Jogador")
print("2 = Jogador X Computador")
print("3 = Coputador X Computador")
print("\n")

from random import randint
total_partidas_modo1 = 0
total_partidas_modo2 = 0 
total_partidas_modo3 = 0  
vitorias_jogadorA = 0
vitorias_jogadorB = 0
vitorias_jogador = 0
vitorias_computador = 0
empates_modo1 = 0
empates_modo2 = 0

comecar_jogo = int(input("Para iniciar o jogo digite 1, e vá a seleção de modos: "))
while comecar_jogo > 1 or comecar_jogo < 1:
    comecar_jogo = int(input("Para iniciar o jogo digite 1, e vá a seleção de modos: "))

escolha_modo = int(input("Escolha o modo de jogo seguindo os repectivos números apresentados no começo, 1, 2 ou 3:  "))


while comecar_jogo > 1 :
    comecar_jogo = int(input("Você quer começar um novo jogo? Se sim digite 1, se não digite 0:  "))

while comecar_jogo == 1 or escolha_modo == 1 or escolha_modo == 2 or escolha_modo == 3:
        print("\n")
        print("DIGITE 1 PARA ESCOLHER PEDRA")
        print("DIGITE 2 PARA ESCOLHER PAPEL")
        print("DIGITE 3 PARA ESCOLHER TESOURA")
        print("\n")
           
        if escolha_modo == 1 :
            jogador_A = int(input("Jogador A faça sua escolha entre pedra, papel ou tesoura!   "))
            jogador_B = int(input("Jogador B faça sua escolha entre pedra, papel ou tesoura!   "))

            if jogador_A == jogador_B :
                print("O jogo empatou!")
                empates_modo1 = empates_modo1 + 1
            elif (jogador_A == 1 and jogador_B == 3) or (jogador_A == 2 and jogador_B == 1) or (jogador_A == 3 and jogador_B == 2):
                print("Vitória jogador A")
                vitorias_jogadorA = vitorias_jogadorA + 1
            else:
                print("Vitória jogador B")
                vitorias_jogadorB = vitorias_jogadorB + 1

            total_partidas_modo1 = total_partidas_modo1 + 1
            print("\n")
            comecar_jogo = int(input("Você quer começar um novo jogo nesse mesmo modo? Se sim digite 1, caso queira trocar de modo digite 2, caso queira parar de jogar digite 3:  "))            
            if comecar_jogo == 2:
                escolha_modo = int(input("Escolha o modo de jogo seguindo os repectivos números apresentados no começo, 1, 2 ou 3:  "))
            elif comecar_jogo == 3:
                break
            elif comecar_jogo > 1:
                print("\n")
                comecar_jogo = int(input("Você quer começar um novo jogo nesse mesmo modo? Se sim digite 1, caso queira trocar de modo digite 2, caso queira parar de jogar digite 3:  "))                    
        
        elif escolha_modo == 2:
            jogador_A = int(input("Jogador faça sua escolha entre pedra, papel ou tesoura!   "))
            computador = randint(1,3)
            print ("Escolha aleatória do computador: ", computador)

            if jogador_A == computador :
                print("O jogo empatou!")
                empates_modo2 = empates_modo2 + 1
            elif (jogador_A == 1 and computador == 3) or (jogador_A == 2 and computador == 1) or (jogador_A == 3 and computador == 2):
                print("Vitória jogador")
                vitorias_jogador = vitorias_jogador + 1
            else:
                print("Vitória computador")
                vitorias_computador = vitorias_computador + 1

            total_partidas_modo2 = total_partidas_modo2 + 1
            print("\n")
            comecar_jogo = int(input("Você quer começar um novo jogo nesse mesmo modo? Se sim digite 1, caso queira trocar de modo digite 2, caso queira parar de jogar digite 3:  "))            
            if comecar_jogo == 2:
                escolha_modo = int(input("Escolha o modo de jogo seguindo os repectivos números apresentados no começo, 1, 2 ou 3:  "))
            elif comecar_jogo == 3:
                print("\n")
                print("VOCÊ ENCERROU O JOGO, AGORA VOCÊ IRÁ VER AS ESTATÍSTICAS!!")
                break
            elif comecar_jogo > 1:
                ("\n")
                comecar_jogo = int(input("Você quer começar um novo jogo nesse mesmo modo? Se sim digite 1, caso queira trocar de modo digite 2, caso queira parar de jogar digite 3:  "))            


if total_partidas_modo1 >= 1:
    taxa_vitorias_jogadorA = (vitorias_jogadorA)/(total_partidas_modo1 - empates_modo1) * 100
    taxa_vitorias_jogadorB = (vitorias_jogadorB)/(total_partidas_modo1 - empates_modo1) * 100
    print("\n")
    print("Após", total_partidas_modo1, "partidas essas são as estatísticas de vitórias no modo Jogador X Jogador!!")
    print("\n")
    print("A taxa de vitórias do jogador A é:  ", taxa_vitorias_jogadorA, "%")
    print("A taxa de vitórias do jogador B é:  ", taxa_vitorias_jogadorB, "%")
    print("Também tivemos", empates_modo1, "empates!! ")


if total_partidas_modo2 >= 1:
    taxa_vitorias_jogador = (vitorias_jogador/(total_partidas_modo2 - empates_modo2)) * 100
    taxa_vitorias_computador = (vitorias_computador/(total_partidas_modo2 - empates_modo2)) * 100
    print("\n")
    print("Após", total_partidas_modo2, "partidas essas são as estatísticas de vitórias no modo Jogador X Computador!!")
    print("\n")
    print("A taxa de vitórias do jogador é:  ", taxa_vitorias_jogador, "%")
    print("A taxa de vitórias do computador é:  ", taxa_vitorias_computador, "%")
    print("Também tivemos", empates_modo2, "empates!! ")
    print("\n")
    print("!!!OBRIGADO POR JOGAR!!!")








