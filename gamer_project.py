import random
import tips_library

DEBUG = 1
#tips_library.greater_smaller(4,8)
#print(tips_library.greater_smaller(4,8))
###Random number guesser. Game chooses a random number and player has to guess it.
###Game explains the rules.
###Game should tell the range of numbers, it chooses a random number in that range.
###User enters the number.
###Game analyses it and decides is it correct. Then tells the user the answer.
def level(difficulty,random_number):
    hints = [tips_library.devisers_of,tips_library.greater_smaller,tips_library.multiplier]
    done_hints = [tips_library.devisers_of(random_number), tips_library.multiplier(random_number)]
    print(done_hints)
    #print(done_hints)
    while True:
        if DEBUG:
            print(random_number)
        print(f'level difficulty is {difficulty}')
        inputted_number = int(input('Enter number '))
        if inputted_number == random_number:
            win = 1
            print('You win!')
            break
        else:
            win = 0
            print('You lose!')
            fg = random.choice(random.choice(done_hints))
            #all_hints = []
            #all_hints.append(fg)
            #if fg == all_hints[0]:
            #    fg = random.choice(random.choice(done_hints))
            print(f'tip: {fg}')
    #        done_hints.pop(fg)
    #        print(f'fg() contains {fg(random_number,inputted_number)}')
    #        print(f'Hint: Devisors of the answer are {tips_library.devisers_of(random_number)}')
    return win
def main():
    difficulty = 10
    score = 0
    random_number = random.randint(0,difficulty)
    while True:
        result = level(difficulty,random_number)
        if DEBUG:
            print(f'Result is {result}')
        if result == 1:
            difficulty = difficulty * 2
            random_number = random.randint(0,difficulty)
            score = score+1
            print(f'Score is {score}')
        else:
            score = score-1
            print(f'Score is {score}')
main()