# pip install random-word
"""
from random_word import RandomWords
r = RandomWords()

r.get_random_word()
"""
import random

def hangman():
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
    palavra = random.choice(lista_palavras)
    
    letras_validas = 'abcdefghijklmnopqrstuvwxyz '
    vidas = 10
    tentativa = ''

    while len(palavra) > 0:
        desenho_palavra = ""

        for letra in palavra:       # Por cada letra na palavra escolhida
            if letra in tentativa:  # se a letra estiver na tentativa
                if letra == " ":
                    desenho_palavra = desenho_palavra + " "
                else:
                    desenho_palavra = desenho_palavra + letra
            else:
                desenho_palavra = desenho_palavra + "_ "

        # Se a palavra estiver correta
        if desenho_palavra == palavra:
            print("------------------------------------------")
            print("You win!")
            print("A palavra é:", palavra)
            break

        print("Adivinha a palavra:", desenho_palavra)
        letra = input().lower()

        if letra in letras_validas and letra not in tentativa:
            tentativa = tentativa + letra
        else:
            print("Enter a valid character")
            letra = input()

        if letra not in palavra:
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


name = input("Insere o teu nome: ")
print(f"Seja Bem vindo {name}")
print("============================")
print("Tenta adivinhar a palavra em menos de 10 tentativas")
hangman()