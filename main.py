import time
import random


def login():
    user_name = str(input('Enter your username, or type "new" to create an account\n'))
    user_name_len = len(user_name)

    # For new accounts
    if user_name == 'new':
        # Check if username doesn't already exists
        user_name = input('Enter your username\n')
        if len(user_name) > 20:
            print("A username can't be above 20 characters")
            login()
        user_name_len = len(user_name)
        info = open("info.txt", "r")
        for line in info.readlines():
            if line[:len(user_name)] == user_name or user_name == 'new':
                print("You can't create an account with an already existing name")
                info.close()
                login()
            else:
                pass
        info.close()
        print('Account created successfully')

        # Adds new name to txt file
        new_info = open("info.txt", "a")
        new_info.write(user_name)
        for i in range(20 - user_name_len):
            new_info.write('-')
        new_info.write('500')
        new_info.close()

        # Same procedure as if trying to connect once account is created
        info = open("info.txt", "r")
        for line in info.readlines():
            if line[:user_name_len] == user_name:
                print("Welcome %s" % user_name)
                chips = int(line[20:])  # No \n there
                info.close()
                game_choice(chips, line, user_name)
            else:
                pass

    # Search for account
    info = open("info.txt", "r")

    for line in info.readlines():
        if line[:user_name_len] == user_name and line[user_name_len + 1] == '-':
            print("Welcome %s" % user_name)
            chips = int(line[20:-1])
            info.close()
            game_choice(chips, line, user_name)
        else:
            pass
    print('Username %s does not exist' % user_name)
    login()

    info.close()


def game_choice(chips, line, user_name):
    print('You have {} chips'.format(chips))
    nxt_game = str(input('Choose your game :\n\t1. Black Jack\n\t2. Roulette\n\t3. Slot machine\n\n\t4. Quit\n\n'))
    if nxt_game.lower() == 'black jack' or nxt_game.lower() == '1':
        black_jack(chips, line, user_name)
    elif nxt_game.lower() == 'roulette' or nxt_game.lower() == '2':
        roulette(chips, line, user_name)
    elif nxt_game.lower() == 'slot machine' or nxt_game.lower() == '3':
        slot_machine(chips, line, user_name)
    elif nxt_game.lower() == 'quit' or nxt_game.lower() == '4':
        info = open("info.txt", "rt")
        data = info.read()
        data = data.replace(line, '')
        info.close()
        info = open("info.txt", "wt")
        info.write(user_name)
        for i in range(20 - len(user_name)):
            info.write('-')
        info.write(str(chips) + '\n')
        info.write(data)
        info.close()
        quit()

        info.write('\n' + line[:user_name] + chips)
    else:
        game_choice(chips, line, user_name)


def black_jack(chips, line, user_name):
    print('You have {} chips'.format(chips))
    p_total = 0
    j = q = k = 10
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, j, q, k] * 4
    p_cards = []
    d_cards = []
    pbj_finish = False
    dbj_finish = False

    bet = int(input('Choose your bet size:\n'))
    if bet > chips:
        print("You can't bet more than you have\n")
        black_jack(chips, line, user_name)
    else:
        pass
    for i in range(2):  # Remove cards 1 by 1 from the original deck while adding it to the player and dealer hand
        # Player
        r_cards = random.choice(cards)
        p_cards.append(r_cards)
        cards.remove(r_cards)
        # Dealer
        r_cards = random.choice(cards)
        d_cards.append(r_cards)
        cards.remove(r_cards)
    print('The dealer has a ' + str(d_cards[0]))

    while not pbj_finish:  # Player chooses his action
        p_total = 0
        for a in p_cards:
            p_total += a
        # Cards total
        print('Your hand is {} ({})\n'.format(p_cards, p_total))
        if p_total >= 22:
            print('Busted')
            pbj_finish = True
            chips -= bet
            game_choice(chips, line, user_name)
        elif p_total == 21:
            print('Black Jack')
            chips += bet * 1.5
        else:
            pass

        action = input('\t- Hit\n\t- Stand\n\n')
        # Actions
        if action.lower() == 'hit':
            r_cards = random.choice(cards)
            p_cards.append(r_cards)
            cards.remove(r_cards)

        elif action.lower() == 'stand':
            pbj_finish = True
            time.sleep(.75)

    while not dbj_finish:  # Dealers turn
        d_total = 0
        for a in d_cards:
            d_total += a
        if d_total >= 22:
            print('The dealer got {} and you got {}'.format(d_total, p_total))
            print('You win')
            dbj_finish = True
            chips += bet
            game_choice(chips, line, user_name)
        elif d_total < 17:
            r_cards = random.choice(cards)
            d_cards.append(r_cards)
            cards.remove(r_cards)
        else:
            print('The dealer got {} and you got {}'.format(d_total, p_total))
            dbj_finish = True
            if p_total < d_total:
                print('You lose')
                chips -= bet
            elif p_total > d_total:  # Bug here
                print('You win')
                chips += bet
            else:
                print('Draw')
            game_choice(chips, line, user_name)


def slot_machine(chips, line, user_name):
    print('You have {} chips'.format(chips))
    wheel = ['dog', 'cat', 'monkey', 'penguin', 'parrot', 'fox', 'flamingo', 'shark']

    print("""Different values:\n\t- 1 dog: x2\n\t- 2 dogs: x3\n\t- 3 cats: x5\n\t- 3 monkey: x30\n\t- 3 penguin: x80
\t- 3 parrots: x120\n\t- 3 foxes: x200\n\t- 3 dogs: x500\n\t- 3 flamingos: x1000\n\t- 3 sharks: x2500""")

    bet = int(input("Choose your bet size:\n"))
    if bet > chips:
        print("You can't bet more than you have\n")
        slot_machine(chips, line, user_name)
    else:
        time.sleep(.5)

    wheel1 = random.choices(wheel, weights=(3, 12, 10, 8, 6, 4, 2, 1), k=1)  # Everything doesn't have equal chances
    # wheel2 = random.choices(wheel, weights=(3, 12, 10, 8, 6, 4, 2, 1), k=1)  # getting picked
    # wheel3 = random.choices(wheel, weights=(3, 12, 10, 8, 6, 4, 2, 1), k=1)

    wheel2 = wheel3 = ['dog']

    print(wheel1, wheel2, wheel3)

    if wheel1 == ['dog'] and wheel2 == ['dog'] and wheel3 == ['dog']:
        chips += bet * 500
        print('You won {}!'.format(bet * 500))
    elif wheel1 == ['dog'] and wheel3 == ['dog']:
        chips += bet * 3
        print('You won {}!'.format(bet * 3))
    elif wheel2 == ['dog'] and wheel3 == ['dog']:
        chips += bet * 3
        print('You won {}!'.format(bet * 3))
    elif wheel2 == ['dog'] and wheel1 == ['dog']:
        chips += bet * 3
        print('You won {}!'.format(bet * 3))
    elif wheel1 == ['cat'] and wheel2 == ['cat'] and wheel3 == ['cat']:
        chips += bet * 5
        print('You won {}!'.format(bet * 5))
    elif wheel1 == ['monkey'] and wheel2 == ['monkey'] and wheel3 == ['monkey']:
        chips += bet * 30
        print('You won {}!'.format(bet * 30))
    elif wheel1 == ['penguin'] and wheel2 == ['penguin'] and wheel3 == ['penguin']:
        chips += bet * 80
        print('You won {}!'.format(bet * 80))
    elif wheel1 == ['parrot'] and wheel2 == ['parrot'] and wheel3 == ['parrot']:
        chips += bet * 120
        print('You won {}!'.format(bet * 120))
    elif wheel1 == ['fox'] and wheel2 == ['fox'] and wheel3 == ['fox']:
        chips += bet * 200
        print('You won {}!'.format(bet * 200))
    elif wheel1 == ['flamingo'] and wheel2 == ['flamingo'] and wheel3 == ['flamingo']:
        chips += bet * 1000
        print('You won {}!'.format(bet * 1000))
    elif wheel1 == ['shark'] and wheel2 == ['shark'] and wheel3 == ['shark']:
        chips += bet * 2500
        print('You won {}!'.format(bet * 2500))
    elif ['dog'] in (wheel1, wheel2, wheel3):
        chips += bet * 2
        print('You won {}!'.format(bet * 2))
    else:
        chips -= bet
        print('Better luck next time')
    again = str(input('Press enter to keep playing or "exit" to change game\n'))
    if again == '':
        slot_machine(chips, line, user_name)
    else:
        game_choice(chips, line, user_name)


def roulette(chips, line, user_name):
    print('You have %s chips' % chips)
    red_bet = black_bet = even_bet = odd_bet = low_bet = high_bet = st12_bet = nd12_bet = rd12_bet = 0
    column1_bet = column2_bet = column3_bet = t_bet = 0
    bets = False
    while not bets:
        z_bet = input("""Where do you want to bet?\n\t1. Red /2. Black\n\t3. Even /4. Odd
\t5. Low (1 to 18) /6. High (19 to 36)\n\t7. 1st12 /8. 2nd12 /9. 3rd12\n\t10. Column 1 /11. Column 2 /12. Column 3
\n\t13. Spin\n""")  # Outside bets for now
        if z_bet.lower() == 'red' or z_bet.lower() == '1':
            red_bet = int(input('How much\n'))
            t_bet += red_bet
        elif z_bet.lower() == 'black' or z_bet.lower() == '2':
            black_bet = int(input('How much\n'))
            t_bet += black_bet
        elif z_bet.lower() == 'even' or z_bet.lower() == '3':
            even_bet = int(input('How much\n'))
            t_bet += even_bet
        elif z_bet.lower() == 'odd' or z_bet.lower() == '4':
            odd_bet = int(input('How much\n'))
            t_bet += odd_bet
        elif z_bet.lower() == 'low' or z_bet.lower() == '5':
            low_bet = int(input('How much\n'))
            t_bet += low_bet
        elif z_bet.lower() == 'high' or z_bet.lower() == '6':
            high_bet = int(input('How much\n'))
            t_bet += high_bet
        elif z_bet.lower() == '1st12' or z_bet.lower() == '7':
            st12_bet = int(input('How much\n'))
            t_bet += st12_bet
        elif z_bet.lower() == '2nd12' or z_bet.lower() == '8':
            nd12_bet = int(input('How much\n'))
            t_bet += nd12_bet
        elif z_bet.lower() == '3rd12' or z_bet.lower() == '9':
            rd12_bet = int(input('How much\n'))
            t_bet += rd12_bet
        elif z_bet.lower() == 'column 1' or z_bet.lower() == '10':
            column1_bet = int(input('How much\n'))
            t_bet += column1_bet
        elif z_bet.lower() == 'column 2' or z_bet.lower() == '11':
            column2_bet = int(input('How much\n'))
            t_bet += column2_bet
        elif z_bet.lower() == 'column 3' or z_bet.lower() == '12':
            column3_bet = int(input('How much\n'))
            t_bet += column3_bet
        elif z_bet.lower() == 'spin' or z_bet.lower() == '13':
            if t_bet > chips:
                print("You can't bet more than you have!\nRestarting...")
                roulette(chips, line, user_name)
            else:
                bets = True
                chips -= red_bet
                chips -= black_bet
                chips -= even_bet
                chips -= odd_bet
                chips -= low_bet
                chips -= high_bet
                chips -= st12_bet
                chips -= nd12_bet
                chips -= rd12_bet
                chips -= column1_bet
                chips -= column2_bet
                chips -= column3_bet
                print('Bets are placed')
    wheel = random.randint(0, 36)
    time.sleep(.5)
    print('The ball landed on %s !' % wheel)
    time.sleep(1)

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
    if wheel in [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]:
        chips += column1_bet * 3
    elif wheel in [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]:
        chips += column2_bet * 3
    elif wheel in [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]:
        chips += column3_bet * 3

    print('You have %s chips left!' % chips)
    again = input('Press enter to keep playing or "exit" to change game\n')
    if again == '':
        roulette(chips, line, user_name)
    else:
        game_choice(chips, line, user_name)


login()
