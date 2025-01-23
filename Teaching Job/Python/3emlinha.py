import pygame
import time
import sys

# função que vai desenhar a area de jogo e chamar as outras funções
def inicio_jogo():
    # music.play()  
    pygame.display.update()
    time.sleep(1)         # dar 1 segundo para o codigo acompanhar 
    ecra.fill(cordefundo) # por o fundo da cor que inserimos lá em baixo

    # desenhar as linhas verticais
    pygame.draw.line(ecra, cordaslinhas, (largura/3, 0), (largura/3, altura), 7)
    pygame.draw.line(ecra, cordaslinhas, (largura/3*2, 0), (largura/3*2, altura), 7)

    # desenhar as linhas horizontais
    pygame.draw.line(ecra, cordaslinhas, (0, altura/3), (largura, altura/3), 7)
    pygame.draw.line(ecra, cordaslinhas, (0, altura/3*2), (largura, altura/3*2), 7)

    estado_do_jogo()

def estado_do_jogo():
    if vencedor is None:
        mensagem = "É a vez do " + XO.upper()  # se não houver vencedor
    else:
        mensagem = "O vencedor é o " + vencedor.upper() # se já houver vencedor
    
    if empate == True:
        mensagem = "O jogo empatou!!"

    # criar a mensagem
    tipo_letra = pygame.font.Font(None, 30)
    texto = tipo_letra.render(mensagem, 1, (255, 255, 255))

    # renderizar a mensagem no jogo
    ecra.fill( (0,0,0) , (0,500,600,100) )
    retangulo_texto = texto.get_rect(center=(largura/2, 550))
    ecra.blit(texto, retangulo_texto)
    pygame.display.update()

def desenhar_jogada(linha, coluna):
    global XO, jogo #permite aceder às variáveis definidas lá em baixo

    if linha == 1:
        posX = 30
    if linha == 2:
        posX = largura/3 + 30
    if linha == 3:
        posX = largura/3* 2 + 30

    if coluna == 1:
        posY = 30
    if coluna == 2:
        posY = altura/3 + 30
    if coluna == 3:
        posY = altura/3*2 + 30

    jogo[linha-1][coluna-1] = XO #inserir o simbolo da jogada na coluna e linha clicada

    if XO == 'x':
        ecra.blit(imagem_x, (posY, posX))
        XO = 'o'
    else:
        ecra.blit(imagem_O, (posY, posX))
        XO = 'x'

def userClick():
    x,y = pygame.mouse.get_pos() # devolver o x e o y do rato no momento do clique

    if (x < largura/3):
        coluna = 1
    elif (x < largura/3 *2):
        coluna = 2
    elif(x < largura):
        coluna = 3
    else:
        coluna = None

    if y < altura/3:
        linha = 1
    elif y < altura/3 *2:
        linha = 2
    elif y < altura:
        linha = 3
    else:
        linha = None

    if(linha and coluna): # se a linha e a coluna tiverem um valor diferente de None
        if (jogo[linha-1][coluna-1] == None): # se o local onde a pessoa clicou não tem valor jogado
            if(vencedor is None):
                desenhar_jogada(linha, coluna)

            verificar_vitoria()
            estado_do_jogo()

def reset_game():
    global jogo, vencedor, empate, XO # variáveis a limpar no reset
    time.sleep(3) # tempo que o reset demora
    XO = 'x'      
    vencedor = None 
    empate = False  
    jogo = [
            [None,None,None],  
            [None,None,None],  
            [None,None,None],  
           ]
    inicio_jogo()

def verificar_vitoria():
    global jogo, vencedor, empate

    #jogo[linhas][colunas]

    # Verificar a vitória nas linhas
    for linha in range(0,3):
        if( jogo[linha][0] == jogo[linha][1] == jogo[linha][2] ):
            if ( jogo[linha][0] is not None ):
                vencedor = jogo[linha][0]
                marcar_vitoria( [[(linha,0), (linha,1), (linha,2)]] )
                break

    # Verificar a vitória nas colunas
    for coluna in range(0,3):
        if( jogo[0][coluna] == jogo[1][coluna] == jogo[2][coluna] ):
            if( jogo[0][coluna] is not None ):
                vencedor = jogo[0][coluna]
                marcar_vitoria( [[(0,coluna), (1,coluna), (2,coluna)]] )
                break
    
    # Verificar a vitória na diagonal da esquerda para a direita
    if(jogo[0][0] == jogo[1][1] == jogo[2][2] ):
        if ( jogo[0][0] is not None ):
            vencedor = jogo[0][0]
            marcar_vitoria( [[(0,0), (1,1), (2,2)]] )


    # Verificar a vitória na diagonal da direita para a esquerda
    if(jogo[0][2] == jogo[1][1] == jogo[2][0] ):
        if ( jogo[0][2] is not None ):
            vencedor = jogo[0][2]
            marcar_vitoria( [[(0,2), (1,1), (2,0)]] )
    
    existem_jogadas_por_fazer = False

    for linha in range(0,3):
        for coluna in range(0,3):
            if( jogo[linha][coluna] is None):
                existem_jogadas_por_fazer = True
    
    ## se não houver um vencedor e o campo estiver todo ocupado
    if(vencedor is None and existem_jogadas_por_fazer == False):
        empate = True


def marcar_vitoria(quadrados):
    for quadrado in quadrados:
        pos_inicial = (quadrado[0][1] * largura / 3 + largura / 6, quadrado[0][0] * altura / 3 + altura / 6)
        pos_final = (quadrado[2][1] * largura / 3 + largura / 6, quadrado[2][0] * altura / 3 + altura / 6)
        pygame.draw.line(ecra, (255, 0, 0), pos_inicial, pos_final, 10)
    pygame.display.update()



#definir algumas variáveis
XO = 'x'        # simbolo da jogada
vencedor = None # vencedor é vazio no inicio do jogo
empate = False  # variável que vai saber se é empate ou não
largura = 500   # largura da janela do jogo
altura = 500    # altura da janela do jogo
cordefundo = (255,255,255)  # cor de fundo da janela de jogo (branca)
cordaslinhas = (10,10,10)   # cor das linhas do jogo (preto)

# este é a lista com listas lá dentro que permite guardar os valores das jogadas
jogo = [
        [None,None,None],  
        [None,None,None],  
        [None,None,None],  
        ]

# iniciar o jogo
pygame.init()
fps = 30        # fps do jogo
relogio = pygame.time.Clock()   # relogio do jogo que permite correr o jogo aos fps inseridos 
ecra = pygame.display.set_mode((largura, altura+100),0, 32) # criação da janela
pygame.display.set_caption("## 3 Em Linha ##")  # nome da janela

#carregar as imagens
imagem_x = pygame.image.load("./imagens/X.png")
imagem_O = pygame.image.load("./imagens/O.png")

#transformar as imagens
imagem_x = pygame.transform.scale(imagem_x, (80,80))
imagem_O = pygame.transform.scale(imagem_O, (80,80))

music = pygame.mixer.Sound('./imagens/music.wav')

inicio_jogo()

while(True):
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        else:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                userClick()
            if evento.type == pygame.KEYDOWN:
                 if evento.key == pygame.K_BACKSPACE: # tecla de apagar
                     reset_game()

    pygame.display.update()
    relogio.tick(fps)