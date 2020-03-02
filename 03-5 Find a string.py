# "Find a string" Challenge

def count_substring(string, sub_string):
    count = 0
    index = string.find(sub_string)
    while index != -1:
        count += 1
        index = string.find(sub_string, index+1)
    return count

"""
<느낀 점>

1. str.find()의 색다른 사용법?
2. str.count()를 사용해보려고 했지만, 오류가 발생한다.
ABCDCDC (CDC) => 2가 나와야 하는데 1밖에 안 나옴

3. One-liner 중에 List Comprehension을 이용한 경우가 있음
sum([1 for i in range(len(string)-len(substring)+1) if string[i:i+len(substring)] == substring])
잘못 알고 있던 부분이 있다면, else에서 굳이 0을 지정해주지 않아도 된다는 점.

"""