# "Set .add()" Challenge

#1. input
N = int(input())
country_set = set([])
[country_set.add(input()) for _ in range(N)] #1

#2.output
print(len(country_set))

"""
<느낀 점>

1. 조금 괴상한 방법이긴 한데, 저런 표현도 가능하다. 근데 앞으로는 안해야지. 상식적이지 않다.

"""