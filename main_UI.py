import pygame
import sys
import time
import random

x = 1280
y = 720

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((x, y))

# https://icons8.com/

pygame.display.set_caption('TM Casino')
icon = pygame.image.load('images/icon.png')
cbb = pygame.image.load('images/Cards/cardBack_blue3.png')
c2 = [pygame.image.load('images/Cards/cardClubs2.png'), 2]
c3 = [pygame.image.load('images/Cards/cardClubs3.png'), 3]
c4 = [pygame.image.load('images/Cards/cardClubs4.png'), 4]
c5 = [pygame.image.load('images/Cards/cardClubs5.png'), 5]
c6 = [pygame.image.load('images/Cards/cardClubs6.png'), 6]
c7 = [pygame.image.load('images/Cards/cardClubs7.png'), 7]
c8 = [pygame.image.load('images/Cards/cardClubs8.png'), 8]
c9 = [pygame.image.load('images/Cards/cardClubs9.png'), 9]
c10 = [pygame.image.load('images/Cards/cardClubs10.png'), 10]
cj = [pygame.image.load('images/Cards/cardClubsJ.png'), 10]
cq = [pygame.image.load('images/Cards/cardClubsQ.png'), 10]
ck = [pygame.image.load('images/Cards/cardClubsK.png'), 10]
ca = [pygame.image.load('images/Cards/cardClubsA.png'), 1]
d2 = [pygame.image.load('images/Cards/cardDiamonds2.png'), 2]
d3 = [pygame.image.load('images/Cards/cardDiamonds3.png'), 3]
d4 = [pygame.image.load('images/Cards/cardDiamonds4.png'), 4]
d5 = [pygame.image.load('images/Cards/cardDiamonds5.png'), 5]
d6 = [pygame.image.load('images/Cards/cardDiamonds6.png'), 6]
d7 = [pygame.image.load('images/Cards/cardDiamonds7.png'), 7]
d8 = [pygame.image.load('images/Cards/cardDiamonds8.png'), 8]
d9 = [pygame.image.load('images/Cards/cardDiamonds9.png'), 9]
d10 = [pygame.image.load('images/Cards/cardDiamonds10.png'), 10]
dj = [pygame.image.load('images/Cards/cardDiamondsJ.png'), 10]
dq = [pygame.image.load('images/Cards/cardDiamondsQ.png'), 10]
dk = [pygame.image.load('images/Cards/cardDiamondsK.png'), 10]
da = [pygame.image.load('images/Cards/cardDiamondsA.png'), 1]
h2 = [pygame.image.load('images/Cards/cardHearts2.png'), 2]
h3 = [pygame.image.load('images/Cards/cardHearts3.png'), 3]
h4 = [pygame.image.load('images/Cards/cardHearts4.png'), 4]
h5 = [pygame.image.load('images/Cards/cardHearts5.png'), 5]
h6 = [pygame.image.load('images/Cards/cardHearts6.png'), 6]
h7 = [pygame.image.load('images/Cards/cardHearts7.png'), 7]
h8 = [pygame.image.load('images/Cards/cardHearts8.png'), 8]
h9 = [pygame.image.load('images/Cards/cardHearts9.png'), 9]
h10 = [pygame.image.load('images/Cards/cardHearts10.png'), 10]
hj = [pygame.image.load('images/Cards/cardHeartsJ.png'), 10]
hq = [pygame.image.load('images/Cards/cardHeartsQ.png'), 10]
hk = [pygame.image.load('images/Cards/cardHeartsK.png'), 10]
ha = [pygame.image.load('images/Cards/cardHeartsA.png'), 1]
s2 = [pygame.image.load('images/Cards/cardSpades2.png'), 2]
s3 = [pygame.image.load('images/Cards/cardSpades3.png'), 3]
s4 = [pygame.image.load('images/Cards/cardSpades4.png'), 4]
s5 = [pygame.image.load('images/Cards/cardSpades5.png'), 5]
s6 = [pygame.image.load('images/Cards/cardSpades6.png'), 6]
s7 = [pygame.image.load('images/Cards/cardSpades7.png'), 7]
s8 = [pygame.image.load('images/Cards/cardSpades8.png'), 8]
s9 = [pygame.image.load('images/Cards/cardSpades9.png'), 9]
s10 = [pygame.image.load('images/Cards/cardSpades10.png'), 10]
sj = [pygame.image.load('images/Cards/cardSpadesJ.png'), 10]
sq = [pygame.image.load('images/Cards/cardSpadesQ.png'), 10]
sk = [pygame.image.load('images/Cards/cardSpadesK.png'), 10]
sa = [pygame.image.load('images/Cards/cardSpadesA.png'), 1]
cat = pygame.image.load('images/Animals/cat.png')
dog = pygame.image.load('images/Animals/dog.png')
flamingo = pygame.image.load('images/Animals/flamingo.png')
fox = pygame.image.load('images/Animals/fox.png')
monkey = pygame.image.load('images/Animals/monkey.png')
penguin = pygame.image.load('images/Animals/penguin.png')
shark = pygame.image.load('images/Animals/shark.png')
parrot = pygame.image.load('images/Animals/parrot.png')


pygame.display.set_icon(icon)
font = pygame.font.Font(None, 64)
e_font = pygame.font.Font(None, 32)
COLOR_INACTIVE = (68, 68, 68)
COLOR_ACTIVE = (5, 5, 5)
r_error1 = False
r_error2 = False
l_error = False
qt_error_chips = False


class Button:
    def __init__(self, color, xx, yy, width, height, text=''):
        self.color = color
        self.x = xx
        self.y = yy
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            b_font = pygame.font.SysFont(None, 60)
            text = b_font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (int(self.x + (self.width / 2 - text.get_width() / 2)),
                            int(self.y + (self.height / 2 - text.get_height() / 2))))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False


class InputBox:

    def __init__(self, xx, yy, w, h, text=''):
        self.rect = pygame.Rect(xx, yy, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = font.render(text, True, self.color)
        self.active = False
        self.user_name_len = 0
        self.input_txt = ''

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    pass
                    # print(self.text)
                    # self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = font.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(500, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)


def start_menu():
    loginButton = Button((255, 255, 255), int(x / 2 - 150), 100, 250, 100, 'Login')
    registerButton = Button((255, 255, 255), int(x / 2 - 150), y - 200, 250, 100, 'Register')

    running = True
    while running:

        screen.fill((170, 170, 170))
        loginButton.draw(screen, (0, 0, 0))
        registerButton.draw(screen, (0, 0, 0))
        pygame.display.update()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if loginButton.isOver(pos):
                    login_menu()
                if registerButton.isOver(pos):
                    register_menu()


def login_menu():
    global l_error
    running = True
    input_login = InputBox(int(x / 2) - 250, 150, 500, 64)
    enterButton = Button((255, 255, 255), int(x / 2 - 150), y - 200, 250, 100, 'Login')
    returnButton = Button((255, 255, 255), 10, 10, 150, 50, 'Return')
    usn_error = e_font.render('Username does not exist', True, (255, 0, 0))
    while running:
        screen.fill((170, 170, 170))
        input_login.update()
        input_login.draw(screen)
        enterButton.draw(screen, (0, 0, 0))
        returnButton.draw(screen, (0, 0, 0))
        if l_error:
            screen.blit(usn_error, (int(x / 2 - usn_error.get_width() / 2), 100))
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if returnButton.isOver(pos):
                    running = False
                    start_menu()
                if enterButton.isOver(pos):
                    info = open("info.txt", "r")

                    for line in info.readlines():
                        if line[:len(input_login.text)] == input_login.text and line[len(input_login.text)] == '-':
                            print("Welcome %s" % input_login.text)
                            chips = int(line[20:-1])
                            info.close()
                            print(chips)
                            user_name = str(input_login.text)
                            game_choice(user_name, line, chips)
                        else:
                            pass
                    print('Username %s does not exist' % input_login.text)
                    l_error = True
                    info.close()
                    login_menu()

            input_login.handle_event(event)
        pygame.display.update()


def register_menu():  # Error messages to be added
    global r_error1, r_error2
    running = True
    registerButton = Button((255, 255, 255), int(x / 2 - 150), y - 300, 250, 100, 'Register')
    returnButton = Button((255, 255, 255), 10, 10, 150, 50, 'Return')
    registerInput = InputBox(int(x / 2) - 250, 150, 500, 64)
    toolong_error = e_font.render('A username can\'t be above 20 characters', True, (255, 0, 0))
    existing_error = e_font.render("You can't create an account with an already exiting name", True, (255, 0, 0))

    while running:
        screen.fill((170, 170, 170))
        registerButton.draw(screen, (0, 0, 0))
        returnButton.draw(screen, (0, 0, 0))
        registerInput.draw(screen)
        registerInput.update()
        if r_error1:
            screen.blit(toolong_error, (int(x / 2 - toolong_error.get_width() / 2), 50))
        if r_error2:
            screen.blit(existing_error, (int(x / 2 - existing_error.get_width() / 2), 100))

        pygame.display.update()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if returnButton.isOver(pos):
                    running = False
                    start_menu()
                if registerButton.isOver(pos):
                    if len(registerInput.text) > 20:
                        print("A username can't be above 20 characters")
                        r_error1 = True
                        register_menu()
                    user_name_len = len(registerInput.text)
                    info = open("info.txt", "r")
                    for line in info.readlines():
                        if line[:len(registerInput.text)] == registerInput.text or registerInput.text == 'new':
                            print("You can't create an account with an already existing name")
                            r_error2 = True
                            info.close()
                            register_menu()
                    info.close()
                    print('Account created successfully')

                    # Adds new name to txt file
                    new_info = open("info.txt", "a")
                    new_info.write(registerInput.text)
                    for i in range(20 - user_name_len):
                        new_info.write('-')
                    new_info.write('500')
                    new_info.close()

                    # Same procedure as if trying to connect once account is created
                    info = open("info.txt", "r")
                    for line in info.readlines():
                        if line[:user_name_len] == registerInput.text:
                            print("Welcome %s" % registerInput.text)
                            chips = int(line[20:])  # No \n there
                            info.close()
                            user_name = str(registerInput.text)
                            game_choice(user_name, line, chips)
            registerInput.handle_event(event)


def game_choice(user_name, line, chips):
    running = True
    bjButton = Button((255, 255, 255), 50, 50, 300, 100, 'Black Jack')
    rouletteButton = Button((255, 255, 255), 50, 200, 300, 100, 'Roulette')
    smButton = Button((255, 255, 255), 50, 350, 300, 100, 'Slot machines')
    exitButton = Button((255, 255, 255), 50, 550, 300, 100, 'Save & Exit')
    chips_txt = font.render(str(chips) + ' chips', True, (0, 0, 0))

    while running:
        screen.fill((170, 170, 170))
        bjButton.draw(screen, (0, 0, 0))
        rouletteButton.draw(screen, (0, 0, 0))
        smButton.draw(screen, (0, 0, 0))
        exitButton.draw(screen, (0, 0, 0))
        screen.blit(chips_txt, (x - chips_txt.get_width() - 50, 50))
        pygame.display.update()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                stop(user_name, line, chips)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bjButton.isOver(pos):
                    running = False
                    black_jack(user_name, line, chips)
                if rouletteButton.isOver(pos):
                    running = False
                    roulette(user_name, line, chips)
                if smButton.isOver(pos):
                    running = False
                    slot_machines(user_name, line, chips)
                if exitButton.isOver(pos):
                    stop(user_name, line, chips)


def black_jack(user_name, line, chips):  # draw cards on screen 1 by 1
    global qt_error_chips, cards, p_cards, p_total, d_cards, dbj_finish
    running = True
    start = False
    nb_error_chips = False
    crd_1 = False
    crd_2 = False
    crd_3 = False
    crd_4 = False
    crd_5 = False
    crd_6 = False
    dcrd_1 = False
    card_pos = 2
    dcard_pos = 2
    info_crd = []
    info_dcrd = []
    chips_txt = font.render(str(chips) + ' chips', True, (0, 0, 0))
    returnButton = Button((255, 255, 255), 10, 10, 150, 50, 'Return')
    betButton = Button((255, 255, 255), 520, y - 90, 90, 80, 'Bet')
    hitButton = Button((255, 255, 255), x - 160, 400, 150, 50, 'Hit')
    standButton = Button((255, 255, 255), x - 160, 460, 150, 50, 'Stand')
    input_chips = InputBox(10, y - 90, 10, 80)
    input_txt = font.render('Bet', True, (0, 0, 0))
    win_txt = font.render('You win', True, (0, 255, 0))
    lose_txt = font.render('You lose', True, (255, 0, 0))
    draw_txt = font.render('Draw', True, (0, 0, 0))
    nb_error_chips_txt = e_font.render('You must enter a valid number', True, (255, 0, 0))
    qt_error_chips_txt = e_font.render('You can\'t bet more than you have', True, (255, 0, 0))

    while running:
        screen.fill((170, 170, 170))
        returnButton.draw(screen, (0, 0, 0))
        betButton.draw(screen, (0, 0, 0))
        hitButton.draw(screen, (0, 0, 0))
        standButton.draw(screen, (0, 0, 0))
        input_chips.update()
        input_chips.draw(screen)
        screen.blit(input_txt, (10, y - 90 - input_txt.get_height()))
        screen.blit(chips_txt, (x - chips_txt.get_width() - 50, y - 50 - chips_txt.get_height()))
        if nb_error_chips:
            screen.blit(nb_error_chips_txt, (110, int(y - 90 - nb_error_chips_txt.get_height())))
        if qt_error_chips:
            screen.blit(qt_error_chips_txt, (110, int(y - 132 - qt_error_chips_txt.get_height())))
        if crd_1:
            screen.blit(info_crd[0][0], (50, 100))
        if crd_2:
            screen.blit(info_crd[1][0], (240, 100))
        if crd_3:
            screen.blit(info_crd[2][0], (430, 100))
        if crd_4:
            screen.blit(info_crd[3][0], (620, 100))
        if crd_5:
            screen.blit(info_crd[4][0], (810, 100))
        if crd_6:
            screen.blit(info_crd[5][0], (1000, 100))
        if dcrd_1:
            screen.blit(info_dcrd[0][0], (50, 340))
            screen.blit(cbb, (240, 340))
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                stop(user_name, line, chips)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if returnButton.isOver(pos):
                    game_choice(user_name, line, chips)
                if betButton.isOver(pos) and not start:
                    if input_chips.text.isdigit():
                        nb_error_chips = False
                        p_total = 0
                        cards = [c2, c3, c4, c5, c6, c7, c8, c9, c10, cj, cq, ck, ca, d2, d3, d4, d5, d6, d7, d8, d9,
                                 d10, dj, dq, dk, da, h2, h3, h4, h5, h6, h7, h8, h9, h10, hj, hq, hk, ha, s2, s3, s4,
                                 s5, s6, s7, s8, s9, s10, sj, sq, sk, sa]
                        p_cards = []
                        d_cards = []
                        dbj_finish = False

                        if int(input_chips.text) > chips:
                            print("You can't bet more than you have\n")
                            qt_error_chips = True
                            black_jack(user_name, line, chips)
                        else:
                            qt_error_chips = False
                        for i in range(2):  # Remove cards 1 by 1 from the original deck while adding it to the player
                            # and dealer hand
                            # Player
                            r_cards = random.choice(cards)
                            p_cards.append(r_cards[1])
                            info_crd.append(r_cards)
                            p_total += r_cards[1]
                            cards.remove(r_cards)
                            if i == 0:
                                crd_1 = True
                            if i == 1:
                                crd_2 = True

                            # Dealer
                            r_cards = random.choice(cards)
                            d_cards.append(r_cards[1])
                            cards.remove(r_cards)
                            info_dcrd.append(r_cards)
                            dcrd_1 = True
                            pygame.display.update()
                        print('The dealer has a ' + str(d_cards[0]))
                        start = True
                        # if p_total == 21:
                        #     print('Black Jack')
                        #     chips += int(input_chips.text) * 2
                    else:
                        nb_error_chips = True

                # Actions
                if hitButton.isOver(pos) and start:
                    card_pos += 1
                    r_cards = random.choice(cards)
                    p_cards.append(r_cards[1])
                    info_crd.append(r_cards)
                    p_total += r_cards[1]
                    cards.remove(r_cards)
                    print('Your hand is {} ({})\n'.format(p_cards, p_total))
                    if p_total >= 22:
                        print('Busted')
                        chips -= int(input_chips.text)
                        screen.blit(lose_txt, (int(x / 2 - lose_txt.get_width() / 2), int(y / 2 - lose_txt.get_height() / 2)))
                        screen.blit(info_crd[card_pos - 1][0], (50 + 190 * (card_pos - 1), 100))
                        pygame.display.update()
                        time.sleep(2.5)
                        black_jack(user_name, line, chips)
                    if card_pos == 3:
                        crd_3 = True
                    if card_pos == 4:
                        crd_4 = True
                    if card_pos == 5:
                        crd_5 = True
                    if card_pos == 6:
                        crd_6 = True

                elif standButton.isOver(pos) and start:
                    screen.blit(info_dcrd[1][0], (240, 340))
                    pygame.display.update()
                    time.sleep(1)

                    while not dbj_finish:  # Dealers turn
                        d_total = 0
                        for a in d_cards:
                            d_total += a
                        if d_total >= 22:
                            print('The dealer got {} and you got {}'.format(d_total, p_total))
                            print('You win')
                            dbj_finish = True
                            chips += int(input_chips.text)
                            screen.blit(win_txt, (int(x / 2 - lose_txt.get_width() / 2), int(y / 2 - lose_txt.get_height() / 2)))
                            pygame.display.update()
                            time.sleep(2.5)
                            black_jack(user_name, line, chips)
                        elif d_total < 17:
                            dcard_pos += 1
                            r_cards = random.choice(cards)
                            d_cards.append(r_cards[1])
                            cards.remove(r_cards)
                            info_dcrd.append(r_cards)
                            if dcard_pos == 3:
                                screen.blit(info_dcrd[2][0], (430, 340))
                            if dcard_pos == 4:
                                screen.blit(info_dcrd[3][0], (620, 340))
                            if dcard_pos == 5:
                                screen.blit(info_dcrd[4][0], (810, 340))
                            if dcard_pos == 6:
                                screen.blit(info_dcrd[5][0], (1000, 340))
                            pygame.display.update()
                            time.sleep(1.5)
                        else:
                            print('The dealer got {} and you got {}'.format(d_total, p_total))
                            dbj_finish = True
                            if p_total < d_total:
                                print('You lose')
                                chips -= int(input_chips.text)
                                screen.blit(lose_txt, (int(x / 2 - lose_txt.get_width() / 2), int(y / 2 - lose_txt.get_height() / 2)))
                            elif p_total > d_total:
                                print('You win')
                                chips += int(input_chips.text)
                                screen.blit(win_txt, (int(x / 2 - lose_txt.get_width() / 2), int(y / 2 - lose_txt.get_height() / 2)))
                            else:
                                print('Draw')
                                screen.blit(draw_txt, (int(x / 2 - lose_txt.get_width() / 2), int(y / 2 - lose_txt.get_height() / 2)))
                            pygame.display.update()
                            time.sleep(2.5)
                            black_jack(user_name, line, chips)

            input_chips.handle_event(event)
        pygame.display.update()


def roulette(user_name, line, chips):  # play sound when betting on each categories
    running = True
    nb_error_chips = False
    qt_error_chips2 = False
    chips_txt = font.render(str(chips) + ' chips', True, (0, 0, 0))
    returnButton = Button((255, 255, 255), 10, 10, 150, 50, 'Return')
    input_chips = InputBox(10, y - 90, 10, 80)
    input_txt = font.render('Bet', True, (0, 0, 0))
    startButton = Button((255, 255, 255), 520, y - 90, 110, 80, 'Spin')
    st12Button = Button((255, 255, 255), 212, 306, 286, 51, '1st 12')
    nd12Button = Button((255, 255, 255), 498, 306, 286, 51, '2nd 12')
    rd12Button = Button((255, 255, 255), 784, 306, 286, 51, '3rd 12')
    to18Button = Button((255, 255, 255), 212, 357, 143, 51, '1to18')
    evenButton = Button((255, 255, 255), 355, 357, 143, 51, 'EVEN')
    redButton = Button((255, 0, 0), 498, 357, 143, 51, '')
    blackButton = Button((0, 0, 0), 641, 357, 143, 51, '')
    oddButton = Button((255, 255, 255), 784, 357, 143, 51, 'ODD')
    to36Button = Button((255, 255, 255), 927, 357, 143, 51, '19to36')
    nb_error_chips_txt = e_font.render('You must enter a valid number', True, (255, 0, 0))
    qt_error_chips_txt = e_font.render('You can\'t bet more than you have', True, (255, 0, 0))

    info_text1 = e_font.render('1. Place the amount you want to bet in the "Bet" area', True, (0, 0, 0))
    info_text2 = e_font.render('2. Click on the areas where you want to place your bet', True, (0, 0, 0))
    info_text3 = e_font.render('3. Once all off the bets are placed, click on the "spin" button', True, (0, 0, 0))

    red_bet = black_bet = even_bet = odd_bet = low_bet = high_bet = st12_bet = nd12_bet = rd12_bet = t_bet = 0
    # column1_bet = column2_bet = column3_bet = 0  Maybe later

    while running:
        screen.fill((170, 170, 170))
        returnButton.draw(screen, (0, 0, 0))
        startButton.draw(screen, (0, 0, 0))
        st12Button.draw(screen, (0, 0, 0))
        nd12Button.draw(screen, (0, 0, 0))
        rd12Button.draw(screen, (0, 0, 0))
        to18Button.draw(screen, (0, 0, 0))
        evenButton.draw(screen, (0, 0, 0))
        redButton.draw(screen, (0, 0, 0))
        blackButton.draw(screen, (0, 0, 0))
        oddButton.draw(screen, (0, 0, 0))
        to36Button.draw(screen, (0, 0, 0))

        screen.blit(chips_txt, (x - chips_txt.get_width() - 50, y - 50 - chips_txt.get_height()))
        screen.blit(info_text1, (20, 110))
        screen.blit(info_text2, (20, 150))
        screen.blit(info_text3, (20, 190))
        input_chips.update()
        input_chips.draw(screen)
        screen.blit(input_txt, (10, y - 90 - input_txt.get_height()))
        if nb_error_chips:
            screen.blit(nb_error_chips_txt, (110, int(y - 90 - nb_error_chips_txt.get_height())))
        if qt_error_chips2:
            screen.blit(qt_error_chips_txt, (110, int(y - 132 - qt_error_chips_txt.get_height())))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop(user_name, line, chips)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if returnButton.isOver(pos):
                    running = False
                    game_choice(user_name, line, chips)
                if st12Button.isOver(pos):
                    if input_chips.text.isdigit():
                        nb_error_chips = False
                        if int(input_chips.text) > chips or (t_bet + int(input_chips.text)) > chips:
                            print("You can't bet more than you have\n")
                            qt_error_chips2 = True
                            continue
                        else:
                            t_bet -= st12_bet
                            qt_error_chips2 = False
                            st12_bet = int(input_chips.text)
                            t_bet += st12_bet

                    else:
                        nb_error_chips = True
                if nd12Button.isOver(pos):
                    if input_chips.text.isdigit():
                        nb_error_chips = False
                        if int(input_chips.text) > chips or (t_bet + int(input_chips.text)) > chips:
                            print("You can't bet more than you have\n")
                            qt_error_chips2 = True
                            continue
                        else:
                            t_bet -= nd12_bet
                            qt_error_chips2 = False
                            nd12_bet = int(input_chips.text)
                            t_bet += nd12_bet

                    else:
                        nb_error_chips = True
                if rd12Button.isOver(pos):
                    if input_chips.text.isdigit():
                        nb_error_chips = False
                        if int(input_chips.text) > chips or (t_bet + int(input_chips.text)) > chips:
                            print("You can't bet more than you have\n")
                            qt_error_chips2 = True
                            continue
                        else:
                            t_bet -= rd12_bet
                            qt_error_chips2 = False
                            rd12_bet = int(input_chips.text)
                            t_bet += rd12_bet

                    else:
                        nb_error_chips = True
                if to18Button.isOver(pos):
                    if input_chips.text.isdigit():
                        nb_error_chips = False
                        if int(input_chips.text) > chips or (t_bet + int(input_chips.text)) > chips:
                            print("You can't bet more than you have\n")
                            qt_error_chips2 = True
                            continue
                        else:
                            t_bet -= low_bet
                            qt_error_chips2 = False
                            low_bet = int(input_chips.text)
                            t_bet += low_bet

                    else:
                        nb_error_chips = True
                if evenButton.isOver(pos):
                    if input_chips.text.isdigit():
                        nb_error_chips = False
                        if int(input_chips.text) > chips or (t_bet + int(input_chips.text)) > chips:
                            print("You can't bet more than you have\n")
                            qt_error_chips2 = True
                            continue
                        else:
                            t_bet -= even_bet
                            qt_error_chips2 = False
                            even_bet = int(input_chips.text)
                            t_bet += even_bet

                    else:
                        nb_error_chips = True
                if redButton.isOver(pos):
                    if input_chips.text.isdigit():
                        nb_error_chips = False
                        if int(input_chips.text) > chips or (t_bet + int(input_chips.text)) > chips:
                            print("You can't bet more than you have\n")
                            qt_error_chips2 = True
                            continue
                        else:
                            t_bet -= red_bet
                            qt_error_chips2 = False
                            red_bet = int(input_chips.text)
                            t_bet += red_bet

                    else:
                        nb_error_chips = True
                if blackButton.isOver(pos):
                    if input_chips.text.isdigit():
                        nb_error_chips = False
                        if int(input_chips.text) > chips or (t_bet + int(input_chips.text)) > chips:
                            print("You can't bet more than you have\n")
                            qt_error_chips2 = True
                            continue
                        else:
                            t_bet -= black_bet
                            qt_error_chips2 = False
                            black_bet = int(input_chips.text)
                            t_bet += black_bet

                    else:
                        nb_error_chips = True
                if oddButton.isOver(pos):
                    if input_chips.text.isdigit():
                        nb_error_chips = False
                        if int(input_chips.text) > chips or (t_bet + int(input_chips.text)) > chips:
                            print("You can't bet more than you have\n")
                            qt_error_chips2 = True
                            continue
                        else:
                            t_bet -= odd_bet
                            qt_error_chips2 = False
                            odd_bet = int(input_chips.text)
                            t_bet += odd_bet

                    else:
                        nb_error_chips = True
                if to36Button.isOver(pos):
                    if input_chips.text.isdigit():
                        nb_error_chips = False
                        if int(input_chips.text) > chips or (t_bet + int(input_chips.text)) > chips:
                            print("You can't bet more than you have\n")
                            qt_error_chips2 = True
                            continue
                        else:
                            t_bet -= high_bet
                            qt_error_chips2 = False
                            high_bet = int(input_chips.text)
                            t_bet += high_bet

                    else:
                        nb_error_chips = True

                if startButton.isOver(pos):
                    print(t_bet)
                    chips -= red_bet
                    chips -= black_bet
                    chips -= even_bet
                    chips -= odd_bet
                    chips -= low_bet
                    chips -= high_bet
                    chips -= st12_bet
                    chips -= nd12_bet
                    chips -= rd12_bet
                    print('Bets are placed')
                    wheel = random.randint(0, 36)
                    time.sleep(.5)

                    # Checking for rewards
                    if wheel in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]:
                        chips += red_bet * 2
                    elif wheel in [2, 4, 6, 8, 10, 11, 13, 15, 18, 20, 22, 24, 26, 28, 29, 31, 33, 35]:
                        chips += black_bet * 2
                    if wheel % 2 == 0:
                        chips += even_bet * 2
                    elif wheel % 2 != 0:
                        chips += odd_bet * 2
                    if 1 <= wheel <= 18:
                        chips += low_bet * 2
                    elif wheel > 18:
                        chips += high_bet * 2
                    if 1 <= wheel <= 12:
                        chips += st12_bet * 3
                    elif 13 <= wheel <= 24:
                        chips += nd12_bet * 3
                    elif 25 <= wheel <= 36:
                        chips += rd12_bet * 3

                    if wheel in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]:
                        screen.blit(font.render('The ball landed on ' + str(wheel), True, (255, 0, 0)), (500, 500))
                    else:
                        screen.blit(font.render('The ball landed on ' + str(wheel), True, (0, 0, 0)), (500, 500))
                    pygame.display.update()
                    time.sleep(3)
                    roulette(user_name, line, chips)

                    print('You have %s chips left!' % chips)

            input_chips.handle_event(event)
        pygame.display.update()


def slot_machines(user_name, line, chips):
    running = True
    nb_error_chips = False
    qt_error_chips3 = False
    chips_txt = font.render(str(chips) + ' chips', True, (0, 0, 0))
    rules_txt1 = e_font.render('Different values:', True, (0, 0, 0))
    rules_txt2 = e_font.render('- 1 dog: x2', True, (0, 0, 0))
    rules_txt3 = e_font.render('- 2 dogs: x3', True, (0, 0, 0))
    rules_txt4 = e_font.render('- 3 cats: x5', True, (0, 0, 0))
    rules_txt5 = e_font.render('- 3 monkeys: x30', True, (0, 0, 0))
    rules_txt6 = e_font.render('- 3 penguins: x80', True, (0, 0, 0))
    rules_txt7 = e_font.render('- 3 parrots: x120', True, (0, 0, 0))
    rules_txt8 = e_font.render('- 3 foxes: x200', True, (0, 0, 0))
    rules_txt9 = e_font.render('- 3 dogs: x500', True, (0, 0, 0))
    rules_txt10 = e_font.render('- 3 flamingos: x1000', True, (0, 0, 0))
    rules_txt11 = e_font.render('- 3 sharks: x2500', True, (0, 0, 0))
    returnButton = Button((255, 255, 255), 10, 10, 150, 50, 'Return')
    betButton = Button((255, 255, 255), 520, y - 90, 90, 80, 'Roll')
    input_chips = InputBox(10, y - 90, 10, 80)
    input_txt = font.render('Bet', True, (0, 0, 0))
    nb_error_chips_txt = e_font.render('You must enter a valid number', True, (255, 0, 0))
    qt_error_chips_txt = e_font.render('You can\'t bet more than you have', True, (255, 0, 0))
    while running:
        screen.fill((170, 170, 170))
        returnButton.draw(screen, (0, 0, 0))
        betButton.draw(screen, (0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(100, 200, 200, 200))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(100, 200, 200, 200), 4)
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(350, 200, 200, 200))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(350, 200, 200, 200), 4)
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(600, 200, 200, 200))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(600, 200, 200, 200), 4)

        screen.blit(chips_txt, (x - chips_txt.get_width() - 50, y - 50 - chips_txt.get_height()))
        screen.blit(input_txt, (10, y - 90 - input_txt.get_height()))
        screen.blit(rules_txt1, (850, 50))
        screen.blit(rules_txt2, (870, 100))
        screen.blit(rules_txt3, (870, 150))
        screen.blit(rules_txt4, (870, 200))
        screen.blit(rules_txt5, (870, 250))
        screen.blit(rules_txt6, (870, 300))
        screen.blit(rules_txt7, (870, 350))
        screen.blit(rules_txt8, (870, 400))
        screen.blit(rules_txt9, (870, 450))
        screen.blit(rules_txt10, (870, 500))
        screen.blit(rules_txt11, (870, 550))
        input_chips.update()
        input_chips.draw(screen)
        if nb_error_chips:
            screen.blit(nb_error_chips_txt, (110, int(y - 90 - nb_error_chips_txt.get_height())))
        if qt_error_chips3:
            screen.blit(qt_error_chips_txt, (110, int(y - 132 - qt_error_chips_txt.get_height())))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop(user_name, line, chips)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if returnButton.isOver(pos):
                    running = False
                    game_choice(user_name, line, chips)
                if betButton.isOver(pos):

                    if input_chips.text.isdigit():
                        nb_error_chips = False
                        if int(input_chips.text) > chips:
                            print("You can't bet more than you have\n")
                            qt_error_chips3 = True
                            continue
                        else:
                            qt_error_chips3 = False
                        wheel = [dog, cat, monkey, penguin, parrot, fox, flamingo, shark]

                        print("""Different values:\n\t- 1 dog: x2\n\t- 2 dogs: x3\n\t- 3 cats: x5\n\t- 3 monkey: x30\n\t- 3 penguin: x80
                        \t- 3 parrots: x120\n\t- 3 foxes: x200\n\t- 3 dogs: x500\n\t- 3 flamingos: x1000\n\t- 3 sharks: x2500""")

                        wheel1 = random.choices(wheel, weights=(3, 12, 10, 8, 6, 4, 2, 1),
                                                k=1)  # Everything doesn't have equal chances
                        wheel2 = random.choices(wheel, weights=(3, 12, 10, 8, 6, 4, 2, 1), k=1)  # getting picked
                        wheel3 = random.choices(wheel, weights=(3, 12, 10, 8, 6, 4, 2, 1), k=1)

                        screen.blit(wheel1[0], (100, 200))
                        pygame.display.update()
                        time.sleep(1)
                        screen.blit(wheel2[0], (350, 200))
                        pygame.display.update()
                        time.sleep(1)
                        screen.blit(wheel3[0], (600, 200))
                        pygame.display.update()
                        time.sleep(1)

                        if wheel1[0] == dog and wheel2[0] == dog and wheel3[0] == dog:
                            chips += int(input_chips.text) * 500
                        elif wheel1[0] == dog and wheel3[0] == dog:
                            chips += int(input_chips.text) * 3
                        elif wheel2[0] == dog and wheel3[0] == dog:
                            chips += int(input_chips.text) * 3
                        elif wheel2[0] == dog and wheel1[0] == dog:
                            chips += int(input_chips.text) * 3
                        elif wheel1[0] == cat and wheel2[0] == cat and wheel3[0] == cat:
                            chips += int(input_chips.text) * 5
                        elif wheel1[0] == monkey and wheel2[0] == monkey and wheel3[0] == monkey:
                            chips += int(input_chips.text) * 30
                        elif wheel1[0] == penguin and wheel2[0] == penguin and wheel3[0] == penguin:
                            chips += int(input_chips.text) * 80
                        elif wheel1[0] == parrot and wheel2[0] == parrot and wheel3[0] == parrot:
                            chips += int(input_chips.text) * 120
                        elif wheel1[0] == fox and wheel2[0] == fox and wheel3[0] == fox:
                            chips += int(input_chips.text) * 200
                        elif wheel1[0] == flamingo and wheel2[0] == flamingo and wheel3[0] == flamingo:
                            chips += int(input_chips.text) * 1000
                        elif wheel1[0] == shark and wheel2[0] == shark and wheel3[0] == shark:
                            chips += int(input_chips.text) * 2500
                        elif dog in (wheel1[0], wheel2[0], wheel3[0]):
                            chips += int(input_chips.text) * 2
                        else:
                            chips -= int(input_chips.text)
                            print('Better luck next time')

                        slot_machines(user_name, line, chips)

                    else:
                        nb_error_chips = True

            input_chips.handle_event(event)
        pygame.display.update()


def stop(user_name, line, chips):
    info = open("info.txt", "rt")
    data = info.read()
    data = data.replace(line, '')
    info.close()
    info = open("info.txt", "wt")
    info.write(str(user_name))
    for i in range(20 - len(str(user_name))):
        info.write('-')
    info.write(str(chips) + '\n')
    info.write(str(data))
    info.close()
    quit()

    info.write('\n' + line[:user_name] + str(chips))


start_menu()
