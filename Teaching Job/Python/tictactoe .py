import pygame as pg,sys
from pygame.locals import *
import time

def game_opening():
    screen.blit(opening,(0,0))  #draw opening image
    pg.display.update()
    time.sleep(1)
    screen.fill(white)

    # Drawing vertical lines
    pg.draw.line(screen,line_color,(width/3,0),(width/3, height),7)
    pg.draw.line(screen,line_color,(width/3*2,0),(width/3*2, height),7)
    # Drawing horizontal lines
    pg.draw.line(screen,line_color,(0,height/3),(width, height/3),7)
    pg.draw.line(screen,line_color,(0,height/3*2),(width, height/3*2),7)
    draw_status()


def draw_status():
    global draw

    if winner is None:
        message = XO.upper() + "'s Turn"
    else:
        message = winner.upper() + " won!"
    if draw:
        message = 'Game Draw!'

    font = pg.font.Font(None, 30)
    text = font.render(message, 1, (255, 255, 255))

    # copy the rendered message onto the board
    screen.fill ((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width/2, 500-50))
    screen.blit(text, text_rect)
    pg.display.update()


def check_win():
    global TTT, winner,draw

    # TTT[Rows][Columns]


    # check for winning rows
    for row in range (0,3):
        if (TTT[row][0] == TTT[row][1] == TTT[row][2]):
            if TTT [row][0] is not None:
                winner = TTT[row][0] 
                break

    # check for winning columns
    for col in range (0, 3):
        if (TTT[0][col] == TTT[1][col] == TTT[2][col]):
            if TTT[0][col] is not None:
                winner = TTT[0][col]
                break

    # check for diagonal winners
    if (TTT[0][0] == TTT[1][1] == TTT[2][2]):       # linha 0 coluna 0, linha 1 coluna 1, linha 2 coluna 2
        if TTT[0][0] is not None:
            winner = TTT[0][0]

    # game won diagonally right to left
    if (TTT[0][2] == TTT[1][1] == TTT[2][0]):       # linha 0 coluna 2, linha 1 coluna 1, linha 2 coluna 0
        if TTT[0][2] is not None: 
            winner = TTT[0][2]


    if(all([all(row) for row in TTT])):
        if winner is None:
            draw = True  #empate

    draw_status()


def drawXO(row,col):
    global TTT,XO
    if row==1:
        posx = 30
    if row==2:
        posx = width/3 + 30
    if row==3:
        posx = width/3*2 + 30

    if col==1:
        posy = 30
    if col==2:
        posy = height/3 + 30
    if col==3:
        posy = height/3*2 + 30
    TTT[row-1][col-1] = XO
    if(XO == 'x'):
        screen.blit(x_img,(posy,posx))
        XO= 'o'
    else:
        screen.blit(o_img,(posy,posx))
        XO= 'x'
    pg.display.update()


def userClick():
    #get coordinates of mouse click
    x,y = pg.mouse.get_pos()

    #get column of mouse click (1-3)
    if(x < width/3):
        col = 1
    elif (x<width/3*2):
        col = 2
    elif(x<width):
        col = 3
    else:
        col = None

    #get row of mouse click (1-3)
    if(y<height/3):
        row = 1
    elif (y<height/3*2):
        row = 2
    elif(y<height):
        row = 3
    else:
        row = None

    if(row and col and TTT[row-1][col-1] is None):
        #draw the x or o on screen
        drawXO(row,col)
        check_win()


def reset_game():
    global TTT, winner,XO, draw
    time.sleep(3)
    XO = 'x'
    draw = False
    game_opening()
    winner=None
    TTT = [[None]*3,[None]*3,[None]*3]

#create a fun
# def highlight_winner(cells):
#     for cell in cells:
#         start_pos = (cell[0][1] * largura / 3 + largura / 6, cell[0][0] * altura / 3 + altura / 6)
#         end_pos = (cell[2][1] * largura / 3 + largura / 6, cell[2][0] * altura / 3 + altura / 6)
#         pygame.draw.line(ecra, (255, 0, 0), start_pos, end_pos, 10)
#     pygame.display.update()

#                 highlight_winner([[(linha, 0), (linha, 1), (linha, 2)]])

# move_sound = pygame.mixer.Sound('./music.wav')



#initialize global variables
XO = 'x'
winner = None
draw = False
width = 400
height = 400
white = (255, 255, 255)
line_color = (10,10,10)

#TicTacToe 3x3 board
TTT = [[None]*3,
       [None]*3,
       [None]*3]

pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height+100),0,32)
pg.display.set_caption("Tic Tac Toe")

#loading the images
opening = pg.image.load('./imagens/tic tac opening.png')
x_img = pg.image.load('./imagens/x.png')
o_img = pg.image.load('./imagens/o.png')

#resizing images
x_img = pg.transform.scale(x_img, (80,80))
o_img = pg.transform.scale(o_img, (80,80))
opening = pg.transform.scale(opening, (width, height+100))
move_sound = pg.mixer.Sound('./music.wav')


game_opening()
# run the game loop forever
while(True):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            userClick()
            if(winner or draw):
                reset_game()
    pg.display.update()
    CLOCK.tick(fps)
    
