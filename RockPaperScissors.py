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

