# "Alphabet Rangoli" Challenge (Not Completed)

# 1. get input
N = int(input())
width = 4 * N - 3
alphalist = [chr(i) for i in range(97, 97+N)]
charnum = 0

# 2. print out
for i in range(1, 2*N):
    if i <= N: charnum += 1
    else: charnum -= 1
    thislist = list(reversed(alphalist[N-charnum:])) + alphalist[N-1+charnum:]
    content = '-'.join(thislist)
    print(content.center(width, '-'))