from Recaman_sequence import sequence_recaman
import turtle


SHAPE_X = 1400
SHAPE_Y = 800
START_POSITION_Y = 0
START_POSITION_X = -670
ANGLE = 180
ANGLE_FORWARD = 270
ANGLE_BACKWARD = 90
SCALE = 2


def main(iters: int) -> None:

    window = turtle.Screen()
    window.setup(SHAPE_X, SHAPE_Y)
    window.bgcolor('black')
    window.title('Визуализация последовательности Рекамана')

    pen = turtle.Turtle()
    pen.setposition(START_POSITION_X, START_POSITION_Y)
    pen.hideturtle()
    pen.color('white')
    pen.speed('fastest')

    window.screensize(SHAPE_X // 2, SHAPE_Y // 2)

    previous_number = 0
    step = 1
    for number in sequence_recaman():
        radius = abs(number - previous_number) * SCALE
        if step == iters:
            break
        if number - previous_number > 0:  # направление вправо, при увеличении нового числа
            pen.setheading(ANGLE_FORWARD)
            pen.circle(radius, ANGLE)
        else:  # направление влево, при уменьшении нового числа
            pen.setheading(ANGLE_BACKWARD)
            pen.circle(radius, ANGLE)
        previous_number = number
        step += 1

    turtle.done()


if __name__ == '__main__':
    main(120)
