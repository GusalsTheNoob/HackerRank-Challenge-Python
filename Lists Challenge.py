#"Lists" Challenge

#0. Get N input
N = int(input())
target = []

#1. method dict
method_dict = {
    'insert': lambda s, i, e: s.insert(i, e),
    'print': lambda s: print(s),
    'remove': lambda s, e: s.remove(e),
    'append': lambda s, e: s.append(e),
    'sort': lambda s: s.sort(),
    'pop': lambda s: s.pop(),
    'reverse': lambda s: s.reverse()
}

#2.get the rest and execute
for _ in range(N):
    command = input().split()
    method = command.pop(0)
    parameters = [target] + list(map(int, command))
    method_dict[method](*parameters)

"""
<느낀 점>

1. python에는 switch문이 없다. if-elif-else 구조를 사용할 수는 있다.
2. 만약 switch와 비슷한 방식의 코딩을 원한다면, key-value 구조의 dict를 사용해보는 것을 시도할 수 있다.
생각해보지도 못한 알고리즘인데, 참고한 링크: https://thrillfighter.tistory.com/602

3. list.pop()의 묘미는 해당 value를 제거해준다는 것. 편리하게 원하는 부분만 남길 수 있다.

4. 전에 배웟지만, *[...]는 여러모로 편리함을 가져다주는 듯.

5. lambda function을 이용하면 다변수로 적용해야 하는 간단한 function 객체를 쉽게 만들 수 있어서 좋다.
6. 다변수 표현법도 찾아봄. 아직 많이 서툴다.

7. 아직 str method에 대한 숙련도가 낮다. 헷갈리는 게 많음.
8. list.insert(pos, ele) 순서
9. del list[i], list.remove(e) 차이점 확실히 구분해두기

10. list의 범주를 벗어나지만 훌륭한 해결법을 하나 찾았는데,
getattr(s, method)(*parameters)를 활용하면 dict가 필요 없다.
getattr(object, method/variable)은 어떤 object의 method/varaible str 이름을 주면 그것을 실제로 호출해준다.
일종의 str -> method/variable type converter 같은 느낌?
신선한 충격.

"""