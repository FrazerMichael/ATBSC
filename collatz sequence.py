def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number / 2
            print(int(number))
        else:
                number = 3 * number + 1
                print(int(number))

print('Enter a interger that you would like to use'
    + 'for the Collatz Sequence')

while True:
    try:
        userNumber = int(input())
        break

    except ValueError:
        print('Must enter an interger')

collatz(userNumber)