# "String Validators" Challenge

#1. get an input
s = input()
s_char = [char for char in s]

#2. validation
print(any(list(map(lambda x: x.isalnum(), s_char))))
print(any(list(map(lambda x: x.isalpha(), s_char))))
print(any(list(map(lambda x: x.isdigit(), s_char))))
print(any(list(map(lambda x: x.islower(), s_char))))
print(any(list(map(lambda x: x.isupper(), s_char))))

#print(any([x.isalnum()for x in s]))

"""
<느낀 점>

1. map과 lambda에 익숙해져 가는 것은 좋지만, 훨씬 더 간단한 방법이 있다는 게 함정!

"""

