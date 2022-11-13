# -*- coding: utf-8 -*-

from maze import MazeGenerator
from maze import MazeExplorer
from gui import MazeCanvas

import turtle


def main():
    # Input maze level from user(only input 1 ~ 4, add validation input)
    while True:
        try:
            level = int(input('Input maze level(1: easy, 2: normal, 3: difficult 4: exit : '))
            if 0 < level < 5:
                break
        except ValueError:
            pass
        print('Wrong input... retry again')

    if level == 4:
        exit(0)

    # Until a maze is created at an appropriate level
    # Check move_list size
    # 4 ~ 6 -> easy
    # 9 ~ 12 -> normal
    # 21 ~ -> difficult
    print('Create maze...')
    is_leveling_maze_created = False
    maze = []
    answer_pos_list = []
    size = -1
    while not is_leveling_maze_created:
        maze = MazeGenerator.create_maze()
        max_distance = MazeExplorer.get_max_distance(maze)
        answer_pos_list, size = MazeExplorer.get_answer_pos_list(maze, max_distance)
        if level == 1:
            if 3 < size < 7:
                is_leveling_maze_created = True
        elif level == 2:
            if 8 < size < 13:
                is_leveling_maze_created = True
        else:
            if 21 < size:
                is_leveling_maze_created = True

    print('Maze created.')
    MazeGenerator.print_maze(maze)
    print(f'move_list : {answer_pos_list}, size : {size}')

    MazeCanvas.draw_maze(maze)
    MazeCanvas.move_character(answer_pos_list)
    MazeCanvas.move_character(list(reversed(answer_pos_list)))
    turtle.exitonclick()


if __name__ == '__main__':
    main()
