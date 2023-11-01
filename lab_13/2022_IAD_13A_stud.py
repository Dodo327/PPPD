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
        move = random.random()
        if not self.has_finished():
            if move < 0.4:
                x = self.position[0] + 1
                if x <= self.max_position[0]:
                    self.position = (x, self.position[1])
            elif 0.4 <= move < 0.8:
                x = self.position[1] + 1
                if x <= self.max_position[1]:
                    self.position = (self.position[0], x)
            elif 0.8 <= move < 0.88:
                x = self.position[0] - 1
                if x >= self.min_position[0]:
                    self.position = (x, self.position[1])
            elif 0.88 <= move < 0.96:
                x = self.position[1] - 1
                if x >= self.min_position[1]:
                    self.position = (self.position[0], x)

    def has_finished(self):
        return self.position == self.max_position
    

class Board:
    __slots__ = ["board_size", "turtles"]

    def __init__(self, board_size):
        self.board_size = int(board_size)
        turtles_count = int(board_size**2 * 0.1)
        self.turtles = [None for _ in range(turtles_count)]
        
        for i in range(turtles_count):
            pos_x = random.randint(0, board_size - 1)
            pos_y = random.randint(0, board_size - pos_x - 1)
            self.turtles[i] = Turtle(i+1, (pos_x, pos_y), (0, 0), (board_size - 1, board_size - 1))
            
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
        plansza = [[None for i in range(self.board_size)] for _ in range(self.board_size)]
        for i in range(len(self.turtles)):
            turtle = self.turtles[i]
            if plansza[turtle.position[0]][turtle.position[1]] is None:
                plansza[turtle.position[0]][turtle.position[1]] = turtle.identifier
            else:
                plansza[turtle.position[0]][turtle.position[1]] += turtle.identifier
        return plansza

    def is_over(self):
        for turtle in self.turtles:
            if not turtle.has_finished():
                return False
        return True
    
    def next_round(self):
        for turtle in self.turtles:
            turtle.make_move()


def main():
    board_size = int(input('Podaj wielkosc planszy: '))
    board = Board(board_size)
    print(board)

    while not board.is_over():
        board.next_round()
        print(board)

if __name__ == "__main__":
    main()