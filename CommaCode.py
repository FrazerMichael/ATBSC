spam = ['apples', 'juice', 'pumpkin', 'banana']

for i in range(len(spam)):
    if(i <= (len(spam) - 3)):
        print(spam[i] + ', ', end='')

    elif(i == (len(spam) - 2)):
        print(spam[i] + ', and ', end='')

    else:
        print(spam[i] + '.')


