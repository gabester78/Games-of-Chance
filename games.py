import random

money = 100

# Write your game of chance functions here


def coin_flip(guess, bet):
    if bet <= 0:
        print('Your coin flip bet must exceed $0.')
        return 0
    print("Your coin flip bet is $" + str(bet) +
          " and your guess is " + guess + '.')
    flip = random.randint(1, 2)
    if flip == 1:
        result = 'Heads'
        print('And the winner is ' + result + '!')
    elif flip == 2:
        result = 'Tails'
        print('And the winner is ' + result + '!')

    if result == guess:
        total = bet
        print('You won $' + str(total) + '!')
        return total
    elif result != guess:
        total = bet * -1
        print('You lost $' + str(abs(total)) + '!')
        return total


# Call your game of chance functions here
money += coin_flip('Heads', 1)
money += coin_flip('Tails', 5)
money += coin_flip('Tails', 10)
print('Your current total is $' + str(money) + '!')
