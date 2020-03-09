# "Merge the Tools" Challenge

def merge_the_tools(string, k):
    
    #1. split
    length = len(string)
    total_iter = int(length / k)

    #2. iterate
    for i in range(total_iter):
        substring = string[i*k:(i+1)*k]
        result = ""
        for char in substring:
            if not (char in result): result += char
        print(result)

"""
<느낀 점>

1. dict.setdefault(key, value)를 이용한 접근, OrderedDict를 이용한 접근이 있다. 신기하네.
S, N = input(), int(input()) 
for part in zip(*[iter(S)] * N):
    d = dict()
    print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))

2. 위 코드에서는 iter를 사용하는데, iter는 어디서나 global처럼 사용되는 신기한 성질이 있다.

"""