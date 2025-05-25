#Rules: 1. If cards in your hand go over 21, bust, you lose.
#       2. 2 - 10 = face value, jack,king,queen = 10, ace = 1/11
#       3. At the beginning, dealer deals 2 cards each and shows 1 of his and 2 of yours
#       4. If you ask for more cards: if under or equal to 21, repeat till you stop. Then compare with dealer if dealer total < 17, dealer must draw another card.
#                                                                        If dealer>your_total and <=21, dealer wins,
#                                                                        Elif, dealer<your_total, you win,
#                                                                        Eliif, dealer = your_total, draw.
#       Assuming that the deck is unlimited so as to not complicate the project.

import random
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def calculatetotal(hand):
    """Calculates total value of a hand"""
    return sum(hand)

def deal(player_total,player_hand,dealer_total,dealer_hand):
    """Deals 2 cards to the player and the dealer. Used at the start of the game"""
    for i in range(2):
        player_hand.append(random.choice(cards))
    for i in range(2):
        dealer_hand.append(random.choice(cards))
    player_total = calculatetotal(player_hand)
    dealer_total = calculatetotal(dealer_hand)
    return player_total,player_hand,dealer_total,dealer_hand

def draw(total,hand):
    """Draws another card and adds to the total"""
    hand.append(random.choice(cards))
    total = calculatetotal(hand)
    if total > 21:
        if 11 in hand:
            index = hand.index(11)
            hand[index] = 1
    return total,hand

def showhand(player_total,player_hand,dealer_total,dealer_hand,drawMore):
    """Shows hand to the player, if the player busts, returns final tally and sets drawmore to no."""
    if player_total>21:
        if 11 in player_hand:
            index = player_hand.index(11)
            player_hand[index] = 1
        else:
            print(f"\t Your final hand: {player_hand}, final score: {player_total} \n\tComputer's final hand: [{dealer_hand[0]}], final score: {dealer_hand[0]}")
            print("You went over. You lose 😭")
            drawMore = "n"
            return drawMore
    print(f"\tYour cards: {player_hand}, current score: {player_total} \n\tComputer's first card: {dealer_hand[0]}")
    drawMore = input("Type 'y' to get another card, type 'n' to pass: ")
    return drawMore

def finalresult(player_total,player_hand,dealer_total,dealer_hand):
    while dealer_total < 17:
        dealer_total,dealer_hand = draw(dealer_total,dealer_hand)
    if player_total <= 21:
        print(f"\t Your final hand: {player_hand}, final score: {player_total} \n\tComputer's final hand: {dealer_hand}, final score: {dealer_total}")
        if dealer_total > player_total:
            print("You lose 😤")
        elif dealer_total == player_total:
            print("Draw 🙃")
        elif dealer_total < player_total:
            if dealer_total > 21:
                print("Opponent went over. You win 😁")
            else:
                print("You win 😁")

while True:
    player_total = 0
    dealer_total = 0
    player_hand = []
    dealer_hand = []
    doContinue = ""
    drawMore = ""
    doContinue = input("Do you want to want to play a game of Blackjack? Type 'y' or 'n': ")
    if doContinue == "y":
        print("\n"*100)
        print(logo)
        player_total,player_hand,dealer_total,dealer_hand = deal(player_total,player_hand,dealer_total,dealer_hand)
        drawMore = showhand(player_total,player_hand,dealer_total,dealer_hand,drawMore)
        while drawMore == "y":
            player_total,player_hand = draw(player_total,player_hand)
            drawMore = showhand(player_total,player_hand,dealer_total,dealer_hand,drawMore)
        finalresult(player_total,player_hand,dealer_total,dealer_hand)
    elif doContinue == "n":
        break