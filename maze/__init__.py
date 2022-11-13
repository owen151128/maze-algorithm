# -*- coding: utf-8 -*-

from random import randint
from collections import deque


class MazeGenerator(object):
    # array of top, bottom, right coordinates
    UP_DOWN_RIGHT_LIST = [(0, -1), (1, 0), (0, 1)]

    @staticmethod
    def print_maze(maze: list):
        for i in maze:
            for j in i:
                print(j, end='\t')
            print()

    # A function that creates and returns a 12 x 12 maze as a two-dimensional array
    @staticmethod
    def create_maze() -> list:
        # Create two-dimensional array initialize to 0
        maze: list = [[0] * 12 for _ in range(12)]

        # Create border wall
        for x in range(12):
            maze[0][x] = 1
            maze[12 - 1][x] = 1
        for y in range(1, 12 - 1):
            maze[y][0] = 1
            maze[y][12 - 1] = 1

        # Create walls at intervals of 1 space from the 3rd to the 9th column
        for y in range(2, 12 - 2, 2):
            for x in range(2, 12 - 2, 2):
                maze[y][x] = 1

        # Create a wall from the wall to the top, bottom, left and right
        # (The wall is created from the second row, and the wall to the left is not created.)
        for y in range(2, 12 - 2, 2):
            for x in range(4, 12 - 2, 2):
                random_x, random_y = \
                    MazeGenerator.UP_DOWN_RIGHT_LIST[randint(0, len(MazeGenerator.UP_DOWN_RIGHT_LIST) - 1)]
                maze[y + random_y][x + random_x] = 1

        # Create a Goal in the maze (created in empty space from 3rd column and above)
        goal_x: int = 0
        goal_y: int = 0
        while maze[goal_y][goal_x] == 1:
            goal_x, goal_y = randint(2, 10), randint(2, 10)
        maze[goal_y][goal_x] = 2

        return maze


class MazeExplorer:
    # Move array for BFS Algorithm
    bfs_move_list = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    @staticmethod
    def get_max_distance(maze: list):
        wall_count = 0
        for x in maze:
            wall_count += x.count(1)

        return 12 * 12 - wall_count - 1

    # Derives the correct answer using the BFS (Breadth First Search) algorithm
    # Returns : answer_post_list, list's size
    @staticmethod
    def get_answer_pos_list(maze: list, max_distance: int) -> (list, int):
        y, x, distance, move_list = 1, 1, 0, [(1, 1)]
        while maze[y][x] != 2:
            deq = deque()
            deq.append((y, x, distance, [(1, 1)]))
            while deq:
                y, x, distance, move_list = deq.popleft()

                # Did you find the goal?
                if maze[y][x] == 2:
                    break

                # Exceeding the maximum distance?
                if distance > max_distance:
                    continue

                for move_y, move_x in MazeExplorer.bfs_move_list:
                    destination_y, destination_x = y + move_y, x + move_x

                    # Get out of the maze?
                    if destination_y < 1 or destination_x < 1 or destination_y >= 11 or destination_x >= 11:
                        continue

                    # Is the coordinate you want to move to 1 (wall)?
                    if maze[destination_y][destination_x] == 1:
                        continue

                    # Is it the coordinates you visited?
                    if (destination_y, destination_x) in move_list:
                        continue

                    # Save the moved coordinate list
                    # Using slice for list deep copy
                    current_move_list = move_list[:]
                    current_move_list.append((destination_y, destination_x))
                    deq.append((destination_y, destination_x, distance + 1, current_move_list))

        return move_list, len(move_list)
