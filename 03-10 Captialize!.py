# "Capitalize!" Challenge

def solve(s):
    return ' '.join(map(lambda x: x.capitalize(), s.split(' ')))

"""
<느낀 점>

1. join - map 방법이 있을 때는 replace도 유연하게 생각할 수 있기를.
str.replace(Astr, Bstr)하면 더 간단하게 표현할 수 있음

2. str.title과 str.capitalize의 차이는 전자는 처음 등장하는 알파벳을 대문자로 바꾼다는 사실!!

3. lambda 함수는 js에서와 달리 별다른 변수를 추가로 사용할 수 없더라...

"""