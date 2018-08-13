import turtle


def main():
    window =turtle.Screen()
    dave = turtle.Turtle()

    make_rectangle(dave)
    turtle.mainloop()

def make_rectangle(dave):
    length =int(input('Tamaño del cuadrado: '))

    for i in range(4):
        make_line_and_turn(dave, length)

def make_line_and_turn(dave, length):
    dave.forward(length)
    dave.left(90)



if __name__ == '__main__':
    main()
