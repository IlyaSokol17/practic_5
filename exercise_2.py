import turtle
def main():
    xc, yc = map(int, input('введите координаты центра окружности ').split())
    r = int(input('введите радиус окружности '))
    x, y = map(int, input('введите координаты точки ').split())
    turtle.up()
    turtle.width(5)
    turtle.pencolor('black')
    turtle.setposition(xc, yc)
    turtle.down()
    turtle.circle(r)
    yc += r
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.dot(5, "red")
    d = (((xc - x) ** 2 )+ ((yc - y) ** 2)) ** 0.5
    print(d)
    turtle.up()
    turtle.goto(xc - r, (yc - (2 * r)))
    turtle.down()
    turtle.pencolor('red')
    if r  > d :
        turtle.write('Точка внутри окружности', move=False, align="left", font=("Arial", 17, "normal"))
    if r  < d:
        turtle.write('Точка вне окружности', move=False, align="left", font=("Arial", 17, "normal"))


    turtle.done()


main()