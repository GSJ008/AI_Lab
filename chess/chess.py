  
import pygame
import requests
import rembg
from io import BytesIO

  
pygame.init()

  
WIDTH = 700
HEIGHT = 700

  
BOARD_SIZE = min(WIDTH - 200, HEIGHT - 100)    
SQUARE_SIZE = BOARD_SIZE // 8
BOARD_X = 0
BOARD_Y = 0

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Chess Game')

font = pygame.font.Font('freesansbold.ttf', 16)
medium_font = pygame.font.Font('freesansbold.ttf', 24)
big_font = pygame.font.Font('freesansbold.ttf', 32)

timer = pygame.time.Clock()
fps = 60

  
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

captured_pieces_white = []
captured_pieces_black = []

  
turn_step = 0
selection = 100
valid_moves = []

  
image_urls = ['https://media.geeksforgeeks.org/wp-content/uploads/20240302025946/black_queen.png',
              'https://media.geeksforgeeks.org/wp-content/uploads/20240302025948/black_king.png',
              'https://media.geeksforgeeks.org/wp-content/uploads/20240302025345/black_rook.png',
              'https://media.geeksforgeeks.org/wp-content/uploads/20240302025951/black_bishop.png',
              'https://media.geeksforgeeks.org/wp-content/uploads/20240302025947/black_knight.png',
              'https://media.geeksforgeeks.org/wp-content/uploads/20240302025945/black_pawn.png',
              'https://media.geeksforgeeks.org/wp-content/uploads/20240302025952/white_queen.png',
              'https://media.geeksforgeeks.org/wp-content/uploads/20240302025943/white_king.png',
              'https://media.geeksforgeeks.org/wp-content/uploads/20240302025949/white_rook.png',
              'https://media.geeksforgeeks.org/wp-content/uploads/20240302025944/white_bishop.png',
              'https://media.geeksforgeeks.org/wp-content/uploads/20240302025325/white_knight.png',
              'https://media.geeksforgeeks.org/wp-content/uploads/20240302025953/white_pawn.png']

  
piece_size = int(SQUARE_SIZE * 0.8)
small_piece_size = int(SQUARE_SIZE * 0.45)

  
black_queen = pygame.image.load(
    BytesIO(rembg.remove(requests.get(image_urls[0]).content)))
black_queen = pygame.transform.scale(black_queen, (piece_size, piece_size))
black_queen_small = pygame.transform.scale(black_queen, (small_piece_size, small_piece_size))
black_king = pygame.image.load(
    BytesIO(rembg.remove(requests.get(image_urls[1]).content)))
black_king = pygame.transform.scale(black_king, (piece_size, piece_size))
black_king_small = pygame.transform.scale(black_king, (small_piece_size, small_piece_size))
black_rook = pygame.image.load(
    BytesIO(rembg.remove(requests.get(image_urls[2]).content)))
black_rook = pygame.transform.scale(black_rook, (piece_size, piece_size))
black_rook_small = pygame.transform.scale(black_rook, (small_piece_size, small_piece_size))
black_bishop = pygame.image.load(
    BytesIO(rembg.remove(requests.get(image_urls[3]).content)))
black_bishop = pygame.transform.scale(black_bishop, (piece_size, piece_size))
black_bishop_small = pygame.transform.scale(black_bishop, (small_piece_size, small_piece_size))
black_knight = pygame.image.load(
    BytesIO(rembg.remove(requests.get(image_urls[4]).content)))
black_knight = pygame.transform.scale(black_knight, (piece_size, piece_size))
black_knight_small = pygame.transform.scale(black_knight, (small_piece_size, small_piece_size))
black_pawn = pygame.image.load(
    BytesIO(rembg.remove(requests.get(image_urls[5]).content)))
black_pawn = pygame.transform.scale(black_pawn, (int(piece_size * 0.8), int(piece_size * 0.8)))
black_pawn_small = pygame.transform.scale(black_pawn, (small_piece_size, small_piece_size))
white_queen = pygame.image.load(
    BytesIO(rembg.remove(requests.get(image_urls[6]).content)))
white_queen = pygame.transform.scale(white_queen, (piece_size, piece_size))
white_queen_small = pygame.transform.scale(white_queen, (small_piece_size, small_piece_size))
white_king = pygame.image.load(
    BytesIO(rembg.remove(requests.get(image_urls[7]).content)))
white_king = pygame.transform.scale(white_king, (piece_size, piece_size))
white_king_small = pygame.transform.scale(white_king, (small_piece_size, small_piece_size))
white_rook = pygame.image.load(
    BytesIO(rembg.remove(requests.get(image_urls[8]).content)))
white_rook = pygame.transform.scale(white_rook, (piece_size, piece_size))
white_rook_small = pygame.transform.scale(white_rook, (small_piece_size, small_piece_size))
white_bishop = pygame.image.load(
    BytesIO(rembg.remove(requests.get(image_urls[9]).content)))
white_bishop = pygame.transform.scale(white_bishop, (piece_size, piece_size))
white_bishop_small = pygame.transform.scale(white_bishop, (small_piece_size, small_piece_size))
white_knight = pygame.image.load(
    BytesIO(rembg.remove(requests.get(image_urls[10]).content)))
white_knight = pygame.transform.scale(white_knight, (piece_size, piece_size))
white_knight_small = pygame.transform.scale(white_knight, (small_piece_size, small_piece_size))
white_pawn = pygame.image.load(
    BytesIO(rembg.remove(requests.get(image_urls[11]).content)))
white_pawn = pygame.transform.scale(white_pawn, (int(piece_size * 0.8), int(piece_size * 0.8)))
white_pawn_small = pygame.transform.scale(white_pawn, (small_piece_size, small_piece_size))

white_images = [white_pawn, white_queen, white_king,
                white_knight, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small,
                      white_rook_small, white_bishop_small]

black_images = [black_pawn, black_queen, black_king,
                black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small,
                      black_knight_small, black_rook_small, black_bishop_small]

piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

  
counter = 0
winner = ''
game_over = False

  
ai_enabled = True    
ai_depth = 3    


  
def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'light gray', [
                             BOARD_X + BOARD_SIZE - (column * SQUARE_SIZE * 2), BOARD_Y + row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE])
        else:
            pygame.draw.rect(screen, 'light gray', [
                             BOARD_X + BOARD_SIZE - SQUARE_SIZE - (column * SQUARE_SIZE * 2), BOARD_Y + row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE])
    
      
    status_bar_y = BOARD_SIZE
    pygame.draw.rect(screen, 'gray', [0, status_bar_y, WIDTH, HEIGHT - status_bar_y])
    pygame.draw.rect(screen, 'gold', [0, status_bar_y, WIDTH, HEIGHT - status_bar_y], 3)
    
      
    if WIDTH > BOARD_SIZE:
        pygame.draw.rect(screen, 'gold', [BOARD_SIZE, 0, WIDTH - BOARD_SIZE, BOARD_SIZE], 3)
    
    status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                   'Black: Select a Piece to Move!', 'Black: Select a Destination!']
    
      
    text_y = status_bar_y + 10
    if HEIGHT - status_bar_y > 50:
        screen.blit(medium_font.render(status_text[turn_step], True, 'black'), (20, text_y))
    else:
        screen.blit(font.render(status_text[turn_step], True, 'black'), (20, text_y))
    
      
    for i in range(9):
        pygame.draw.line(screen, 'black', (BOARD_X, BOARD_Y + SQUARE_SIZE * i), (BOARD_X + BOARD_SIZE, BOARD_Y + SQUARE_SIZE * i), 2)
        pygame.draw.line(screen, 'black', (BOARD_X + SQUARE_SIZE * i, BOARD_Y), (BOARD_X + SQUARE_SIZE * i, BOARD_Y + BOARD_SIZE), 2)
    
      
    if WIDTH > BOARD_SIZE + 100 and HEIGHT > 100:
        forfeit_x = BOARD_SIZE + 10
        forfeit_y = HEIGHT - 50
        screen.blit(font.render('FORFEIT', True, 'black'), (forfeit_x, forfeit_y))


  
def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        piece_x = BOARD_X + white_locations[i][0] * SQUARE_SIZE + (SQUARE_SIZE - piece_size) // 2
        piece_y = BOARD_Y + white_locations[i][1] * SQUARE_SIZE + (SQUARE_SIZE - piece_size) // 2
        
        if white_pieces[i] == 'pawn':
            pawn_offset = (SQUARE_SIZE - int(piece_size * 0.8)) // 2
            screen.blit(white_pawn, (BOARD_X + white_locations[i][0] * SQUARE_SIZE + pawn_offset, 
                                   BOARD_Y + white_locations[i][1] * SQUARE_SIZE + pawn_offset))
        else:
            screen.blit(white_images[index], (piece_x, piece_y))
        
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'red', [BOARD_X + white_locations[i][0] * SQUARE_SIZE + 1, 
                                               BOARD_Y + white_locations[i][1] * SQUARE_SIZE + 1,
                                               SQUARE_SIZE - 2, SQUARE_SIZE - 2], 2)

    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        piece_x = BOARD_X + black_locations[i][0] * SQUARE_SIZE + (SQUARE_SIZE - piece_size) // 2
        piece_y = BOARD_Y + black_locations[i][1] * SQUARE_SIZE + (SQUARE_SIZE - piece_size) // 2
        
        if black_pieces[i] == 'pawn':
            pawn_offset = (SQUARE_SIZE - int(piece_size * 0.8)) // 2
            screen.blit(black_pawn, (BOARD_X + black_locations[i][0] * SQUARE_SIZE + pawn_offset, 
                                   BOARD_Y + black_locations[i][1] * SQUARE_SIZE + pawn_offset))
        else:
            screen.blit(black_images[index], (piece_x, piece_y))
        
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue', [BOARD_X + black_locations[i][0] * SQUARE_SIZE + 1, 
                                                BOARD_Y + black_locations[i][1] * SQUARE_SIZE + 1,
                                                SQUARE_SIZE - 2, SQUARE_SIZE - 2], 2)


  
def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range((len(pieces))):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        elif piece == 'king':
            moves_list = check_king(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list


  
def check_king(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
      
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0),
               (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list


  
def check_queen(position, color):
    moves_list = check_bishop(position, color)
    second_list = check_rook(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list


  
def check_bishop(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    for i in range(4):    
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append(
                    (position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list


  
def check_rook(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    for i in range(4):    
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append(
                    (position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list


  
def check_pawn(position, color):
    moves_list = []
    if color == 'white':
        if (position[0], position[1] + 1) not in white_locations and \
                (position[0], position[1] + 1) not in black_locations and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        if (position[0], position[1] + 2) not in white_locations and \
                (position[0], position[1] + 2) not in black_locations and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        if (position[0] + 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] - 1, position[1] + 1))
    else:
        if (position[0], position[1] - 1) not in white_locations and \
                (position[0], position[1] - 1) not in black_locations and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] - 2) not in white_locations and \
                (position[0], position[1] - 2) not in black_locations and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list


  
def check_knight(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
      
    targets = [(1, 2), (1, -2), (2, 1), (2, -1),
               (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list


  
def check_valid_moves():
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options


  
piece_values = {'pawn': 1, 'knight': 3, 'bishop': 3, 'rook': 5, 'queen': 9, 'king': 1000}

  
def evaluate_board():
    white_score = 0
    black_score = 0
    
      
    for piece in white_pieces:
        white_score += piece_values[piece]
    
    for piece in black_pieces:
        black_score += piece_values[piece]
    
      
      
    center_squares = [(3, 3), (3, 4), (4, 3), (4, 4)]
    for pos in white_locations:
        if pos in center_squares:
            white_score += 0.1
    
    for pos in black_locations:
        if pos in center_squares:
            black_score += 0.1
    
      
    white_score += len([move for moves in white_options for move in moves]) * 0.01
    black_score += len([move for moves in black_options for move in moves]) * 0.01
    
    return white_score - black_score

  
def is_legal_move(piece_index, new_pos, is_white):
    if is_white:
        if piece_index >= len(white_pieces):
            return False
        options = white_options
    else:
        if piece_index >= len(black_pieces):
            return False
        options = black_options
    
    return new_pos in options[piece_index]

  
def make_move(piece_index, new_pos, is_white):
    captured_piece = None
    captured_index = None
    
    if is_white:
        old_pos = white_locations[piece_index]
        white_locations[piece_index] = new_pos
        
          
        if new_pos in black_locations:
            captured_index = black_locations.index(new_pos)
            captured_piece = black_pieces[captured_index]
            captured_pieces_white.append(captured_piece)
            black_pieces.pop(captured_index)
            black_locations.pop(captured_index)
    else:
        old_pos = black_locations[piece_index]
        black_locations[piece_index] = new_pos
        
          
        if new_pos in white_locations:
            captured_index = white_locations.index(new_pos)
            captured_piece = white_pieces[captured_index]
            captured_pieces_black.append(captured_piece)
            white_pieces.pop(captured_index)
            white_locations.pop(captured_index)
    
    return captured_piece, captured_index,old_pos

  
def undo_move(piece_index, old_pos, new_pos, captured_piece,captured_index, is_white):
    if is_white:
        white_locations[piece_index] = old_pos
        
        if captured_piece is not None:
              
            black_pieces.insert(captured_index, captured_piece)
            black_locations.insert(captured_index, new_pos)

            captured_pieces_white.pop()
            
    else:
        black_locations[piece_index] = old_pos
        
        if captured_piece is not None:
              
            white_pieces.insert(captured_index, captured_piece)
            white_locations.insert(captured_index, new_pos)
            captured_pieces_black.pop()

  
def get_all_moves(is_white):
    moves = []
    pieces = white_pieces if is_white else black_pieces
    options = white_options if is_white else black_options
    
    for piece_index, piece_moves in enumerate(options):
        for move in piece_moves:
            moves.append((piece_index, move))
    
    return moves

  
def minimax(depth, is_maximizing, alpha, beta):
    global white_options, black_options
    
      
    white_options = check_options(white_pieces, white_locations, 'white')
    black_options = check_options(black_pieces, black_locations, 'black')
    
      
    if 'king' not in white_pieces:
        return -1000 - depth    
    if 'king' not in black_pieces:
        return 1000 + depth     
    
    if depth == 0:
        return evaluate_board()
    
    if is_maximizing:    
        max_eval = float('-inf')
        moves = get_all_moves(True)
        
        for piece_index, move in moves:
              
            captured_piece,captured_index, old_pos = make_move(piece_index, move, True)
            
              
            eval_score = minimax(depth - 1, False, alpha, beta)
            
              
            undo_move(piece_index, old_pos, move, captured_piece, captured_index,True)
            
            max_eval = max(max_eval, eval_score)
            alpha = max(alpha, eval_score)
            
            if beta <= alpha:
                break    
        
        return max_eval
    else:    
        min_eval = float('inf')
        moves = get_all_moves(False)
        
        for piece_index, move in moves:
              
            captured_piece, captured_index,old_pos = make_move(piece_index, move, False)
            
              
            eval_score = minimax(depth - 1, True, alpha, beta)
            
              
            undo_move(piece_index, old_pos, move, captured_piece, captured_index,False)
            
            min_eval = min(min_eval, eval_score)
            beta = min(beta, eval_score)
            
            if beta <= alpha:
                break    
        
        return min_eval

  
def get_ai_move():
    best_move = None
    best_score = float('inf')    
    
    moves = get_all_moves(False)    
    
    for piece_index, move in moves:
          
        captured_piece,captured_index, old_pos = make_move(piece_index, move, False)
        
          
        score = minimax(ai_depth - 1, True, float('-inf'), float('inf'))
        
          
        undo_move(piece_index, old_pos, move, captured_piece, captured_index,False)
        
        if score < best_score:
            best_score = score
            best_move = (piece_index, move)
    
    return best_move

  
def make_ai_move():
    global turn_step, winner, white_options, black_options
    
    ai_move = get_ai_move()
    if ai_move:
        piece_index, new_pos = ai_move
        
          
        black_locations[piece_index] = new_pos
        
          
        if new_pos in white_locations:
            white_piece_index = white_locations.index(new_pos)
            captured_pieces_black.append(white_pieces[white_piece_index])
            if white_pieces[white_piece_index] == 'king':
                winner = 'black'
            white_pieces.pop(white_piece_index)
            white_locations.pop(white_piece_index)
        
          
        black_options = check_options(black_pieces, black_locations, 'black')
        white_options = check_options(white_pieces, white_locations, 'white')
        turn_step = 0


  
def draw_valid(moves):
    if turn_step < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(
            screen, color, (BOARD_X + moves[i][0] * SQUARE_SIZE + SQUARE_SIZE // 2, 
                          BOARD_Y + moves[i][1] * SQUARE_SIZE + SQUARE_SIZE // 2), 5)


  
def draw_captured():
    if WIDTH > BOARD_SIZE:
        for i in range(len(captured_pieces_white)):
            captured_piece = captured_pieces_white[i]
            index = piece_list.index(captured_piece)
            screen.blit(small_black_images[index], (BOARD_SIZE + 25, 5 + small_piece_size * i))
        for i in range(len(captured_pieces_black)):
            captured_piece = captured_pieces_black[i]
            index = piece_list.index(captured_piece)
            if WIDTH > BOARD_SIZE + 100:
                screen.blit(small_white_images[index], (BOARD_SIZE + 125, 5 + small_piece_size * i))
            else:
                screen.blit(small_white_images[index], (BOARD_SIZE + 25, 5 + small_piece_size * (i + len(captured_pieces_white))))


  
def draw_check():
    if turn_step < 2:
        if 'king' in white_pieces:
            king_index = white_pieces.index('king')
            king_location = white_locations[king_index]
            for i in range(len(black_options)):
                if king_location in black_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark red', [BOARD_X + white_locations[king_index][0] * SQUARE_SIZE + 1,
                                                              BOARD_Y + white_locations[king_index][1] * SQUARE_SIZE + 1, 
                                                              SQUARE_SIZE - 2, SQUARE_SIZE - 2], 5)
    else:
        if 'king' in black_pieces:
            king_index = black_pieces.index('king')
            king_location = black_locations[king_index]
            for i in range(len(white_options)):
                if king_location in white_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark blue', [BOARD_X + black_locations[king_index][0] * SQUARE_SIZE + 1,
                                                               BOARD_Y + black_locations[king_index][1] * SQUARE_SIZE + 1, 
                                                               SQUARE_SIZE - 2, SQUARE_SIZE - 2], 5)


def draw_game_over():
    overlay_width = min(400, WIDTH - 40)
    overlay_height = 70
    overlay_x = (WIDTH - overlay_width) // 2
    overlay_y = (HEIGHT - overlay_height) // 2
    
    pygame.draw.rect(screen, 'black', [overlay_x, overlay_y, overlay_width, overlay_height])
    screen.blit(font.render(f'{winner} won the game!', True, 'white'), (overlay_x + 10, overlay_y + 10))
    screen.blit(font.render(f'Press ENTER to Restart!', True, 'white'), (overlay_x + 10, overlay_y + 40))


  
black_options = check_options(black_pieces, black_locations, 'black')
white_options = check_options(white_pieces, white_locations, 'white')
run = True
while run:
    timer.tick(fps)
    if counter < 30:
        counter += 1
    else:
        counter = 0
    screen.fill('dark gray')
    draw_board()
    draw_pieces()
    draw_captured()
    draw_check()
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)
              
    if ai_enabled and not game_over and turn_step == 2:
        make_ai_move()


      
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x_coord = (event.pos[0] - BOARD_X) // SQUARE_SIZE
            y_coord = (event.pos[1] - BOARD_Y) // SQUARE_SIZE
            click_coords = (x_coord, y_coord)
            
              
            if 0 <= x_coord <= 7 and 0 <= y_coord <= 7:
                if turn_step <= 1:
                      
                    if event.pos[0] > BOARD_SIZE and event.pos[1] > HEIGHT - 60:
                        winner = 'black'
                    if click_coords in white_locations:
                        selection = white_locations.index(click_coords)
                        if turn_step == 0:
                            turn_step = 1
                    if click_coords in valid_moves and selection != 100:
                        white_locations[selection] = click_coords
                        if click_coords in black_locations:
                            black_piece = black_locations.index(click_coords)
                            captured_pieces_white.append(black_pieces[black_piece])
                            if black_pieces[black_piece] == 'king':
                                winner = 'white'
                            black_pieces.pop(black_piece)
                            black_locations.pop(black_piece)
                        black_options = check_options(
                            black_pieces, black_locations, 'black')
                        white_options = check_options(
                            white_pieces, white_locations, 'white')
                        turn_step = 2
                        selection = 100
                        valid_moves = []
                if turn_step > 1:
                      
                    if event.pos[0] > BOARD_SIZE and event.pos[1] > HEIGHT - 60:
                        winner = 'white'
                    if click_coords in black_locations:
                        selection = black_locations.index(click_coords)
                        if turn_step == 2:
                            turn_step = 3
                    if click_coords in valid_moves and selection != 100:
                        black_locations[selection] = click_coords
                        if click_coords in white_locations:
                            white_piece = white_locations.index(click_coords)
                            captured_pieces_black.append(white_pieces[white_piece])
                            if white_pieces[white_piece] == 'king':
                                winner = 'black'
                            white_pieces.pop(white_piece)
                            white_locations.pop(white_piece)
                        black_options = check_options(
                            black_pieces, black_locations, 'black')
                        white_options = check_options(
                            white_pieces, white_locations, 'white')
                        turn_step = 0
                        selection = 100
                        valid_moves = []

        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                game_over = False
                winner = ''
                white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                captured_pieces_white = []
                captured_pieces_black = []
                turn_step = 0
                selection = 100
                valid_moves = []
                black_options = check_options(
                    black_pieces, black_locations, 'black')
                white_options = check_options(
                    white_pieces, white_locations, 'white')

    if winner != '':
        game_over = True
        draw_game_over()

    pygame.display.flip()

pygame.quit()