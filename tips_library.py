import random
##make tips: Divisers of number [number], </>[number],
##Devisers of
#><
#multiplier
def greater_smaller(answer,number):
    if number > answer:
        print(f'{answer} is bigger than the answer')
        return number,'>'
    else:
        print(f'{answer} is smaller than the answer')
        return number,'<'
def devisers_of(answer,*_):
    numbers = []
    for f in range(2,answer):
        if answer % f:
            pass
        else:
            numbers.append(f)
    return numbers
def multiplier(answer,*_):
    numbers = []
    for f in range(2,answer):
        multiplied_answer = f'Answer multiplied by something = {answer * f}'
        numbers.append(multiplied_answer)
    return numbers