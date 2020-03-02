#" sWAP cASE" challenge

def swap_case(s):
    ret = ""
    for char in s:
        code = ord(char)
        if (65 <= code <= 90): #대문자면
            ret += chr(code + 32)
        elif (97 <= code <= 122): #소문자면
            ret += chr(code - 32)
        else:
            ret += char
    return ret

"""
<느낀 점>

1. 일단 built-in function을 찾아보자. 구글링이 엄청난 시간 절약을!
python.swapcase()

2. 그래도 중요한 method와 함수를 많이 복습해봤다.
3. 우선 .isupper(), .islower() ASKII 코드 검색했던 게 뻘쭘해지네;;
4. ord()와 chr()의 방향. 직관적으로 함수 이름이 결과물이라고 생각.

5. 알고리즘 짤 때, else 부분을 빼먹었다. 이런 실수는 줄여야 함.

6. One-liner 장인들의 코드.
print(*map(lambda ch : ch.lower() if ch.isupper() else ch.upper(), input()), sep="")
print(sep="")는 계속 보면서 익숙해져야겠다.
ternary operator, lambda func, list comprehension이 자주 쓰이는 듯.

"""