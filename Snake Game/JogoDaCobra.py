import turtle, time, random

delay = 0.1
pontos = 0

#ecra
wn = turtle.Screen()
wn.title('Minhoca xD Made By Ninguém')
wn.bgcolor("#33cc33")
wn.setup(width=600, height=600)
wn.tracer(0) 

borda = turtle.Turtle()
borda.speed(5)
borda.pensize(2)
borda.penup()
borda.goto(-300,-300)#canto esquerdo
borda.pendown()
borda.color("black")

for d in range(4):
    borda.forward(600)
    borda.left(90)
borda.penup()
borda.hideturtle()

#TEXTO
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("Black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: {}".format(pontos), align="center", font=("courier", 24, "bold"))

#CABEÇA
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("#087323")
head.penup()
head.goto(0,0)
head.direction = "stop"

#COMIDA
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("#ff5050")
comida.penup()
comida.goto(0,100)

#CORPO
parte = []

#FUNÇÕES DO MOVIMENTO
def direita():
    if head.direction != "left":
        head.direction = "right"
def esquerda():
    if head.direction != "right":
        head.direction = "left"
def cima():
    if head.direction != "down":
        head.direction = "up"
def baixo():
    if head.direction != "up":
        head.direction = "down"

def movimento():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+10)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-10)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-10)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+10)    

wn.listen()
wn.onkeypress(cima, "w")
wn.onkeypress(baixo, "s")
wn.onkeypress(direita, "d")
wn.onkeypress(esquerda, "a")

#############################Sempre a correr o código############################################
while True:
    wn.update()
############################################COLISOES##############################################
    if head.xcor()>280 or head.ycor()<-280 or head.xcor()<-280 or head.ycor()>280:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            for nova_parte in parte:
                nova_parte.goto(1000, 1000)
            
            parte.clear()
            delay = 0.1
            pontos = 0
            pen.clear()
            pen.write("Score: {}".format(pontos), align="center", font=("courier", 24, "bold"))

    for nova_parte in parte:
        if nova_parte.distance(head) < 10:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            
            for nova_parte in parte:
                nova_parte.goto(1000, 1000)
            
            parte.clear()
            delay = 0.1
            pontos = 0
            pen.clear()
            pen.write("Score: {}".format(pontos), align="center", font=("courier", 24, "bold"))
 ###############################################################################################   

    if head.distance(comida) < 25:
        x = random.randint(-280, 280)
        y = random.randint(-280, 260)
        comida.goto(x,y)
        delay -= 0.002
        pontos += 1
        pen.clear()
        pen.write("Score: {}".format(pontos), align="center", font=("courier", 24, "bold"))
        nova_parte = turtle.Turtle()
        nova_parte.speed(0)
        nova_parte.shape("square")
        nova_parte.color("#045418")
        nova_parte.penup()
        parte.append(nova_parte)

    for i in range(len(parte)-1, 0, -1):
        x = parte[i-1].xcor()
        y = parte[i-1].ycor()
        parte[i].goto(x,y)

    #mover a parte 0 para onde a cabeça está
    if len(parte) > 0:
        x = head.xcor()
        y = head.ycor()
        parte[0].goto(x,y)

    movimento()
    time.sleep(delay)

wn.mainloop()
