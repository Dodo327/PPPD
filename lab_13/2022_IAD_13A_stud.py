import random

class Turtle:
    __slots__ = ["position", "min_position", "max_position", "identifier"]

    def __init__(self, identifier, position, min_position, max_position):
        self.position = position
        self.min_position = min_position
        self.max_position = max_position
        self.identifier = identifier
        

    def __str__(self):
        return f'{self.identifier}'

    def make_move(self):
        chances = [i for i in range(25)]
        move = random.choice(chances)
        if 0 <= move < 10:
            if self.position[1] + 1 <= self.max_position:
                self.position = (self.position[0], self.position[1] + 1)
        elif 10 <= move < 20:
            if self.position[0] + 1 <= self.max_position:
                self.position = (self.position[0] + 1, self.position[1])
        elif 20 <= move < 22:
            if self.position[0] - 1 >= self.min_position[0]:
                self.position = (self.position[0] - 1, self.position[1])
        elif 22 <= move < 24:
            if self.position[1] - 1 >= self.min_position[1]:
                self.position = (self.position[0], self.position[1] - 1)
    
    def has_finished(self):
        return self.position == self.max_position

class Board:
    __slots__ = ["board_size", "turtles"]

    def __init__(self, board_size):
        self.board_size = board_size
        turles_count = int((self.board_size)**2 * 0.1)
        self.turtles = [None for _ in range(turles_count)]


    def __str__(self):
        board_matrix = self.create_matrix()
        board_printing = ''
        for j in range(len(board_matrix[0])*2 + 2):
            board_printing += "-"

        board_printing += '\n'

        for i in range(len(board_matrix)):
            board_printing+= "|"
            for j in range(len(board_matrix[i])):
                if board_matrix[i][j] is not None:
                    board_printing += f'{board_matrix[i][j]:2d}'
                else:
                    board_printing+= "  "
            board_printing+= "|\n"

        for j in range(len(board_matrix[0])*2 + 2):
            board_printing+='-'
        board_printing+='\n'

        return board_printing

    def create_matrix(self):
        board = [[None for i in range(self.board_size)]for _ in range(self.board_size)]
        for i in range(len(self.turtles)):
            turtle = self.turtles[i]
            if board[turtle.position[0]][turtle.position[1]] is None:
                board[turtle.position[0]][turtle.position[1]] = turtle.identifier
            else:
                board[turtle.position[0]][turtle.position[1]] += turtle.identifier
        return board

    def is_over(self):
        for i in range(len(self.turtles)):
            turtle = self.turtles[i]
            if not turtle.is_finished():
                return False
        return True
    
    def next_round(self):
        for i in range(len(self.turtles)):
            turtle = self.turtles[i]
            turtle.next_move()


def main():
    board_size = input('Podaj wielkosc planszy: ')
    board = Board(board_size)


if __name__ == "__main__":
    main()