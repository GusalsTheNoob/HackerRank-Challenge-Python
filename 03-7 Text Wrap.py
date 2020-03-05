# "Text Wrap" Challenge

# Without text wrap

text = input()
num = int(input())
length = len(text)
i = 0

while (i < length):
    if length > num:
        print(text[i: i+num])
        i += num
    else:
        print(text[i:])
        i = length
        
"""
<느낀 점>

1. 역시 다른 사람들도 원했을만한 기능들은 이미 개발이 되어 있다. 구글링 필수.

2. textwrap이라는 표준 python library가 있다. 표준 library 공부는 어디까지 해야하는 걸까?

3. 깔끔한 코드가 하나 있다.
"\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])

"""