import sys
import connectFourLogic as logic
import pygame
pygame.init()

# Definicja potrzebnych wymiarów
ROWS = 6
COLS = 7
SQUARE_SIZE = 100
width = COLS * SQUARE_SIZE
height = (ROWS+2) * SQUARE_SIZE
size = (width, height)
RADIUS = int(SQUARE_SIZE/2 - 5)
# Używane czcionki
font = pygame.font.SysFont('Consolas',  40)
font_2 = pygame.font.SysFont('Consolas',  60)
activated = False
pygame.display.set_caption("GRA CZTERY W RZEDZIE - Krzysztof Kulig")
# Używane w grze kolory
USED_COLORS = [
    (255,255,255),
    (255, 0, 0),
    (255, 255, 0)
]


class Buttons():
    
    button_color = (158, 101, 168)
    text_color = (255, 255, 255)
    shadow_color = (165, 102, 176)
    width = 50
    height = 50

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def set_buttons(self):
        global activated
        action = False
        mouse_position = pygame.mouse.get_pos()
        button = pygame.Rect(self.x, self.y, self.width, self.height)
        # Warunek sprawdzający czy kursor jest nad przyciskiem
        if button.collidepoint(mouse_position):
            # Warunek sprawdzający czy przycisk został wciśnięty i puszczony
            if pygame.mouse.get_pressed()[0] == 1:
                activated = True
                pygame.draw.rect(screen, self.button_color, button)
            elif pygame.mouse.get_pressed()[0] == 0 and activated == True:
                activated = False
                action = True
            else:
                pygame.draw.rect(screen, self.button_color, button)
        else:
            pygame.draw.rect(screen, self.shadow_color, button)
        # Przyciski - obramowanie
        pygame.draw.line(screen, USED_COLORS[0], (self.x, self.y), (self.x+self.width, self.y), 2)
        pygame.draw.line(screen, USED_COLORS[0], (self.x, self.y), (self.x, self.height+self.y), 2)
        pygame.draw.line(screen, (120, 120, 120), (self.x, self.height+self.y), (self.x + self.width, self.height+self.y), 2)
        pygame.draw.line(screen, (120, 120, 120), (self.x+self.width, self.y), (self.x+ self.width, self.height+self.y), 2)
        # Przyciski - tekst
        text_img = font.render(self.text, True, self.text_color)
        text_len = text_img.get_width()
        screen.blit(text_img, (self.x + int(self.width/2) - int(text_len/2), self.y+5))
        return action

# Przyciski nad kolumnami, wybór miejsca do wrzucenia monety
button = []

for i in range(0, COLS+1):
    temp = str(i+1)
    button.append(Buttons(25+i*100, 5, temp))


def set_board(board):
    for i in range(COLS+1):
        for j in range(ROWS):
            pygame.draw.rect(screen, (0, 0, 0), (i*SQUARE_SIZE, j*SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.circle(screen, USED_COLORS[0], (int(i*SQUARE_SIZE+SQUARE_SIZE/2), int(j*SQUARE_SIZE + SQUARE_SIZE+SQUARE_SIZE/2)), RADIUS)



app = logic.connect_four()
end = False
turn = 0


screen = pygame.display.set_mode(size)
set_board(app.board)
pygame.display.update()
m_1 = pygame.Rect(0, 700, 450, 120)
info = pygame.Rect(100, 300, 500, 120)
m_2 = pygame.Rect(200, 70, 400, 30)
reset = Buttons(485, 720, "RESET")
reset.width = 200
reset.height = 50

while not end:
    pygame.draw.rect(screen, (0, 0, 0), m_1)
    text_2 = font_2.render(f"PLAYER {turn + 1} TURN", True, USED_COLORS[turn +1])
    screen.blit(text_2, (0, 720))
    column = -1

    for i in range(0, COLS):
        if button[i].set_buttons():
            column = i

    if reset.set_buttons():
        var = app.board
        app = logic.connect_four()
        screen = pygame.display.set_mode(size)
        set_board(app.board)
        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if app.full_board():
        text = font.render("DRAW", True, USED_COLORS[0])
        pygame.draw.rect(screen, (25, 190, 225), info)
        pygame.draw.line(screen, USED_COLORS[0], (100, 300), (600, 300), 2)
        pygame.draw.line(screen, USED_COLORS[0], (100, 300), (100, 420), 2)
        pygame.draw.line(screen, (105, 105, 105), (100, 420), (600, 420), 2)
        pygame.draw.line(screen, (105, 105, 105), (600, 300), (100 + 500, 420), 2)
        screen.blit(text, (300, 340))
        pygame.display.update()
        pygame.time.wait(3000)
        var = app.board
        app = logic.connect_four()
        screen = pygame.display.set_mode(size)
        set_board(app.board)
        pygame.display.update()

    if column >= 0:
        if app.full_col(column):
            row = app.free_row(column)
            app.put_coin(row, column, turn + 1)
            pygame.draw.circle(screen, USED_COLORS[turn+1], (int(column * SQUARE_SIZE + SQUARE_SIZE / 2),int((5-row) * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2)),RADIUS)

            if app.ktoWygral(turn + 1):
                pygame.draw.rect(screen, (0, 0, 0), m_1)
                text_2 = font.render(f"PLAYER {turn + 1} WON!", True, (56, 54, 56))
                text_3 = font.render(f"CONGRATULATIONS!", True, USED_COLORS[turn+1])
                pygame.draw.rect(screen, (201, 182, 204), info)
                pygame.draw.line(screen, USED_COLORS[0], (100, 300), (600, 300), 2)
                pygame.draw.line(screen, USED_COLORS[0], (100, 300), (100, 420), 2)
                pygame.draw.line(screen, (105, 105, 105), (100, 420),(600, 420), 2)
                pygame.draw.line(screen, (105, 105, 105), (600, 300),(100 + 500, 420), 2)
                screen.blit(text_2, (175, 320))
                screen.blit(text_3, (225, 360))
                pygame.display.update()
                pygame.time.wait(3000)
                var = app.board
                app = logic.connect_four()
                screen = pygame.display.set_mode(size)
                set_board(app.board)
                pygame.display.update()

        else:
            text_5 = font.render("COLUMN FULL", True, (201, 182, 204))
            screen.blit(text_5, (200, 70))
            pygame.display.update()
            pygame.time.wait(1000)
            pygame.draw.rect(screen, (0, 0, 0), m_2)
            turn ^= 1



        app.g()
        turn ^= 1
    pygame.display.update()