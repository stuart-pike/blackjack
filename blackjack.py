import random, os


def cls():  # Cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return(random.choice(cards))


def check_hand(hand):
    if hand[0] == 11 & hand[1] == 11:
        return(True)


def score(p_hand, d_hand):
    print(f"    your cards: {p_hand}, current score: {sum(p_hand)}")
    print(f"    Dealer's card: {d_hand[0]}")


def score_final(p_hand, d_hand):
    print(f"    Player's final hand: {p_hand}, final score: {sum(p_hand)}")
    print(f"    Dealer's final hand: {d_hand}, final score: {sum(d_hand)}")


def compare_hands(p_hand, d_hand):
    if sum(d_hand) > 21 or sum(d_hand) < sum(p_hand):
        score_final(p_hand, d_hand)
        return "    Ka-ching! Player wins"
    elif sum(d_hand) > sum(p_hand):
        score_final(p_hand, d_hand)
        return "    Hand over your money, haha, loser"
    elif sum(d_hand) == sum(p_hand):
        score_final(p_hand, d_hand)
        return "Booring, It's a tie!"


def start_game():

    dealer_hand = []
    player_hand = []
    deal = True
    play = input("Do you want to play a game of Blackjack 'y' or 'n': ")
    if play != 'y':
        exit()
    else:
        cls()
        for _ in range(0, 2):
            player_hand.append(int(deal_card()))
            dealer_hand.append(int(deal_card()))

    # if both cards are an Aces replace one of them
    if check_hand(player_hand):
        player_hand[0] = 1
    if check_hand(dealer_hand):
        dealer_hand[0] = 1

    # Check if there a Blackjack, there maybe a winner
    if sum(player_hand) == 21 and sum(dealer_hand) < 21:
        print("    Blackjack! You win moola")
        start_game()
    elif sum(player_hand) < 21 and sum(dealer_hand) == 21:
        print("    Dealer's BlackJack wins")
        start_game()
    elif sum(player_hand) == 21 and sum(dealer_hand) == 21:
        print("    Even-Steven")
        start_game()

    # Print initial Player and Dealer hand
    score(player_hand, dealer_hand)

    # Keep dealing cards to player until they hold or go bust.
    while deal:
        another_card = input("Type 'y' to get another card, type 'h' to hold: ")
        if another_card == 'y':
            player_hand.append(int(deal_card()))
            last_card = int(player_hand[len(player_hand) - 1])
            if sum(player_hand) > 21 and last_card != 11:
                print("    You bust!ard ")
                start_game()
            elif last_card == 11:
                player_hand[len(player_hand) - 1] == 1
            score(player_hand, dealer_hand)
        else:
            deal = False

    # Dealer must draw card if their hand is below 17
    while sum(dealer_hand) <= 16:
        dealer_hand.append(int(deal_card()))
        last_dealer_card = int(dealer_hand[len(dealer_hand) - 1])
        if sum(dealer_hand) > 21 and last_dealer_card == 11:
            dealer_hand[len(dealer_hand) - 1] = 1

    print(compare_hands(player_hand, dealer_hand))
    start_game()


start_game()
