import turtle, time, math

turtle.pensize(3)
turtle.hideturtle()
turtle.tracer(False)

def base():
    turtle.penup()
    turtle.home()
    turtle.pendown()
    turtle.backward(200)
    turtle.goto(0, 0)
    #  画出虚线
    for i in range(10):
        turtle.penup()
        turtle.forward(7)
        turtle.pendown()
        turtle.forward(13)

def mode_left():
    global angle
    left_angle = 0
    while angle:
        left_angle += 1
        turtle.clear()
        base()
        turtle.left(left_angle)
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.forward(200)
        angle -= 1

        turtle.home()
        turtle.penup()
        turtle.goto(40, 0)
        turtle.left(90)
        turtle.pendown()
        turtle.circle(40, left_angle)

        turtle.penup()
        x = 60 * math.cos(3.1415926 / 360 * left_angle)
        y = 60 * math.sin(3.1415926 / 360 * left_angle)
        turtle.goto(x, y)
        turtle.pendown()
        turtle.write("{}°这是我们转过的角度".format(left_angle), font=("Arial", 20, "normal"))

        turtle.penup()
        turtle.home()
        turtle.goto(-60, 0)
        turtle.right(90)
        turtle.pendown()
        turtle.circle(60, left_angle - 180)

        turtle.penup()
        x = -100 * math.cos(3.1415926 / 360 * (left_angle - 180))
        y = -100 * math.sin(3.1415926 / 360 * (left_angle - 180))
        turtle.goto(x, y)
        turtle.pendown()
        turtle.write("180-{}={}°".format(left_angle, 180 - left_angle), font=("Arial", 20, "normal"))

        time.sleep(0.1)
        turtle.update()
    turtle.ontimer(mode_left, 1000)

def mode_right():
    global angle
    right_angle = 0
    while angle:
        right_angle += 1
        turtle.clear()
        base()
        turtle.right(right_angle)
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.forward(200)
        angle -= 1

        turtle.penup()
        turtle.home()
        turtle.goto(40, 0)
        turtle.left(90)
        turtle.pendown()
        turtle.circle(40, -right_angle)

        turtle.penup()
        turtle.home()
        turtle.goto(-60, 0)
        turtle.right(90)
        turtle.pendown()
        turtle.circle(60, 180 - right_angle)

        turtle.penup()
        x = -100 * math.cos(3.1415926 / 360 * (180 - right_angle))
        y = -100 * math.sin(3.1415926 / 360 * (180 - right_angle))
        turtle.goto(x, y)
        turtle.pendown()
        turtle.write("180-{}={}°".format(right_angle, 180 - right_angle), font=("Arial", 20, "normal"))

        turtle.penup()
        x = 60 * math.cos(3.1415926 / 360 * right_angle)
        y = -60 * math.sin(3.1415926 / 360 * right_angle)
        turtle.goto(x, y)
        turtle.pendown()
        turtle.write("{}°这是我们转过的角度".format(right_angle), font=("Arial", 20, "normal"))

        time.sleep(0.1)

        turtle.update()
    turtle.ontimer(mode_right, 10)

your_code = input("请输入你的代码")
if "left" in your_code:
    angle_string = ""
    for i in your_code:
        if i in "1234567890":
            angle_string = angle_string + i
    angle = int(angle_string)
    mode_left()
elif "right" in your_code:
    angle_string = ""
    for i in your_code:
        if i in "1234567890":
            angle_string = angle_string + i
    angle = int(angle_string)
    mode_right()
else:
    print("你的输入错误了，重新运行程序，少侠请重新来过")

turtle.done()