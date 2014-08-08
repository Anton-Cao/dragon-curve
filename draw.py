def draw(fileName):
    import turtle
    screen = turtle.Screen()
    obj = turtle.Turtle()

    
    
    file = open(fileName, 'r')

    for line in file:
        for digit in line:
            if digit != ' ' and digit != '\n':
                obj.forward(1)
            if int(digit)%2==0:
                obj.left(90)
            else:
                obj.right(90)
                
    file.close()
    screen.mainloop()
