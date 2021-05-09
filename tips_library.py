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
            numbers.append(f'One of the devisors of the answer is {f}')
    if numbers == []:
        numbers.append('The answer is simple ;)')
    return numbers
def multiplier(answer,*_):
    numbers = []
    for f in range(2,answer):
        multiplied_answer = f'Answer multiplied by something = {answer * f}'
        numbers.append(multiplied_answer)
    return numbers
def list_flatten(list_):
    ss = []
    for f in list_:
        for d in f:
            ss.append(d)
    return ss