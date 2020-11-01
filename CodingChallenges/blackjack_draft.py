import random

# Global variables for card deck
cards = {'A':(1, 11), '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}
card_deck = [card for card in cards.keys()] * 4
random.shuffle(card_deck)

def initial_deal():
    """ Deal initial 2 cards """
    dealer_cards = [card_deck.pop(), card_deck.pop()]
    print('Dealer has: ? ', end='')
    display_hidden_hand(dealer_cards)

    player_cards = [card_deck.pop(), card_deck.pop()]
    print('Player has: ', end='')
    display_hand(player_cards)

    return dealer_cards, player_cards

def display_hidden_hand(players):
    """ Display current hands """
    print(*players[1:], sep=' ', end='')
    print(' = ?')

def display_hand(players):
    """ Display current hands """
    print(*players, sep=' ', end='')
    print(' =', calc_total(players))

def deal_card(players):
    """ Deal single card """
    players.append(card_deck.pop())
    return players

def calc_total(players):
    """ Calculate current card total """
    initial_card_value = []
    a_value = 0
    for value in players:
        if value == 'A':
            a_value += 1
            initial_card_value.append(cards[value][1])
        else:
            initial_card_value.append(cards[value])
    total = sum(initial_card_value)

    if a_value != 0 and total > 21:
        total -= 10
        a_value -= 1

    return total

def blackjack():
    """ Function to handle BlackJack game's logic """

    print('* Welcome to BlackJack *\n')
    dealer, player = initial_deal()

    player_status = ''

    # Player's turn
    while True:
        if calc_total(player) > 21:
            player_status = 'lost'
            break
        elif calc_total(player) == 21:
            player_status = 'win'
            break

        # Player Hits or Stands
        input_key = input('Would you like to (H)it or (S)tand? ').upper()
        print('')
        if input_key == 'H':
            player = deal_card(player)
            if calc_total(player) <= 21:
                print('Dealer has: ? ', end='')
                display_hidden_hand(dealer)
            print('Player has: ', end='')
            display_hand(player)
        elif input_key == 'S':
            print('Player stands with: ', end='')
            display_hand(player)
            print('')
            break
        else:
            print('Invalid input. Please enter H or S')

    # ** Final outcome **

    # BlackJack Case
    if player_status == 'win':
        print('Player wins!')
        print('BlackJack!')
        pass

    else:
        # If player is busted
        if player_status == 'lost':
            print('Player busts with', calc_total(player))
            print('Dealer wins')
        # Dealer's turn
        else:
            # Dealer keeps hitting until 17
            while calc_total(dealer) <= 17:
                print('Dealer has: ', end='')
                display_hand(dealer)
                dealer = deal_card(dealer)
                print('Dealer hits')
            print('Dealer has: ', end='')
            display_hand(dealer)
            print('Dealer stands')

            # Final total comparision if player hasn't won or lost
            if calc_total(dealer) > 21:
                print('\nPlayer wins!')
            elif calc_total(dealer) == 21:
                print('Dealer wins!')
                print('BlackJack!')
            elif calc_total(player) > calc_total(dealer):
                print('\nPlayer Wins!')
                print(*player, sep=' ', end='')
                print(' =', calc_total(player), "to Dealer's ", end='')
                print(*dealer, sep=' ', end='')
                print(' =', calc_total(dealer))
            else:
                print('\nDealer wins')
                print(*dealer, sep=' ', end='')
                print(' =', calc_total(dealer), "to Player's ", end='')
                print(*player, sep=' ', end='')
                print(' =', calc_total(player))


if __name__ == "__main__":
    blackjack()
