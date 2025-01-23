from tkinter import *
import random

# VARIAVEIS GLOBAIS
LARGURA = 500
ALTURA = 500
CORDEFUNDO = "#000000" # cor preta
SPEED = 200

TAMANHO_QUADRADO = 20
CORDACOBRA = "#00FF00"  # verde
CORDACOMIDA = "#FF0000" # vermelho

direcao_global = "baixo"
pontos = 0


# classe cobra
class Cobra:
    # metodo de inicialização do objeto
    def __init__(self):
        self.tamanho_corpo = 2
        self.coordenadas = []
        self.partes_corpo = []

        #Inicializar o corpo da cobra
        for i in range(0, 2):
            self.coordenadas.append([0,0]) #as duas partes do corpo começam no 0,0
        

        for x, y in self.coordenadas:
            quadrado = areaDeJogo.create_rectangle(x, y, x+TAMANHO_QUADRADO, y+TAMANHO_QUADRADO, fill=CORDACOBRA, tag="cobra")
            self.partes_corpo.append(quadrado)

class Comida:

    def __init__(self):
        # posicoes random da comida
        x = random.randint(0, (int)(LARGURA / TAMANHO_QUADRADO) - 1) * TAMANHO_QUADRADO
        y = random.randint(0, (int)(ALTURA / TAMANHO_QUADRADO) - 1)  * TAMANHO_QUADRADO

        self.coordenadas = [x,y]

        areaDeJogo.create_oval(x, y, x+TAMANHO_QUADRADO, y+TAMANHO_QUADRADO, fill=CORDACOMIDA, tag="comida")

def mudar_de_direcao(nova_direcao):
    global direcao_global

    # se a pessoa quer ir para a esquerda, e não estiver a andar para a direita (nao pode mudar completamente de direção)
    if(nova_direcao == "esquerda" and direcao_global != "direita"):
        direcao_global = nova_direcao

    elif(nova_direcao == "direita" and direcao_global != "esquerda"):
        direcao_global = nova_direcao

    elif(nova_direcao == "cima" and direcao_global != "baixo"):
        direcao_global = nova_direcao

    elif(nova_direcao == "baixo" and direcao_global != "cima"):
        direcao_global = nova_direcao


def movimento(cobra, comida):
    global direcao_global
    global pontos

    #obter as coordenadas da cabeça da cobra
    x, y = cobra.coordenadas[0] # primeiro elemento
    
    if direcao_global == "cima":
        y = y - TAMANHO_QUADRADO
    elif direcao_global == "baixo":
        y = y + TAMANHO_QUADRADO
    elif direcao_global == "esquerda":
        x = x - TAMANHO_QUADRADO
    elif direcao_global == "direita":
        x = x + TAMANHO_QUADRADO

    # atualizar as coordenadas da cobra (ou seja adicionar no inicio da lista a nova coordenada da cabeça)
    cobra.coordenadas.insert(0,(x, y))

    # criar o novo quadrado da cobra
    novo_quadrado = areaDeJogo.create_rectangle(x, y, x+TAMANHO_QUADRADO, y+TAMANHO_QUADRADO, fill=CORDACOBRA)

    # adicionar à lista de partes do corpo esse quadrado
    cobra.partes_corpo.insert(0, novo_quadrado)

    #Ver se a cobra comeu a comida
    # Ver se as coordenadas da cabeça da cobra estão nas mesmas coordenadas da comida
    if x == comida.coordenadas[0] and y == comida.coordenadas[1]:
        pontos = pontos + 1
        texto.config(text="Pontos: {}".format(pontos)) #atualizar o texto com os pontos
        areaDeJogo.delete("comida") # eliminar a comida do ecra
        comida = Comida()           # criar uma nova comida
    else:
        del cobra.coordenadas[-1]  # eliminar o ultimo elemento da lista
        areaDeJogo.delete(cobra.partes_corpo[-1]) #eliminar do ecra a ultima parte do corpo da cobra
        del cobra.partes_corpo[-1] # eliminar da lista a ultima parte de corpo

    # se o resultado da função é Verdade
    if detetarColisoes(cobra):
        print("Jogo Terminou")
        print("Acabou o jogo com ", pontos, " pontos")
        areaDeJogo.delete(ALL)
        janela.destroy()
    else:
        janela.after(SPEED, movimento, cobra, comida) # chamar a funçao movimento a cada 200milisegundos


#devolve verdadeiro ou falso consoante se a cobra bateu ou não
def detetarColisoes(cobra):

    # coordenadas da cabeça da cobra
    x,y = cobra.coordenadas[0]

    # detetar se a cobra bateu na janela
    if x < 0 or x >= LARGURA:
        return True
    elif y < 0 or y >= ALTURA:
        return True
    
    # detetar se bateu em alguma parte do corpo
    for parte in cobra.coordenadas[1:]:
        if x == parte[0] and y == parte[1]:
            return True
    

    return False
    
    
janela = Tk()
janela.title("Jogo Da Cobra") # Mudar o nome da janela

texto = Label(janela, text="Pontos: {}".format(pontos))
texto.pack()

areaDeJogo = Canvas(janela, bg=CORDEFUNDO, height=ALTURA, width=LARGURA)
areaDeJogo.pack()

# associar o movimento com as teclas das setas
janela.bind('<Left>', lambda event: mudar_de_direcao("esquerda"))
janela.bind('<Right>', lambda event: mudar_de_direcao("direita"))
janela.bind('<Up>', lambda event: mudar_de_direcao("cima"))
janela.bind('<Down>', lambda event: mudar_de_direcao("baixo"))

cobra = Cobra()
comida = Comida()

movimento(cobra, comida)

janela.update()
janela.mainloop() # correr a janela para sempre