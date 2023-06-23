import turtle

def dibujar_balon():
    turtle.bgcolor("white")
    turtle.speed(3)
    turtle.pensize(3)

    # Dibujar el pentgono central
    turtle.penup()
    turtle.goto(0, -100)
    turtle.pendown()
    turtle.circle(100)

    # Dibujar los hexgonos y pentgonos alrededor del pentono central
    for _ in range(6):
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.circle(200, 60)
        turtle.circle(200, -60)

    turtle.done()

# Llamar a la funcin para dibujar el baln
dibujar_balon()
