print("\n")
print("!!!BEM VINDO AO JOKENPO!!!")
print("\n")
print("DIGITE 1 PARA ESCOLHER PEDRA")
print("DIGITE 2 PARA ESCOLHER PAPEL")
print("DIGITE 3 PARA ESCOLHER TESOURA")
print("\n")


from random import randint

comecar_jogo = int(input("Você quer começar um novo jogo? Se sim digite 1, se não digite 0:  "))

while comecar_jogo == 0 :
    break 

while comecar_jogo == 1 :
    jogador_A = int(input("Faça sua escolha entre pedra, papel ou tesoura!   "))
    computador = randint(1,3)
    print ("Escolha aleatória do computador: ", computador)

    if jogador_A == computador :
        print("O jogo empatou!")
    elif (jogador_A == 1 and computador == 3) or (jogador_A == 2 and computador == 1) or (jogador_A == 3 and computador == 2):
        print("Vitória jogador A")
    else:
        print("Vitória computador")
    comecar_jogo = int(input("Você quer começar um novo jogo? Se sim digite 1, se não digite 0:  "))



