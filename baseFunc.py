
# 파이썬 내장함수


# abs(x)
#----------------------------------------------------
# 그 숫자의 절대값을 돌려준다

# print(abs(3))       # 3
# print(abs(-3))      # 3
# print(abs(-1.2))    # 1.2



# all(x)
#----------------------------------------------------
# 반복가능한(iteralbe) 자료형 x를 입력 인수로 받으며,
# 이 x의 요소가 모두 참이면 True,
# 거짓이 하나라도 있으면 False를 돌려준다.
# 반복가능한 자료형이란 for문으로 그 값을 출력할 수 있는 것을 의미한다.
# > 리스트, 튜플, 문자열, 딕셔너리, 집합 등이 있다.

# print(all([1,2,3]))     # True
# print(all([1,2,3,0]))   # False
# print(all([]))          # True



# any(x)
#----------------------------------------------------
# 반복가능한 자료형 x를 입력 인수로 받으며
# x의 요소 중 하나라도 참이 있으면 True를 돌려주고,
# x가 모두 거짓일때만 False를 돌려준다. all(x)의 반대

# print(any([1,2,3,0]))       # True
# print(any([0, ""]))         # False
# print(any([]))              # False




# chr
#----------------------------------------------------
# 아스키 코드값을 입력받아 그 코드에 해당하는 문자를 출력하는 합수이다.

# print(chr(97))      # a
# print(chr(48))      # 0



# dir
#----------------------------------------------------
# 객체가 자체적으로 가지고 있는 변수나 함수를 보여준다.

# print(dir([1,2,3]))
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# print(dir({'1':'a'}))
# ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', 
# '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']




# divmod(a, b)
#----------------------------------------------------
# 2개의 숫자를 입력으로 받아 a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려주는 함수.

# print(divmod(7, 3))     # (2, 1)




# enumerate
#----------------------------------------------------
# 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아
# 인덱스 값을 포함하는 enumerate 객체를 돌려준다

# for i, name in enumerate(['body', 'foo', 'bar']):
#     print(i, name)

# # >>>
# # 0 body
# # 1 foo
# # 2 bar



# eval(expression)
#----------------------------------------------------
# 실행가능한 문자열(1+2, 'hi'+'a'같은것)을 입력으로 받아
# 문자열을 실행한 결괏값을 돌려주는 함수이다.

# print(eval('1+2'))              # 3
# print(eval("'hi' + 'a'"))       # hia
# print(eval('divmod(4,3)'))      # (1, 1)




# filter
#----------------------------------------------------
# 첫번째 인수로 함수 이름을, 두번째 인수로 그 함수에 차례로 들어갈
# 반복 가능한 자료형을 받는다.
# 그리고 두번째 인수인 반복 가능한 자료형 요소가 첫번째 인수인 함수에 입력되었을 떄
# 반환 값이 참인것만 묶어서(걸러내서) 돌려준다.

# ex 1
# def positive(l):
#     result = []
#     for i in l:
#         if i > 0:
#             result.append(i)
#     return result

# print(positive([1,-3,2,0,-5,6]))        # [1,2,6]

# ex2
# def positive(x):
#     return x > 0

# print(list(filter(positive, [1,-3,2,0,-5,6])))      # [1,2,6]

# ex3
# def positive(x):
#     return x < 0

# print(list(filter(positive, [1,-3,2,0,-5,6])))      # [-3,-5]

# ex4
# print(list(filter(lambda x:x>0, [1,-3,2,0,-5,6])))    # [1,2,6]



# hex
#----------------------------------------------------
# 정수값을 입력받아 16진수로 변환하여 돌려주는 함수

# print(hex(234))     # 0xea
# print(hex(3))       # 0x3



# id
#----------------------------------------------------
# 객체를 입력받아 객체의 고유 주소값(레퍼런스)을 돌려주는 함수

# a = 3
# print(id(3))    # 3015116941680
# print(id(a))    # 3015116941680
# b = a
# print(id(b))    # 3015116941680
# print(id(4))    # 3015116941712



# input([prompt])
#----------------------------------------------------
# 사용자 입력을 받는 함수이다.

# a = input()
# print(a)
# b = input("Enter:")
# print(b)



# int
#----------------------------------------------------
# 문자열 형태의 숫자나 소수점이 있는 숫자등을 정수 형태로 돌려주는 함수

# print(int('3'))     # 3
# print(int(3.4))     # 3



# isinstance(object, class)
#----------------------------------------------------
# 첫번째 인수로 인스턴스, 두번째 인수로 클래스 이름을 받는다.
# 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여
# 참이면 True, 거짓이면 False를 돌려준다.

# class Person:
#     pass

# a = Person()
# b = 3

# print(isinstance(a, Person))    # True
# print(isinstance(b, Person))    # False



# list(s)
#----------------------------------------------------
# 반복가능한 자료형 s를 입력받아 리스트로 만들어 돌려주는 함수

# print(list("python"))       # ['p', 'y', 't', 'h', 'o', 'n']
# print(list((1,2,3)))        # [1, 2, 3]



# map(f, iterable)
#----------------------------------------------------
# 함수(f)와 반복가능(iterable)자료형을 입력으로 받는다
# 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려준다

# ex1
# def two_times(numberList):
#     result = []
#     for number in numberList:
#         result.append(number*2)
#     return result

# result = two_times([1,2,3,4])
# print(result)   # [2,4,6,8]


# ex2
# def two_times(x):
#     return x*2

# print(list(map(two_times, [1,2,3,4])))      # [2,4,6,8]


# ex3
# print(list(map(lambda x:x*2, [1,2,3,4])))       # [2,4,6,8]



# max(iterable)
#----------------------------------------------------
# 반복 가능한 자료형을 입력받아 그 최대값을 돌려주는 함수

# print(max([1,2,3]))             # 3
# print(max((7,8,19,3,1,-4)))     # 19


# min(iterable)
#----------------------------------------------------
# max 의 반대

# print(min([1,2,3]))             # 1
# print(min((7,8,19,3,1,-4)))     # -4



# oct
#----------------------------------------------------
# 정수 형태의 숫자를 8진수 문자열로 바꾸어 돌려주는 함수

# print(oct(34))          # 0o42
# print(oct(12345))       # 0o30071



# open(filename, [mode])
#----------------------------------------------------
# mode = 'w' : 쓰기모드로 파일열기
# mode = 'r' : 읽기모드로 파일열기
# mode = 'a' : 추가모드로 파일열기
# mode = 'b' : 바이너리 모드로 파일열기
# b 는 w,r,a 와 함께 사용한다.

# fread = open("read_mode.txt", 'r')
# fread2 = open("read_mode.txt")
# 모드부분을 생략하면 기본값으로 읽기 모드 r을 갖게 된다.




# ord(c)
#----------------------------------------------------
# 문자의 아스키 코드값을 돌려주는 함수
# chr 의 반대

# print(ord('a'))     # 97
# print(ord('0'))     # 48




# pow(x,y)
#----------------------------------------------------
# x의 y제곱한 결과값을 돌려주는 함수

# print(pow(2,4))     # 16
# print(pow(3,3))     # 27



# range
#----------------------------------------------------
# range([start,] stop [,step)는 for 문과 함께 자주 사용하는 함수
# 입력받은 숫자에 해당하는 범위값을 반복가능한 객체로 만들어 돌려준다.

# print(list(range(5)))       # [0,1,2,3,4], 시작 숫자를 지정하지 않으면 0부터 시작

# print(list(range(5, 10)))   # [5,6,7,8,9], 끝 숫자는 해당범위에 포함되지 않는다.

# print(list(range(1,10,2)))  # [1,3,5,7,9], 세번째 인수는 숫자 사이의 거리를 말한다.



# round(number[, ndigits])
#----------------------------------------------------
# 숫자를 입력받아 반올림해주는 함수

# print(round(4.6))           # 5
# print(round(4.2))           # 4
# print(round(5.678, 2))      # 5.68, 소수 2자리까지만 반올림하여 표시



# sorted(iterable)
#----------------------------------------------------
# 입력값을 정렬한 후 그 결과를 리스트로 돌려주는 함수

# print(sorted([3,1,2]))          # [1,2,3]
# print(sorted(['a','c','b']))    # ['a','b','c']
# print(sorted("zero"))           # ['e','o','r','z']
# print(sorted((3,2,1)))          # [1,2,3]



# str(object)
#----------------------------------------------------
# 문자열 형태로 객체를 변환하여 돌려주는 함수

# print(str(3))               # 3
# print(str('hi'))            # hi
# print(str('hi'.upper()))    # HI



# sum(iterable)
#----------------------------------------------------
# 입력받은 리스트나 튜플의 모든 요소의 합을 돌려주는 함수

# print(sum([1,2,3]))     # 6
# print(sum((4,5,6,)))    # 15



# tuple(iterable)
#----------------------------------------------------
# 반복가능한 자료형을 입력받아 튜플형태로 바꾸어 돌려주는 함수.

# print(tuple([1,2,3]))       # (1,2,3)
# print(tuple("abc"))         # ('a','b','c')
# print(tuple((4,5,6,))       # (4,5,6)



# type(object)
#----------------------------------------------------
# 입력값의 자료형이 무엇인지 알려주는 함수

# print(type("abc"))                  # <class 'str'>
# print(type([1,2,3]))                # <class 'list'>
# print(type(open("test",'w')))       # <class '_io.TextIOWrapper'>



# zip(*iterable)
#----------------------------------------------------
# 동일한 개수로 이루어진 자료형을 묶어주는 역할을 하는 함수

# print(list(zip([1,2,3], [4,5,6])))              # [(1, 4), (2, 5), (3, 6)]
# print(list(zip([1,2,3],[4,5,6],[7,8,9])))       # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
# print(list(zip("abc","def")))                   # [('a', 'd'), ('b', 'e'), ('c', 'f')]



