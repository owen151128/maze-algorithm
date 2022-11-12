from random import randint


class MazeGenerator(object):
    # array of top, bottom, right coordinates
    UP_DOWN_RIGHT_LIST = [(0, -1), (1, 0), (0, 1)]

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
