print("\n")
print("!!!BEM VINDO AO JOKENPO!!!")
print("\n")
print("DIGITE 1 PARA ESCOLHER PEDRA")
print("DIGITE 2 PARA ESCOLHER PAPEL")
print("DIGITE 3 PARA ESCOLHER TESOURA")
print("\n")


from random import randint

comecar_jogo = int(input("Você quer começar um novo jogo? Se sim digite 1, se não digite 0:  "))
total_partidas = 0
vitorias_jogadorA = 0
vitorias_computador = 0
empates = 0

while comecar_jogo > 1 :
    comecar_jogo = int(input("Você quer começar um novo jogo? Se sim digite 1, se não digite 0:  "))
    

while comecar_jogo == 0 :
    break 

while comecar_jogo == 1 :
    jogador_A = int(input("Faça sua escolha entre pedra, papel ou tesoura!   "))
    computador = randint(1,3)
    print ("Escolha aleatória do computador: ", computador)

    if jogador_A == computador :
        print("O jogo empatou!")
        empates = empates + 1
    elif (jogador_A == 1 and computador == 3) or (jogador_A == 2 and computador == 1) or (jogador_A == 3 and computador == 2):
        print("Vitória jogador A")
        vitorias_jogadorA = vitorias_jogadorA + 1
    else:
        print("Vitória computador")
        vitorias_computador = vitorias_computador + 1

    total_partidas = total_partidas + 1
    comecar_jogo = int(input("Você quer começar um novo jogo? Se sim digite 1, se não digite 0:  "))

taxa_vitorias_jogadorA = (vitorias_jogadorA/(total_partidas - empates)) * 100
taxa_vitorias_computador = (vitorias_computador/(total_partidas - empates)) * 100

print("\n")
print("Após", total_partidas, "partidas essas são as estatísticas de vitórias!!")
print("A taxa de vitórias do jogador A é:  ", taxa_vitorias_jogadorA)
print("A taxa de vitórias do computador é:  ", taxa_vitorias_computador)
print("Também tivemos", empates, "empates!! ")




