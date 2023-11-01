import random
import math

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
        a = random.random()
        if a < 0.4:  # w dol
            x=self.position[0]+1
            if x<=self.max_position[0] and self.position[0]<=self.max_position[0]:
                self.position=(x,self.position[1])
        elif a >= 0.4 and a < 0.8:  # w prawo
            x = self.position[1] + 1
            if x<=self.max_position[1] and self.position[1]<=self.max_position[1]:
                self.position = (self.position[0],x)
        elif a >= 0.8 and a < 0.88:  # w gore
            x = self.position[0] - 1
            if x >= self.min_position[0] and self.position[0]>=self.min_position[0]:
                self.position = (x, self.position[1])
        elif a >= 0.88 and a < 0.96:  # w lewo
            x = self.position[1] - 1
            if x >= self.min_position[1] and self.position[1]>=self.min_position[1]:
                self.position = (self.position[0], x)
        return self

    def has_finished(self):
        return self.position==self.max_position

class Board:
    __slots__ = ["board_size", "turtles"]

    def __init__(self, board_size):
        self.board_size=board_size
        turtles_count=math.floor(0.1*(board_size**2))
        board_pom = [[0 for i in range(board_size)] for j in range(board_size)]
        for i in range(board_size):
            for j in range(board_size - i):
                board_pom[i][j] = 1
        lista=[]
        for i in range(turtles_count):
            identifier=i+1
            min_position=(0,0)
            max_position=(board_size-1,board_size-1)
            position=(random.randint(0,board_size-1), random.randint(0,board_size-1))
            while board_pom[position[0]][position[1]]==2 or board_pom[position[0]][position[1]]==0:
                position = (random.randint(0, board_size - 1), random.randint(0, board_size - 1))
            board_pom[position[0]][position[1]]=2 #jesli nie bylo to zapelniam 2
            zolw=Turtle(identifier,position,min_position,max_position)
            lista.append(zolw)
        self.turtles=lista

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
        wynik=[[None for i in range(self.board_size)] for j in range(self.board_size)]
        for i in range(len(self.turtles)):
            zolw=self.turtles[i]
            position=zolw.position
            if wynik[position[0]][position[1]]!=None:
                wynik[position[0]][position[1]]+=zolw.identifier
            else:
                wynik[position[0]][position[1]]=zolw.identifier
        return wynik

    def is_over(self):
        for i in range(len(self.turtles)):
            zolw=self.turtles[i]
            if zolw.has_finished()==False:
                return False
        return True
    
    def next_round(self):
        for i in range(len(self.turtles)):
            zolw=self.turtles[i]
            zolw.make_move()

def main():
    board_size=int(input("Please provide board size: "))
    board=Board(board_size)
    print(board)
    while board.is_over()==False:
        board.next_round()
        print(board)

if __name__ == "__main__":
    main()