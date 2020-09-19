# blackjack
import random
import sys


def deckQty():
    while True:
        try:
            numDecks = int(input("How many decks to play with?: "))
        except:
            print('You did not enter a number')
        if numDecks > 0:
            break
        else:
            sys.exit()
    return numDecks


def buildDeck(numDecks):  # construct the deck based on how many player wants to play with
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 'A'] * 4 * numDecks
    deck = [str(i) for i in deck]
    return deck


def dealComputerHand(deck):  # deal computer's starting hand of 2 cards
    deckSize = int(len(deck))
    computerHand = []
    for i in range(1, 3):
        card = random.randint(0, deckSize - 1)
        computerHand.append(deck[card])
        del deck[card]
        deckSize = len(deck)
    return computerHand


def dealPlayerHand(deck):  # deal player's starting hand of 2 cards
    deckSize = int(len(deck))
    playerHand = []
    for i in range(1, 3):
        card = random.randint(0, deckSize - 1)
        playerHand.append(deck[card])
        del deck[card]
        deckSize = len(deck)
    return playerHand


def playerAction(playerHand, chipCount, bet):
    choice = ''
    if len(playerHand) == 1:
        while True:
            choice = input('\n' + 'What would you like to do?' + '\n' +
                           '(H = hit, S = stand): ').lower()
            if choice in ['h', 's']:
                break
        return choice
    elif playerHand[0] == playerHand[1]:
        while True:
            choice = input('\n' + 'What would you like to do?' + '\n' +
                           '(H = hit, S = stand, P = Split, D = Double down): ').lower()
            if choice in ['h', 's', 'p', 'd']:
                if choice == 'd' and (bet + bet > chipCount):  # can't double if you don't have the dough
                    print('Insufficient chips to Double Down!')
                    continue
                elif choice == 'p' and (bet + bet > chipCount):  # can't double if you don't have the dough
                    print('Insufficient chips to Split!')
                    continue
                else:
                    break
        return choice
    elif playerHand == ['1','A'] and split == False: # special case for [A,A] since checkTotal has some weird ace logic in there
        while True:
            choice = input('\n' + 'What would you like to do?' + '\n' +
                           '(H = hit, S = stand, P = Split, D = Double down): ').lower()
            if choice in ['h', 's', 'p', 'd']:
                if choice == 'd' and (bet + bet > chipCount):  # can't double if you don't have the dough
                    print('Insufficient chips to Double Down!')
                    continue
                elif choice == 'p' and (bet + bet > chipCount):  # can't double if you don't have the dough
                    print('Insufficient chips to Split!')
                    continue
                else:
                    break
        return choice
    elif len(playerHand) == 2 and split == False:  # can only double down on 1st 2 cards
        while True:
            choice = input('\n' + 'What would you like to do?' + '\n' +
                           '(H = hit, S = stand, D = Double down): ').lower()
            if choice in ['h', 's', 'd']:
                if choice == 'd' and (bet + bet > chipCount):  # can't double if you don't have the dough
                    print('Insufficient chips to Double Down!')
                    continue
                else:
                    break
        return choice
    else:
        while True:
            choice = input('\n' + 'What would you like to do?' + '\n' +
                           '(H = hit, S = stand): ').lower()
            if choice in ['h', 's']:
                break
        return choice


def checkTotal(hand):
    HandTotal = 0
    while True:
        for i in hand:
            if (i != 'A'):  # if not an ace, add the value of the card
                if (HandTotal + int(i) > 21) and ('A' in hand):
                    # if value of card puts total above 21, and there is an ace in hand,
                    # then add card value, subtract 10, and change ace to value 1.
                    HandTotal += int(i) - 10
                    aceLocation = hand.index('A')
                    hand.insert(aceLocation, '1')
                    hand.remove('A')
                    continue
                else:  # add value of the card
                    HandTotal += int(i)
            else:  # if card is an ace...
                if HandTotal + 11 > 21:
                    HandTotal += 1
                    aceLocation = hand.index('A')
                    hand.insert(aceLocation, '1')
                    hand.remove('A')
                else:
                    HandTotal += 11
        if ('A' in hand) and (HandTotal > 21):
            continue
        else:
            break
    return HandTotal


def Hit(deck, playerHand):
    deckSize = int(len(deck))
    card = random.randint(1, deckSize - 1)
    playerHand.append(deck[card])
    del deck[card]
    deckSize = len(deck)
    return playerHand

def Bust(hand):
    value = 0
    for i in hand:
        if (i == 'A'):
            value = value + 1
        else:
            value = value + int(i)
    if value <= 21:
        return False
    else:
        return True

def showHand(hand):
    for i in hand:
        print(i)


def isBlackJack(hand):
    if ('A' in hand) and ('10' in hand):
        return True
    else:
        return False

def placeBet():
    if chipCount < 10:
        print("You don't have enough chips to play! GameOver!")
        sys.exit()
    else:
        while True:
            try:
                bet = int(input('Place your bet: '))
                if bet > chipCount:
                    print("You don't have that many chips!")
                elif bet < 10:
                    print("You can't bet less than 10!")
                else:
                    break
            except (KeyboardInterrupt):
                sys.exit()
            except:
                print('Invalid Bet')
        return bet

gameIsPlaying = True
split = False
while gameIsPlaying == True:
    print(str('').center(70, '*') + "\n" +
          str("   Welcome to BlackJack!   ").center(70, '*') + "\n" +
          str().center(70, '*'))
    numDecks = deckQty()
    deck = buildDeck(numDecks)
    sessionIsActive = True
    chipCount = 100
    while sessionIsActive:
        if len(deck) < 20:  # if deck is running out of cards, shuffle with original amount of decks selected
            print(str('').center(70, '*') + '\n' +
                  '   Deck is low on cards... shuffling Deck.   '.center(70, '*') + '\n' +
                  str('').center(70, '*'))
            deck = buildDeck(numDecks)
            continue
        # add decksize check and 'shuffle' if too low
        print('\n' + '     Your available chip count is: '.rjust(50, '*') +
              str(chipCount) + '     '.ljust(30, '*') + '\n')
        bet = placeBet()
        playerHand = dealPlayerHand(deck)
        computerHand = dealComputerHand(deck)
        print("\n" + "Dealer's Up Card is: " + str(computerHand[0]) + "\n")
        print("Your Hand: ")
        showHand(playerHand)

        # check hands for blackjack
        if isBlackJack(playerHand) and isBlackJack(computerHand) == False:
            print('   You have BlackJack!   '.center(60, '&'))
            chipCount += int(bet * 1.5)  # blackjack pays player 1.5
            continue
        if isBlackJack(computerHand) and isBlackJack(playerHand) == False:
            print('Dealer hand: ')
            showHand(computerHand)
            print('   Dealer has BlackJack! You lose!   '.center(60, '&'))
            chipCount -= int(bet)
            continue
        if isBlackJack(computerHand) and isBlackJack(playerHand):
            print('Dealer hand: ')
            showHand(computerHand)
            print('   You and Dealer have BlackJack! Hand is a Push!   '.center(60, '&'))
            continue

        # playerAction
        pStay = False
        while (Bust(playerHand) == False) and (pStay == False):
            playerTotal = checkTotal(playerHand)
            print('You have ' + str(playerTotal))
            choice = playerAction(playerHand, chipCount, bet)  # returns choice
            if choice == 'h':
                Hit(deck, playerHand)
                showHand(playerHand)
            elif choice == 's':
                showHand(playerHand)
                pStay = True
            elif choice == 'd':
                bet += bet
                Hit(deck, playerHand)
                showHand(playerHand)
                pStay = True
            elif choice == 'p' and split == True:
                print("You can only split once, sorry!")
                continue
            elif choice == 'p' and split == False:
                split = True
                if playerHand[0] == '1':
                    print('You have split your Aces.')
                    print("Playing on first Ace.")
                else:
                    print('You have split your ' + str(playerHand[0]) + "'s.")
                    print("Playing on first " + str(playerHand[0]) + ".")
                playerHand_2 = []
                playerHand_2.append(playerHand[1])
                playerHand.remove(playerHand[1])
            else:
                break

        # final player hand value after action
        playerTotal = checkTotal(playerHand)
        print('You have ' + str(playerTotal) + '\n')
        if playerTotal > 21:
            print('You Bust!' + '\n')
            chipCount -= int(bet)
            print('Chip count is : ' + str(chipCount))
            if split == False:
                continue

        #if split, play 2nd hand
        if split == True:
            print('\n')
            if playerHand[0] == '1':
                print("Playing on second Ace.")
            else:
                print("Playing on second " + str(playerHand_2[0]) + ".")
            pStay = False
            while (Bust(playerHand_2) == False) and (pStay == False):
                playerTotal_2 = checkTotal(playerHand_2)
                print('You have ' + str(playerTotal_2))
                choice = playerAction(playerHand_2, chipCount, bet)  # returns choice
                if choice == 'h':
                    Hit(deck, playerHand_2)
                    showHand(playerHand_2)
                elif choice == 's':
                    showHand(playerHand_2)
                    pStay = True
                elif choice == 'd':
                    bet += bet
                    Hit(deck, playerHand_2)
                    showHand(playerHand_2)
                    pStay = True
                elif choice == 'p' and split == True:
                    print("You can only split once, sorry!")
                    continue
                else:
                    break

        # final player (2nd split) hand value after action
        playerTotal = checkTotal(playerHand)
        if split == True:
            playerTotal_2 = checkTotal(playerHand_2)
            print('Second Split Hand: You have ' + str(playerTotal_2) + '\n')
            if playerTotal_2 > 21:
                print('Second Split Hand: You Bust!' + '\n')
                chipCount -= int(bet)
                split = False
                continue

        # dealerAction
        cStay = False
        while (Bust(computerHand) == False) and (cStay == False):
            print('Dealer hand: ')
            showHand(computerHand)
            computerTotal = checkTotal(computerHand)
            print('Dealer has ' + str(computerTotal) + '\n')
            if computerTotal < 17:
                print('Dealer hits.' + '\n')
                Hit(deck, computerHand)
            elif (computerTotal >= 17) and (computerTotal <= 21):
                print('Dealer stays with ' + str(computerTotal))
                cStay = True
            else:
                break

        computerTotal = checkTotal(computerHand)
        if computerTotal > 21:
            print('Dealer hand: ')
            showHand(computerHand)
            print('Dealer busts at ' + str(computerTotal) + '! You Win!')
            chipCount += int(bet)
            if split == True and playerTotal_2 <= 21:
                chipCount += int(bet)
                split = False
            continue

        # check the winner
        if split == True and playerTotal <= 21:
            if playerTotal > computerTotal:
                print('First Split Hand: You win!' + '\n')
                chipCount += int(bet)
            elif playerTotal < computerTotal:
                print('First Split Hand: You lose!' + '\n')
                chipCount -= int(bet)
            else:
                print("First Split Hand: Hand is a push." + '\n')

            if playerTotal_2 > computerTotal and playerTotal_2 <= 21:
                print('Second Split Hand: You win!' + '\n')
                chipCount += int(bet)
            elif playerTotal_2 < computerTotal:
                print('Second Split Hand: You lose!' + '\n')
                chipCount -= int(bet)
            else:
                print("Second Split Hand: Hand is a push." + '\n')
            split = False

        else:
            if playerTotal > computerTotal:
                print('You win!' + '\n')
                chipCount += int(bet)
            elif playerTotal < computerTotal:
                print('You lose!' + '\n')
                chipCount -= int(bet)
            else:
                print("Hand is a push." + '\n')