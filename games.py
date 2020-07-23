import random

money = 100

# Write your game of chance functions here


def coin_flip(guess, bet):
    print('')

    # checks to make sure player doesn't have any typos in their guess
    # if guess != 'Heads' or 'Tails':
    #     print('You must choose Heads or Tails to play coin flip!')
    #     return 0

    # checks to make sure player has money to bet
    if money <= 0:
        print('You do not have enough money to play. Game over!')

        return 0

    # checks to make sure player is betting at least $1
    if bet <= 0:
        print('Your coin flip bet must exceed $0.')

        return 0

    print("Your coin flip bet is $" + str(bet) +
          " and your guess is " + guess + '.')

    # returns a random 1 or 2
    flip = random.randint(1, 2)

    # prints out the result of the random number found
    if flip == 1:
        result = 'Heads'
        print('The result is ' + result + '!')
    elif flip == 2:
        result = 'Tails'
        print('The result is ' + result + '!')

    # prints out whether the player won or lost their bet
    if result == guess:
        print('You won $' + str(bet) + '!')
        return bet
    elif result != guess:
        total = bet * -1
        print('You lost $' + str(abs(total)) + '!')
        return total


# Call your game of chance functions here
print('')
print('Your current total in the bank is $' + str(money) + '!')
money += coin_flip('Heads', 20)
money += coin_flip('Heads', 30)
money += coin_flip('Heads', 50)
print('')
print('Your current total in the bank is $' + str(money) + '!')
print('')
