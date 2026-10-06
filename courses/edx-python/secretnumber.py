low = 0
high = 100
guesses = 0
acertou = False

print('Please think of a number between 0 and 100!')

print("Enter 'h' to indicate the guess is too high | Enter 'l' to indicate the guess is too low | Enter 'c' to indicate I guessed correctly.\n")

def mostrar_chute(chute):
    print('Is your secret number '+ str(chute) + '?')

while not acertou:
    mid = (low + high) // 2
    mostrar_chute(mid)
    dica = input('Enter your answer: ')
    guesses += 1

    if dica == 'h':
        high = mid - 1
    elif dica == 'l':
        low = mid + 1
    elif dica == 'c':
        acertou = True
    else:
        print("Invalid option! Use h, l, or c.")

print('I guessed the number ' + str(mid) + ' in ' + str(guesses) + ' attempts!')
