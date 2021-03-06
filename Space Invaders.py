#Space Invaders

import turtle
import winsound
import math
import random
import platform

#Setup Up the Screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders By LuciferOT23")
wn.bgpic("assets/Space.png")
wn.tracer(0)

#Register the shapes
wn.register_shape("assets/invader.gif")
wn.register_shape("assets/player.gif")

#Draw Border
border_pen=turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Set the score to 0
score = 0
#Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,275)
scorestring = "Score: {}".format(score)
score_pen.write(scorestring, False, align ="left", font=("Arial",14,"normal"))
score_pen.hideturtle()


#Create the player turtle
player=turtle.Turtle()
player.color("blue")
player.shape("assets/player.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)
player.speed = 0


#Choose Number of enemies
number_of_enemies = 30
#Create an empty list of enemies
enemies = []
#Add enemies to the list
for i in range(number_of_enemies):
    #Create the enemy
    enemies.append(turtle.Turtle())

enemy_start_x = -225
enemy_start_y = 250
enemy_number = 0

for enemy in enemies:
    enemy.color("red")
    enemy.shape("assets/invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = enemy_start_x + (50 * enemy_number)
    y = enemy_start_y
    enemy.setposition(x,y)
    #Update the enemy number
    enemy_number += 1
    if enemy_number == 10:
        enemy_start_y -= 50
        enemy_number = 0

enemyspeed = 0.2


#Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 7

#Define bullet state
#Ready - ready to fire
#Fire - bullet is firing
bulletstate = "ready"
 

#Functions
def move_left():                    #Move the player left
    player.speed = -3
    
def move_right():                   #Move the player right
    player.speed = 3

def move_player():
    x = player.xcor()
    x += player.speed 
    if x < -280 :
        x = -280
    if x > 280 :
        x = 280
    player.setx(x)

def fire_bullet():
    #Declare bulletstate as a global if it needs changed
    global bulletstate
    if bulletstate == "ready":
        winsound.PlaySound("assets/laser.wav",winsound.SND_ASYNC)
        bulletstate = "fire"
        #Move the bullet to the just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False


#Keyboard Bindings
wn.listen()
wn.onkeypress(move_left,"Left")
wn.onkeypress(move_right,"Right")
wn.onkeypress(fire_bullet,"space")

#Play background
winsound.PlaySound("assets/bg.wav",winsound.SND_ASYNC)

#Main Game loop
while True:
    wn.update()
    move_player()

    for enemy in enemies:
        #Move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #Move the enemy back and down
        if enemy.xcor() > 280:
            #Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #Change enemy direction
            enemyspeed *= -1

        if enemy.xcor() < -280:
            #Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #Change enemy direction
            enemyspeed *= -1

        #Check for a collision between the bullet and the enemy
        if isCollision(bullet, enemy):
            winsound.PlaySound("assets/explosion.wav",winsound.SND_ASYNC)
            #Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0,-400)
            #reset the enemy
            enemy.setposition(0,10000)
            #Update the score
            score += 10
            scorestring = "Score: {}".format(score)
            score_pen.clear()
            score_pen.write(scorestring, False, align ="left", font=("Arial",14,"normal"))

        if isCollision(player, enemy):
            winsound.PlaySound("assets/explosion.wav",winsound.SND_ASYNC)
            player.hideturtle() 
            enemy.hideturtle()
            print("Game Over")
            break


    #Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #Check to see if bullet has reached the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

    #Check for a collision between the bullet and the enemy
    if isCollision(bullet, enemy):
        #Reset the bullet
        bullet.hideturtle()
        bulletstate = "ready"
        bullet.setposition(0,-400)
        #reset the enemy
        enemy.setposition(-200,250)

    if isCollision(player, enemy):
        player.hideturtle()
        enemy.hideturtle()
        print("Game Over")
        break




