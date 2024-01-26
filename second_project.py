keyword = ['c', 'o', 'm', 'p', 'u', 't', 'e', 'r']
current = ['_', '_', '_', '_', '_', '_', '_', '_']

print('\nThis is the simple world game.')

while True:
    answer = input('\nEnter the alphabet you think: \n(or you can enter the word you think correct)\n')
    if answer == 'c' :
        del current[0]
        current.insert(0, 'c')
    elif answer == 'o' :
        del current[1]
        current.insert(1, 'o')
    elif answer == 'm':
        del current[2]
        current.insert(2, 'm')
    elif answer == 'p' :
        del current[3]
        current.insert(3, 'p')
    elif answer == 'u' :
        del current[4]
        current.insert(4, 'u')
    elif answer == 't' :
        del current[5]
        current.insert(5, 't')
    elif answer == 'e' :
        del current[6]
        current.insert(6, 'e')
    elif answer == 'r' :
        del current[7]
        current.insert(7, 'r')

    elif answer == 'computer':
        print('congratulations! You guessed correctly.')
        break

    else :
        print('\n' + answer, 'is not (in) the word.')


    for alphabet in current:
        print(alphabet, end=' ')




