# -*- coding: utf-8 -*-
from turtle import hideturtle, speed, penup, goto, pendown, fillcolor, begin_fill, forward, right, end_fill, pencolor, \
    showturtle, shape, title


class MazeCanvas:
    fill_color_map = {0: '', 1: 'black', 2: 'red'}

    @staticmethod
    def draw_maze(maze: list):
        title('Maze Algorithm')
        hideturtle()
        speed('fastest')
        penup()

        # Default position is 0,0 but is center, move -300, 300
        goto(-300, 300)
        pendown()

        # Maze size is 12
        for y in range(12):
            for x in range(12):
                # If set fill color using color map
                fill_color = MazeCanvas.fill_color_map[maze[y][x]]

                if fill_color != '':
                    # Draw square
                    fillcolor(fill_color)
                    begin_fill()
                    for i in range(4):
                        forward(50)
                        right(90)
                    end_fill()

                # Move forward
                penup()
                forward(50)
                pendown()

            # Go start position
            penup()
            goto(-300, 300 - (y + 1) * 50)
            pendown()

    @staticmethod
    def move_character(move_list: list):
        speed('slow')
        penup()
        pencolor('red')

        # Move -225 + (50 * (x position)), 225 - (50 * (y position)) using move_list
        goto(-225 + (50 * (move_list[0][1] - 1)), 225 - (50 * (move_list[0][0] - 1)))
        showturtle()
        # Character is circled
        shape('circle')
        pendown()

        # Draw character use move list
        for move_y, move_x in move_list:
            goto(-225 + (50 * (move_x - 1)), 225 - (50 * (move_y - 1)))
