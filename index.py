from random import randint # Importa Biblioteca para implementar no(s) modo(s) Computador(es)

# Variáveis para controle de estatísticas
total_partidas_modo1 = 0
total_partidas_modo2 = 0 
total_partidas_modo3 = 0  

vitorias_jogadorA = 0
vitorias_jogadorB = 0
vitorias_jogador = 0
vitorias_computador = 0
vitorias_computador_A = 0
vitorias_computador_B = 0

empates_modo1 = 0
empates_modo2 = 0
empates_modo3 = 0

# Interface inicial do nosso jogo
print("\n")
print("!!! BEM-VINDO AO JOKENPÔ !!!")
print("\n")
print("Nosso jogo possui três modos distintos:")
print("1 = Jogador X Jogador")
print("2 = Jogador X Computador")
print("3 = Computador X Computador")
print("\n")

# Recebe se jogar quer ir iniciar o jogo
comecar_jogo = int(input("Para iniciar o jogo digite 1, e vá à seleção de modos: "))

# Verifica se jogar quer iniciar o jogo( verifica se váriavel comecar_jogo é diferente de 1)
while comecar_jogo != 1:
    comecar_jogo = int(input("Para iniciar o jogo digite 1, e vá à seleção de modos: "))

# Escolhe qual será o modo de jogo
escolha_modo = int(input("Escolha o modo de jogo (1, 2 ou 3): "))

# Loop principal do nosso jogo(Verifica se o modo de jogo é válido)
while comecar_jogo == 1 and escolha_modo in [1, 2, 3]:

    print("\n")
    print("DIGITE 1 PARA ESCOLHER PEDRA")
    print("DIGITE 2 PARA ESCOLHER PAPEL")
    print("DIGITE 3 PARA ESCOLHER TESOURA")
    print("\n")
    
    # MODO 1: Jogador X Jogador
    if escolha_modo == 1:
        jogador_A = int(input("Jogador A, escolha: "))
        jogador_B = int(input("Jogador B, escolha: "))

        if jogador_A == jogador_B:
            print("O jogo empatou!")
            empates_modo1 += 1
        elif (jogador_A == 1 and jogador_B == 3) or (jogador_A == 2 and jogador_B == 1) or (jogador_A == 3 and jogador_B == 2):
            print("Vitória do Jogador A!")
            vitorias_jogadorA += 1
        else:
            print("Vitória do Jogador B!")
            vitorias_jogadorB += 1

        total_partidas_modo1 += 1

    # MODO 2: Jogador X Computador
    elif escolha_modo == 2:
        jogador_A = int(input("Jogador, escolha: "))
        computador = randint(1, 3)
        print("Escolha aleatória do computador:", computador)

        if jogador_A == computador:
            print("O jogo empatou!")
            empates_modo2 += 1
        elif (jogador_A == 1 and computador == 3) or (jogador_A == 2 and computador == 1) or (jogador_A == 3 and computador == 2):
            print("Vitória do Jogador!")
            vitorias_jogador += 1
        else:
            print("Vitória do Computador!")
            vitorias_computador += 1

        total_partidas_modo2 += 1

    # MODO 3: Computador X Computador 
    elif escolha_modo == 3:
        computador_A = randint(1,3)
        print("Escolha aleatória do computador:", computador_A)
        computador_B = randint(1,3)
        print("Escolha aleatória do computador:", computador_B)

        if computador_A == computador_B:
            print("O jogo empatou!")
            empates_modo3 += 1
        elif (computador_A == 1 and computador_B == 3) or (computador_A == 2 and computador_B == 1) or (computador_A == 3 and computador_B == 2):
            print("Vitória do Computador A!")
            vitorias_computador_A += 1
        else:
            print("Vitória do Computador B!")
            vitorias_computador_B += 1

        total_partidas_modo3 += 1
        
# ESTATÍSTICAS Modo Jogador X Jogador
if total_partidas_modo1 >= 1:
    total_validas = total_partidas_modo1 - empates_modo1
    if total_validas > 0:
        taxa_vitorias_jogadorA = (vitorias_jogadorA / total_validas) * 100
        taxa_vitorias_jogadorB = (vitorias_jogadorB / total_validas) * 100
    else:
        taxa_vitorias_jogadorA = taxa_vitorias_jogadorB = 0

    print("\nApós", total_partidas_modo1, "partidas no modo Jogador X Jogador:")
    print("Taxa de vitórias do Jogador A:", taxa_vitorias_jogadorA, "%")
    print("Taxa de vitórias do Jogador B:", taxa_vitorias_jogadorB, "%")
    print("Empates:", empates_modo1)

# ESTATÍSTICAS Modo Jogador X Computador
if total_partidas_modo2 >= 1:
    total_validas = total_partidas_modo2 - empates_modo2
    if total_validas > 0:
        taxa_vitorias_jogador = (vitorias_jogador / total_validas) * 100
        taxa_vitorias_computador = (vitorias_computador / total_validas) * 100
    else:
        taxa_vitorias_jogador = taxa_vitorias_computador = 0

    print("\nApós", total_partidas_modo2, "partidas no modo Jogador X Computador:")
    print("Taxa de vitórias do Jogador:", taxa_vitorias_jogador, "%")
    print("Taxa de vitórias do Computador:", taxa_vitorias_computador, "%")
    print("Empates:", empates_modo2)

# ESTATÍSTICAS Modo Computador X Computador

if total_partidas_modo3 >= 1:
    total_validas = total_partidas_modo3 - empates_modo3
    if total_validas > 0:
        taxa_vitorias_computador_A = (vitorias_computador_A / total_validas) * 100
        taxa_vitorias_computador_B = (vitorias_computador_B / total_validas) * 100
    else:
        taxa_vitorias_computador_A = taxa_vitorias_computador_B = 0

    print("\nApós", total_partidas_modo3, "partidas no modo Jogador X Computador:")
    print("Taxa de vitórias do Computador A:", taxa_vitorias_computador_A, "%")
    print("Taxa de vitórias do Computador B:", taxa_vitorias_computador_B, "%")
    print("Empates:", empates_modo3)

print("\n!!! OBRIGADO POR JOGAR !!!")