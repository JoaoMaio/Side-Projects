import random  # biblioteca usada para escolher uma palavra ao acaso

def jogo():
        # Lista de jogos
    lista_palavras = ["minecraft",
                      "counter strike",
                      "league of legends",
                      "valorant",
                      "among us",
                      "fortnite",
                      "gta v",
                      "call of duty",
                      "fifa",
                      "overwatch",
                      "apex legends",
                      "rocket league",
                      "pubg",
                      "rainbow six siege",
                      "the witcher",
                      "red dead redemption"
                      ]
    
    palavra = random.choice(lista_palavras) # escolher a palavra ao calhas

    letras_validas = 'abcdefghijklmnopqrstuvwxyz ' # string com todos os caracteres permitidos
    vidas = 10   # numero de vezes que a pessoa pode falhar
    tentativa = '' #string com as letras que a pessoa usou

    while True:  # estar sempre a executar
        desenho_palavra = ""

        # Desenhar a tentativa da pessoa
        for letra in palavra:       # Por cada letra na palavra escolhida pelo computador
            if letra in tentativa:  # Se a letra estiver na string com as tentivas da pessoa (se a pessoa acertar)
                desenho_palavra = desenho_palavra + letra
            else:
                desenho_palavra = desenho_palavra + "_ "

        # Se a pessoa acertou a palavra completa
        if palavra == desenho_palavra:
            print("------------------------------------------")
            print("You win!")
            print("A palavra é:", palavra)
            break
        ##########################################################################

        print("Adivinhe a palavra: ", desenho_palavra) # Adivinhe a palavra : _ _ _ _ a _ s
        letra_inserida = input("insira uma letra: ")
        letra_inserida = letra_inserida.lower() # transformar para minuscula para depois fazer as verificações


         # letra_inserida está letras_validas e letra_inserida não está tentativa
        if letra_inserida in letras_validas and letra_inserida not in tentativa:
            tentativa = tentativa + letra_inserida 
        else:
            letra_inserida = input("insira uma letra válida!")
 
        # se a letra_inserida não estiver na palavra
        if letra_inserida not in palavra:
            vidas = vidas - 1

        match vidas :
            case 9:
                print("9 vidas restantes")
                print("  --------  ")
            case 8:
                print("8 vidas restantes")
                print("  ---------  ")
                print("      O      ")
            case 7:
                print("7 vidas restantes")
                print("  ---------  ")
                print("      O      ")
                print("      |      ")
            case 6:
                print("6 vidas restantes")
                print("  ---------  ")
                print("      O      ")
                print("      |      ")
                print("     /       ")
            case 5:
                print("5 vidas restantes")
                print("  ---------  ")
                print("      O      ")
                print("      |      ")
                print("     / \     ")
            case 4:
                print("4 vidas restantes")
                print("  ---------  ")
                print("      O      ")
                print("    / |      ")
                print("     / \     ")
            case 3:
                print("3 vidas restantes")
                print("  ---------  ")
                print("      O      ")
                print("    / | \    ")
                print("     / \     ")
            case 2:
                print("2 vidas restantes")
                print("  ---------  ")
                print("      O  |   ")
                print("    / | \    ")
                print("     / \     ")
            case 1:
                print("1 vidas restantes")
                print("  ---------  ")
                print("    \ O_|/   ")
                print("      |      ")
                print("     / \     ")
            case 0:
                print("You lose")
                print("  ---------  ")
                print("      O_|    ")
                print("     /|\     ")
                print("     / \     ")
                break
        print("============================================")
        print("============================================")

print("============================")
print("Tenta adivinhar a palavra em menos de 10 tentativas")
jogo()