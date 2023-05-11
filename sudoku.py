import pygame as pg
import pandas as pd
import random
import math
import time

# Colors
black = (0, 0, 0)
red = (255, 100, 100)
green = (100, 255, 100)
blue = (100, 100, 255)
light_blue = (200, 200, 255)
white = (255, 255, 255)

# Levels
hard = 26
medium = 41
easy = 58

# Setup game screen
window = pg.display.set_mode((1000, 700))

# Setup game font
pg.font.init()
font = pg.font.SysFont('Courier New', 50, bold=True)

board_date = [['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
              ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
              ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
              ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
              ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
              ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
              ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
              ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
              ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']]

game_date =  [['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
              ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
              ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
              ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
              ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
              ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
              ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
              ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
              ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']]

const_game = [['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
              ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
              ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
              ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
              ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
              ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
              ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
              ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
              ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']]

hiding_numbers = True
filled_board = True
click_last_status = False
win = False

click_position_x = -1
click_position_y = -1
number = 0

def Hover_Board(window, mouse_position_x, mouse_position_y):
    square = 66.7
    fit = 50

    x = (math.ceil((mouse_position_x - fit) / square) - 1)
    y = (math.ceil((mouse_position_y - fit) / square) - 1)
    
    pg.draw.rect(window, white, (0, 0, 1000, 700))
    
    if x >= 0 and x <= 8 and y >= 0 and y <= 8:
        pg.draw.rect(window, light_blue, ((fit + x * square, fit + y * square, square, square)))
    
def Selected_Square(window, mouse_position_x, mouse_position_y, click_last_status, click, x, y):
    square = 66.7
    fit = 50
    
    if click_last_status == True and click == True:
        x = (math.ceil((mouse_position_x - fit) / square) - 1)
        y = (math.ceil((mouse_position_y - fit) / square) - 1)
    
    if x >= 0 and x <= 8 and y >= 0 and y <= 8:
        pg.draw.rect(window, blue, ((fit + x * square, fit + y * square, square, square)))
    
    return x, y

def Board(window):
    pg.draw.rect(window, black, (50, 50, 600, 600), 6)
    pg.draw.rect(window, black, (50, 250, 600, 200), 6)
    pg.draw.rect(window, black, (250, 50, 200, 600), 6)
    pg.draw.rect(window, black, (50, 117, 600, 67), 2)
    pg.draw.rect(window, black, (50, 317, 600, 67), 2)
    pg.draw.rect(window, black, (50, 517, 600, 67), 2)
    pg.draw.rect(window, black, (117, 50, 67, 600), 2)
    pg.draw.rect(window, black, (317, 50, 67, 600), 2)
    pg.draw.rect(window, black, (517, 50, 67, 600), 2)

def Restart_Button(window):
    pg.draw.rect(window, green, (700, 50, 250, 100))

    word = font.render('Restart', True, black)
    window.blit(word, (725, 75))

def Check_Button(window):
    pg.draw.rect(window, green, (700, 250, 250, 100))

    word = font.render('Check', True, black)
    window.blit(word, (750, 275))

def Selected_Row(board_date, y):
    sorted_row = board_date[y]

    return sorted_row

def Selected_Column(board_date, x):
    sorted_column = []
    
    for row in range(8):
        sorted_column.append(board_date[row][x])

    return sorted_column

def Selected_Block(board_date, x, y):
    sorted_block = []
    
    if x >= 0 and x <= 2 and y >= 0 and y <= 2:
        sorted_block.extend([board_date[0][0], board_date[0][1], board_date[0][2],
                             board_date[1][0], board_date[1][1], board_date[1][2],
                             board_date[2][0], board_date[2][1], board_date[2][2]])
    
    if x >= 3 and x <= 5 and y >= 0 and y <= 2:
        sorted_block.extend([board_date[0][3], board_date[0][4], board_date[0][5],
                             board_date[1][3], board_date[1][4], board_date[1][5],
                             board_date[2][3], board_date[2][4], board_date[2][5]])
    
    if x >= 6 and x <= 8 and y >= 0 and y <= 2:
        sorted_block.extend([board_date[0][6], board_date[0][7], board_date[0][8],
                             board_date[1][6], board_date[1][7], board_date[1][8],
                             board_date[2][6], board_date[2][7], board_date[2][8]])
    
    if x >= 0 and x <= 2 and y >= 3 and y <= 5:
        sorted_block.extend([board_date[3][0], board_date[3][1], board_date[3][2],
                             board_date[4][0], board_date[4][1], board_date[4][2],
                             board_date[5][0], board_date[5][1], board_date[5][2]])
    
    if x >= 3 and x <= 5 and y >= 3 and y <= 5:
        sorted_block.extend([board_date[3][3], board_date[3][4], board_date[3][5],
                             board_date[4][3], board_date[4][4], board_date[4][5],
                             board_date[5][3], board_date[5][4], board_date[5][5]])
    
    if x >= 6 and x <= 8 and y >= 3 and y <= 5:
        sorted_block.extend([board_date[3][6], board_date[3][7], board_date[3][8],
                             board_date[4][6], board_date[4][7], board_date[4][8],
                             board_date[5][6], board_date[5][7], board_date[5][8]])
    
    if x >= 0 and x <= 2 and y >= 6 and y <= 8:
        sorted_block.extend([board_date[6][0], board_date[6][1], board_date[6][2],
                             board_date[7][0], board_date[7][1], board_date[7][2],
                             board_date[8][0], board_date[8][1], board_date[8][2]])
    
    if x >= 3 and x <= 5 and y >= 6 and y <= 8:
        sorted_block.extend([board_date[6][3], board_date[6][4], board_date[6][5],
                             board_date[7][3], board_date[7][4], board_date[7][5],
                             board_date[8][3], board_date[8][4], board_date[8][5]])
    
    if x >= 6 and x <= 8 and y >= 6 and y <= 8:
        sorted_block.extend([board_date[6][6], board_date[6][7], board_date[6][8],
                             board_date[7][6], board_date[7][7], board_date[7][8],
                             board_date[8][6], board_date[8][7], board_date[8][8]])
    
    return sorted_block

def Filling_Block(board_date, x2, y2):
    filled_block = True
    loop = 0
    try_count = 0
    number = 1
    
    while filled_block:
        x = random.randint(x2, x2 + 2)
        y = random.randint(y2, y2 + 2)
            
        sorted_row = Selected_Row(board_date, y)
        sorted_column = Selected_Column(board_date, x)
        sorted_block = Selected_Block(board_date, x, y)
        
        if board_date[y][x] == 'n' and number not in sorted_row and number not in sorted_column and number not in sorted_block:
            board_date[y][x] = number
            number += 1

        loop +=1
        
        if loop == 50:
            board_date[y2 + 0][x2 + 0] = 'n'
            board_date[y2 + 0][x2 + 1] = 'n'
            board_date[y2 + 0][x2 + 2] = 'n'
            board_date[y2 + 1][x2 + 0] = 'n'
            board_date[y2 + 1][x2 + 1] = 'n'
            board_date[y2 + 1][x2 + 2] = 'n'
            board_date[y2 + 2][x2 + 0] = 'n'
            board_date[y2 + 2][x2 + 1] = 'n'
            board_date[y2 + 2][x2 + 2] = 'n'
            
            loop = 0
            number = 1
            try_count += 1
        
        if try_count == 10:
            break

        count = 0
        
        for n in range(9):
            if sorted_block[n] != 'n':
                count += 1

        if count == 9:
            filled_block == False
            break

    return board_date

def Restart_Board_Date(board_date):
    board_date =   [['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                    ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                    ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                    ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                    ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                    ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                    ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                    ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                    ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']]
    
    return board_date

def Board_Result(board_date, filled_board):

    while filled_board:
        # Block - 1
        board_date = Filling_Block(board_date, 0, 0)
        
        # Block - 2
        board_date = Filling_Block(board_date, 3, 0)
        
        # Block - 3
        board_date = Filling_Block(board_date, 6, 0)
        
        # Block - 4
        board_date = Filling_Block(board_date, 0, 3)
        
        # Block - 5
        board_date = Filling_Block(board_date, 0, 6)

        # Block - 6
        board_date = Filling_Block(board_date, 3, 3)
        
        # Block - 7
        board_date = Filling_Block(board_date, 3, 6)
        
        # Block - 8
        board_date = Filling_Block(board_date, 6, 3)
        
        # Block - 9
        board_date = Filling_Block(board_date, 6, 6)
        
        
        for row in range(9):
            for col in range(9):
                if board_date[row][col] == 'n':
                    board_date = Restart_Board_Date(board_date)
                    
        count = 0
        
        for row in range(9):
            for col in range(9):
                if board_date[row][col] != 'n':
                    count += 1

        if count == 81:
            filled_board = False
        
    return board_date, filled_board

def Hiding_Numbers(board_date, const_game, game_date, hiding_numbers, level):
    if hiding_numbers == True:
        for _ in range(level):
            sort_number = True
            
            while sort_number:
                x = random.randint(0, 8)
                y = random.randint(0, 8)
                
                if game_date[y][x] == 'n':
                    const_game[y][x] = board_date[y][x]
                    game_date[y][x] = board_date[y][x]
                    sort_number = False
                
        hiding_numbers = False

    return const_game, game_date, hiding_numbers

def Writing_Numbers(window, const_game, game_date):
    square = 66.7
    fit = 67

    for row in range(9):
        for col in range(9):
            if const_game[row][col] != 'n':
                word = font.render(str(const_game[row][col]), True, black)
                window.blit(word, (fit + col * square, fit - 5 + row * square))
            elif game_date[row][col] != 'n':
                word = font.render(str(game_date[row][col]), True, green)
                window.blit(word, (fit + col * square, fit - 5 + row * square))
                    
def Input_Number(number):
    try:
        number = int(number[1])
    except:
        number = int(number)

    return number

def Check_Input_Number(game_date, const_game, click_position_x, click_position_y, number):
    x = click_position_x
    y = click_position_y
    
    if x >= 0 and x <=8 and y >= 0 and y <= 8 and const_game[y][x] == 'n' and number !=0:
        game_date[y][x] = number
        number = 0
    
    return game_date, number

def Click_Restart_Button(mouse_position_x, mouse_position_y, click_last_status, click, filled_board, hiding_numbers, board_date, game_date, const_game):
    x = mouse_position_x
    y = mouse_position_y
    
    if x >= 700 and x <= 950 and y >= 50 and y <= 150 and click_last_status == False and click == True:
        filled_board = True
        hiding_numbers = True
        board_date = Restart_Board_Date(board_date)
        game_date = Restart_Board_Date(game_date)
        const_game = Restart_Board_Date(const_game)
    
    return filled_board, hiding_numbers, board_date, game_date, const_game

def Click_Check_Button(mouse_position_x, mouse_position_y, click_last_status, click, board_date, game_date):
    x = mouse_position_x
    y = mouse_position_y
    
    if x >= 700 and x <= 950 and y >= 250 and y <= 350 and click_last_status == False and click == True:
        for row in range(9):
            for col in range(9):
                if board_date[row][col] != game_date[row][col]:
                    print("Gabarito errado do sudoku")
                    return False
        
        print("Parabens voce venceu o sudoku")
        return True

    return False

while not win:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            number = pg.key.name(event.key)
    
    # Declaring position variable
    mouse = pg.mouse.get_pos()
    mouse_position_x = mouse[0]
    mouse_position_y = mouse[1]
    
    # Declaring mouse variable
    click = pg.mouse.get_pressed()
    
    # Game
    Hover_Board(window, mouse_position_x, mouse_position_y)
    click_position_x, click_position_y = Selected_Square(window, mouse_position_x, mouse_position_y, click_last_status, click[0], click_position_x, click_position_y)
    Board(window)
    Restart_Button(window)
    Check_Button(window)
    board_date, filled_board = Board_Result(board_date, filled_board)
    const_game, game_date, hiding_numbers = Hiding_Numbers(board_date, const_game, game_date, hiding_numbers, easy)
    Writing_Numbers(window, const_game, game_date)
    number = Input_Number(number)
    game_date, number = Check_Input_Number(game_date, const_game, click_position_x, click_position_y, number)
    filled_board, hiding_numbers, board_date, game_date, const_game = Click_Restart_Button(mouse_position_x, mouse_position_y, click_last_status, click[0], filled_board, hiding_numbers, board_date, game_date, const_game)
    win = Click_Check_Button(mouse_position_x, mouse_position_y, click_last_status, click[0], board_date, game_date)
    
    # Click last status
    if click[0] == True:
        click_last_status = True
    else:
        click_last_status = False
    
    pg.display.update()


pg.draw.rect(window, light_blue, (0, 0, 1000, 700))

word = font.render('VITORIA', True, green)
window.blit(word, (400, 300))

(250, 50, 200, 600)

pg.display.update()
time.sleep(5)
