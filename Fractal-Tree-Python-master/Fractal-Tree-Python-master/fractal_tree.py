import turtle

t = turtle.Turtle(shape="classic")
t.penup()# in order to remove the first line it makes
t.setpos((0,-70))#set the starting position
t.lt(90)

lv = 11#13 default
l = 100#120 default
s = 30#17 default

t.width(lv)

t.penup()
t.bk(l)
t.pendown()
t.fd(l)

def draw_tree(l, level):
    width = t.width()  # save the current pen width

    t.width(width * 3.0 / 4.0)  # narrow the pen width

    l = 3.0 / 4.0 * l

    t.lt(s)
    t.fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    t.bk(l)
    t.rt(2 * s)
    t.fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    t.bk(l)
    t.lt(s)

    t.width(width)  # restore the previous pen width

t.speed("fastest")

draw_tree(l, 2)

turtle.done()
