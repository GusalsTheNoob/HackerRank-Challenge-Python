# "Mutation" Challenge

def mutate_string(string, position, character):
    strlist = list(string)
    strlist[position] = character
    return "".join(strlist)

"""
<느낀 점>

1. 원래는 아래 코드를 작성하려고 했는데,
return string[:position-1] + character + string[position:]
IndexError가 걱정돼서 (맨 처음이나 맨 뒤) 다른 코드를 이용함.
그런데 막상 돌려보니 문제가 없네?
[:0], [len(list):]는 ""로 인식되는 듯하다!

"""