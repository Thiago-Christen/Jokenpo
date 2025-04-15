print("\n")
print("!!!BEM VINDO AO JOKENPO!!!")
print("\n")
print("DIGITE 1 PARA ESCOLHER PEDRA")
print("DIGITE 2 PARA ESCOLHER PAPEL")
print("DIGITE 3 PARA ESCOLHER TESOURA")
print("\n")

comecar_jogo = int(input("Você quer começar um novo jogo? Se sim digite 1, se não digite 0:  "))
total_partidas = 0
vitorias_jogadorA = 0
vitorias_jogadorB = 0
empates = 0

while comecar_jogo > 1 :
    comecar_jogo = int(input("Você quer começar um novo jogo? Se sim digite 1, se não digite 0:  "))

while comecar_jogo == 0 :
    break 

while comecar_jogo == 1 :
    jogador_A = int(input("Faça sua escolha entre pedra, papel ou tesoura!   "))
    jogador_B = int(input("Faça sua escolha entre pedra, papel ou tesoura!   "))

    if jogador_A == jogador_B :
        print("O jogo empatou!")
        empates = empates + 1
    elif (jogador_A == 1 and jogador_B == 3) or (jogador_A == 2 and jogador_B == 1) or (jogador_A == 3 and jogador_B == 2):
        print("Vitória jogador A")
        vitorias_jogadorA = vitorias_jogadorA + 1
    else:
        print("Vitória jogador B")
        vitorias_jogadorB = vitorias_jogadorB + 1

    total_partidas = total_partidas + 1
    comecar_jogo = int(input("Você quer começar um novo jogo? Se sim digite 1, se não digite 0:  "))

taxa_vitorias_jogadorA = (vitorias_jogadorA)/(total_partidas - empates) * 100
taxa_vitorias_jogadorB = (vitorias_jogadorB)(total_partidas - empates) * 100

print("\n")
print("Após", total_partidas, "partidas essas são as estatísticas de vitórias!!")
print("\n")
print("A taxa de vitórias do jogador A é:  ", taxa_vitorias_jogadorA)
print("A taxa de vitórias do jogador B é:  ", taxa_vitorias_jogadorB)
print("Também tivemos", empates, "empates!! ")


