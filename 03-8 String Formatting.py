# "String Formatting" Challenge

def print_formatted(number):
    width = len(bin(number)) - 2
    for i in range(1, number+1):
        print('{1:>{0}d} {1:>{0}o} {1:>{0}X} {1:>{0}b}'.format(width, i))

"""
<느낀 점>

1. formatting은 적당히 알고 넘기면 되겠지 했는데 딱 걸린 느낌?
2. 우선 중요한 발견은 formatting param도 {} 안에 집어넣을 수 있는 엄청난 기능이 있다는 것
3. 또, 이런 param에 대해서는 관행상 named param 형식을 취해주는 듯

4. n진수를 쓸모있게 다뤄본 적이 없어서 엄청 더뎠음.
5. 우선 이름 정도는 알아두기, b, o, d, h.
6. bin() hex() 함수는 문자열을 돌려준다. 거기에다가 앞에 진수 표시를 위한 요상한 표기를 붙이는 것 주의.
이것 때문에 알고리즘에 논리적 오류가 생김.
7. int(s, i)에 대해 여지껏 잘못 알고 있었음. 이때 s는 n진수로 변환된 문자열이지 10진수가 아님.
int()는 진수 변환 기능이 없음. 있었으면 좋았을 텐데.

"""