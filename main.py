import turtle as trt
import ru_local as RU
import math


def get_num_hexagons() -> int:
    """
    Prompt the user to enter the number of hexagons per side.

    Returns:
        int: The number of hexagons per side (between 4 and 20).
    """
    while True:
        try:
            data = int(input(RU.ENTER_NUMBER))
            if 4 <= data <= 20:
                return data
            else:
                print(RU.RETRY_ENTER_NUMBER)
        except ValueError:
            print(RU.RETRY_ENTER_NUMBER)


def get_color_choice() -> str:
    """
    Prompt the user to select a color from the available options.

    Returns:
        str: The hex code of the selected color.
    """
    colors = {
        '1': '#7FFFD4',
        '2': '#87CEEB',
        '3': '#5F9EA0',
        '4': '#7FFF00',
        '5': '#6495ED',
        '6': '#9932CC',
        '7': '#00FFFF'
    }
    print(RU.AVAILABLE_COLORS)
    print(
        f'1 - {RU.AQUAMARINE}, 2 - {RU.SKY_BLUE}, 3 - {RU.CADET_BLUE},'
        f'4 - {RU.CHARTREUSE},5 - {RU.CORNFLOWERBLUE}, 6 - {RU.DARKORCHID},'
        f'7 - {RU.CYAN}'
    )

    while True:
        color = input(RU.ENTER_COLOR)
        if color in colors:
            return colors[color]
        else:
            print(RU.RETRY_ENTER_COLOR)


def draw_hexagon(x, y, side_len, color) -> None:
    """
    Draw a filled hexagon at the specified position.

    Args:
        x (float): The x-coordinate of the starting position.
        y (float): The y-coordinate of the starting position.
        side_len (float): The length of each side of the hexagon.
        color (str): The fill color of the hexagon in hex format.
    """
    trt.penup()
    trt.goto(x, y)
    trt.pendown()
    trt.fillcolor(color)
    trt.begin_fill()
    trt.setheading(90)
    for _ in range(6):
        trt.forward(side_len)
        trt.right(60)
    trt.end_fill()


def main() -> None:
    """Main function to set up the turtle screen and draw the hexagon grid."""
    screen = trt.Screen()
    screen.screensize(500, 500)
    screen.tracer(0)
    trt.speed(0)
    trt.hideturtle()

    print(RU.ENTER_FIRST_COLOR)
    color_1 = get_color_choice()
    print(RU.ENTER_SECOND_COLOR)
    color_2 = get_color_choice()

    num_hexagons = get_num_hexagons()
    side_len = 450 / (num_hexagons * math.sqrt(3))
    horizontal_spacing = side_len * math.sqrt(3)
    vertical_spacing = side_len * 1.5

    start_x = -250
    start_y = 250

    for row in range(num_hexagons):
        for col in range(num_hexagons):
            current_color = color_1 if col % 2 == 0 else color_2
            position_x = start_x + col * horizontal_spacing
            position_y = start_y - row * vertical_spacing

            if row % 2 != 0:
                position_x += horizontal_spacing / 2

            draw_hexagon(position_x, position_y, side_len, current_color)

    screen.update()
    screen.mainloop()


if __name__ == '__main__':
    main()
