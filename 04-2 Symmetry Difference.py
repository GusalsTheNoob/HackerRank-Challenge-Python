# "Symmetry Difference" Challenge

#1. Get input
_ , setA = (input(), set(map(int, input().split())))
_ , setB = (input(), set(map(int, input().split())))

#2. Get difference
A_has = setA.difference(setB) 
B_has = setB.difference(setA) 

#3. Merge it!
answer = A_has.union(B_has)

#4. Output
answer = sorted(list(answer))
[print(num) for num in answer]

"""
<느낀 점>

1. Input 받을 때 Type Check 제발...ㅠ

2. Modifying sets: .add(), .update()
3. removing items: .discard(), .remove() [Remove는 KeyError 기능이 있음]
4. set operations: .union(), .intersection(), .difference()

"""