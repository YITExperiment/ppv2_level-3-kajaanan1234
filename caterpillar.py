import random
import turtle as t
t.bgcolor('yellow')

caterpillar = t.Turtle()
caterpillar.shape('square')
caterpillar.color('red')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()
leaf = t.Turtle()
leaf_shape = ((0, 0), (14, 2), (18, 6), (20, 20), \
(6, 18), (2, 14))
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed(0)
def outside_window():
    pass
def game_over():
    pass
def display_score(current_soore):
    pass
def place_leaf():
    pass

def start_game():
    global game_stared
    if game_stared:
        return
    game_stared = True

    score = 0
    text_turtle.clear()

    caterpillar_speed = 2
    caterpillar_lenth = 3
    caterpillar.shapesize(1, caterpillar_lenth, 1)
    caterpillar.showturtle()
    display_score(score)
    place_leaf()
while True:
    caterpillar.forward(caterpillar_speed)
    if  caterpillar.distance(leaf) < 20:
        place_leaf()
        caterpillar_lenth = caterpillar_lenth + 1
        caterpillar.shapesize(1, catpillar_lenth, 1)
        caterpillar_speed = caterpillar_speed + 1
        score = score + 10
        display_score(score)
    if outside_window():
        game_over()
        break
def move_up():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(90)

def move_down():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(270)

def move_left():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(180)

def move_right():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading

t.onkey(start_game,'space')
t.onkey(move_up,'Up')
t.onkey(move_right,'Right')
t.onkey(move_down,'Down')
t.onkey(move_left,'Left')
t.listen()
t.mainloop()
t.onkey(start_game, 'space')
t.listen()
t.mainloop()
def outside_window():
    left_wall = -t.window_width()/2
    right_wall = -t.window_width()/2
    top_wall = t.window_height()/2
    bottom_wall = -t.window_height()/2
    (x.y) = catpillar.pos()
    outside = x < left_wall or x > right_wall or y < bottom_wall or y > top_wall
    return outside
def game_over():
    catpillar.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('GAME_OVER!',align='center' , font=('Aerial',30,'normal'))
def display_score(current_score):
    score_turtle.clear()
    score_turtle.clear()
    x = (t.window_width() / 2)-50
    y = (t.window_height() /2)-50
    score_turtle.setpos(x,y)
    score_turtle.write(str(current_score) , align = 'right',font=('Arial',40,'bold'))
def place_leaf():
    leaf.hideturtle()
    leaf.setx(rd.randint(-200,200))
    leaf.sety(rd.randint(-200,200))
    leaf.showturtle()

    
    
    
