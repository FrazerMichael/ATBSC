import random

print ('ROCK, PAPER, SCISSORS')
print ('Would you like to play?')

gameOn = input()
wins = 0
losses = 0
ties = 0

while gameOn == 'yes':
    #
    print(f'{wins} Wins, {losses} Losses, {ties} Ties')

    throwOptions = ['Rock', 'Paper', 'Scissors']

    #computer's throw
    cpuThrow = throwOptions[random.randint(0, 2)]

    #user's throw
    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
    throw = input()

    def realThrow(i):
        switcher={
                'r' : throwOptions[0],
                'p' : throwOptions[1],
                's' : throwOptions[2],
                'q' : 'off'
                }
        return switcher.get(i,'Invalid day of the week')

    #check for quit
    if realThrow(throw) == 'off':
        break

    #print throws
    print(f'{realThrow(throw)} versus...')
    print(cpuThrow)

    #determine winner
        #determine winner
    if realThrow(throw) == cpuThrow:
        print ('It is a tie!')
        ties += 1
    elif realThrow(throw) == 'Rock' and cpuThrow == 'Scissors':
        print ('You Win!')
        wins += 1
    elif realThrow(throw) == 'Paper' and cpuThrow == 'Rock':
        print ('You Win!')
        wins += 1
    elif realThrow(throw) == 'Scissors' and cpuThrow == 'Paper':
        print ('You Win!')
        wins += 1
    elif realThrow(throw) == 'Rock' and cpuThrow == 'Paper':
        print ('You Lose!')
        losses += 1
    elif realThrow(throw) == 'Scissors' and cpuThrow == 'Rock':
        print ('You Lose!')
        losses += 1
    elif realThrow(throw) == 'Paper' and cpuThrow == 'Scissors':
        print ('You Lose!')
        losses += 1
