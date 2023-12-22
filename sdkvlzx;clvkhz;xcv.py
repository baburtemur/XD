import pygame.display
import copy
import random

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 5
        self.top = 5
        self.cell_size = 20

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def get_click(self, mouse_pos, event):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell, event)

    def get_cell(self, mouse_pos):
        x = (mouse_pos[0] - self.left) // self.cell_size
        y = (mouse_pos[1] - self.top) // self.cell_size
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return None
        return y, x

    def on_click(self, cell, event):
        q, w = board.get_cell(event.pos)
        board.board[q][w] += 1
        board.board[q][w] %= 3
        print(cell)

    def render(self, screen):
        for i in range(self.width):
            for j in range(self.height):
                color = (0, 0, 255)
                if board.board[j][i] == 0:
                    color = (0, 0, 0)
                if board.board[j][i] == 1:
                    color = (255, 0, 0)
                pygame.draw.rect(screen, pygame.Color('green'), (i * self.cell_size + self.left, j * self.cell_size + self.top,
                            self.cell_size, self.cell_size))
                pygame.draw.rect(screen, (255, 255, 255), (i * self.cell_size + self.left, j * self.cell_size + self.top,
                            self.cell_size, self.cell_size), 1)


class Minesweeper(Board):
    def __init__(self, height, width):
        super().__init__(height, width)
        self.board = [[-1] * width for _ in range(height)]
        n = random.randrange((self.width - 1) * (self.height - 1))
        while n:
            x = random.randrange(self.width - 1)
            y = random.randrange(self.height - 1)
            self.board[x][y] = 10
            n += 1



    def on_click(self, cell, event):
        x, y = cell
        return x, y


    def render(self, screen):
        for i in range(self.width):
            for j in range(self.height):
                if self.board[i][j] == 10:
                    color = 'red'
                else:
                    color = 'green'
                pygame.draw.rect(screen, pygame.Color(color),
                                 (j * self.cell_size + self.left, i * self.cell_size + self.top,
                                  self.cell_size, self.cell_size))
                pygame.draw.rect(screen, (255, 255, 255),
                                 (j * self.cell_size + self.left, i * self.cell_size + self.top,
                                  self.cell_size, self.cell_size), 1)

    def next_move(self):
        temp_board = copy.deepcopy(self.board)
        for i in range(self.height):
            for j in range(self.width):
                s = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if x + i < 0 or x + i >= self.height or y + j < 0 or y + j >= self.width:
                            continue
                        s += self.board[x + i][y + j]
                s -= self.board[i][j]


pygame.init()
board = Minesweeper(15, 15)
size = width, height = 1000, 1000
screen = pygame.display.set_mode(size)
running = True
board.set_view(100, 100, 50)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()
pygame.quit()
