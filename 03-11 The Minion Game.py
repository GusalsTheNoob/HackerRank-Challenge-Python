# "The Minion Game" Challenge

def minion_game(string):

    #2. iterate
    vowels = ['A', 'E', 'I', 'O', 'U'] #1 'AEIOU'
    stuart = 0
    kevin = 0
    length = len(string)
    for i, char in enumerate(string):
        score = length - i
        if char in vowels:
            kevin += score
        else:
            stuart += score
    
    #3. decide who has won
    if kevin > stuart: print(f'Kevin {kevin}')
    elif kevin < stuart: print(f'Stuart {stuart}')
    else: print("Draw")

"""
<느낀 점>

1. string도 iterable하기 때문에 in이 이용 가능하다.

"""