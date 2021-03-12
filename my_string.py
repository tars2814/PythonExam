
# ====================
# STRING (문자열 자료형)
# ====================

### 문자열을 만드는 방법
# a = "Hello World"
# b = 'Python is fun'
# c = """Life is too short, You need phthon"""
# d = '''Life is too short, You need phtyon'''
# print(a)    # Hello World
# print(b)    # Python is fun
# print(c)    # Life is too short, You need phtyon
# print(d)    # Life is too short, You need phtyon


### 작은 따옴표와 큰 따옴표를 문자열에 포함시키려면 문자열을 반대의 따옴표로 둘러싼다.
# a = 'Python's favorite food is perl'
# print(b)  # Syntax Error

# a = "Python's favorite food is perl"
# print(a)  # Python's favorite food is perl

# a = '"Python is very easy." he says.'
# print(a)    # "Python is very easy." he says.

# a = """"Python's favorite food is perl" he says."""
# print(a)


### 백글래시(\)를 사용해서 작은따옴표와 큰따옴표를 문자열에 포함시킬수 있다.
# food = 'Python\'s favorite food is perl'
# say = "\"Python is very easy.\" he says."
# print(food)     # Python's favorite food is perl
# print(say)      # "Python is very easy." he says.


### 여러 줄인 문자열을 변수에 대입하고 싶을때
# multiline = "Life is too short\nYou need python"
# print(multiline)
# > Life is too short
# > You need python  

# multiline = '''
# Life is too short
# You need python
# '''
# print(multiline)
# > Life is too short
# > You need python  

# multiline2 = """
# Live is too short
# You need phthon
# """
# print(multiline2)
# > Life is too short
# > You need python  


### 이스케이프 코드
# \n    문자열 안에서 줄을 바꿀 때
# \t    문자열 사이에 탭 간격을 줄 때
# \\    문자(\)를 그대로 표현할 때
# \'    작은따옴표(')를 그대로 표현할 때
# \"    큰따옴표(")를 그대로 표현할 때
# \r    캐리지 리턴(줄 바꿈 문자, 현재 커서를 가장 앞으로 이동)
# \f    폼 피드(줄 바꿈 문자, 현재 커서를 다음 줄로 이동)
# \a    벨 소리(출력할 때 PC 스피커에서 '삑'소리가 난다)
# \b    백 스페이스
# \000  널 문자


# ====================
# 문자열 연산하기
# ====================

# Concatenation (문자열 더해서 연결하기)
# head = "Python"
# tail = " is fun"
# print(head + tail)
# > Python is fun


# 문자열 곱하기
# a = "Python"
# print(a * 3)
# > PythonPythonPython

# print("=" * 50)
# print("My Program")
# print("=" * 50)
# > ==================================================
# > My Program
# > ==================================================


# 문자열 길이 구하기
# a = "Life is too short"
# b = len(a)
# print(a)
# print(b)
# > Life is too short
# > 17


# ====================
# INDEXING
# ====================

# a = "Life is too short, You need Python"
# print(a[3], a[8], a[19])
# > e t Y
# print(a[-1], a[-3])
# > n h


# ====================
# SLICING
# ====================

# a = "Life is too short, You need Python"
# print(a[0] + a[1] + a[2] + a[3])    # > Life
# print(a[0:4])       # Life (0 <= a < 3, 끝번에 해당하는 것은 포함하지 않는다.)
# print(a[3:14])      # e is too sh
# print(a[:6])        # Life i
# print(a[19:])       # You need Python
# print(a[:])         # Life is too short, You need Python
# print(a[19:-7])     # You need


# a = "20010331Rainy"
# date = a[:8]
# weather = a[8:]
# print(date)     # 20010331
# print(weather)  # Rainy


# Pithon 이라는 문자열을 Python 으로 바꾸려면?
# a = "Pithon"
# # a[1] = 'y'  # TypeError, 문자열의 요솟값은 바꿀수 있는 값이 아니다.
# print(a[0] + 'y' + a[2:]) # Slicing 기법으로 새로운 문자열을 만든다.



# ====================
# FORMATTING (문자열 포매팅)
# ====================
# 문자열 안에 어떤값을 삽입하는 방법이다.

# 숫자 바로 대입
# a = "I eat %d apples." % 3
# print(a)    # I eat 3 apples.

# 문자열 바로 대입
# a = "I eat %s apples." % "five"
# print(a)    # I eat five apples.

# 숫자 값을 나타내는 변수로 대입
# number = 3
# a = "I eat %d apples." % number
# print(a)    # I eat 3 apples.

# 2개 이상의 값 넣기
# number = 10
# day = "three"
# print("I ate %d apples. so I was sick for %s days." % (number, day))
# # > I ate 10 apples. so I was sick for three days.

# 문자열 포맷 코드
# (%s)  string(문자열)
# (%c)  character(문자1개)
# (%d)  Integer(정수)
# (%f)  floating-point(부동소수)
# (%o)  8진수
# (%x)  16진수
# (%%)  Literal % (문자 % 자체)


# %s는 자동으로 %뒤에 있는 값을 문자열로 바꾼다.
# print("I have %s apples" % 3)   # I have 3 apples
# print("rate is %s" % 3.234)     # rate is 3.234

# %d와 %를 같이 쓸때 %%를 쓴다
# # print("Error is %d%" % 98)  # ValueError:incomplete foramt
# print("Error is %d%%" % 98)


# ====================
# 포맷 코드와 숫자 함께 사용하기
# ====================

# 정렬과 공백
# print("%10s" % "hi")    # '        hi' (전체길이가 10개인 문자열 공간에서 대입되는 값을 오른쪽으로 정렬하고 나머지는 공백으로)
# print("%-10sjane." % 'hi')  # 'hi        jane.' (길이가 10개인 문자열 공간에 대입되는 값을 왼쪽으로 정렬하고 나머지는 공백으로)

# 소수점 표현하기
# print("%0.4f" % 3.42134234)     # '3.4213' (소수점 4자리)
# print("%10.4f" % 3.4213423)     # '    3.4213' (길이가 10인 문자열 공간에서 오른쪽으로 정렬, 소수점 4자리까지 표시)

# format 함수를 사용한 포매팅
# print("I eat {0} apples".format(3))         # 'I eat 3 apples' ({0} 부분이 3으로 바뀜)
# print("I eat {0} apples".format("five"))    # 'I eat five apples'

# number = 3
# print("I eat {0} apples".format(number))    # 'I eat 3 apples'

# 2개 이상의 값 넣기
# number = 10
# day = "three"
# print("I ate {0} apples. so I was sick for {1} days".format(number, day))   # 'I ate 10 apples. so I was sick for three days'
# print("I ate {number} apples. so I was sick for {day} days".format(number=10, day=3))   # 'I ate 10 apples. so I was sick for 3 days'
# print("I ate {0} apples. so I was sick for {day} days".format(10, day=3))   # 'I ate 10 apples. so I was sick for 3 days'

# 왼쪽 정렬
# print("{0:<10}".format("hi"))     # 'hi        ' (치환되는 문자열을 왼쪽으로 정렬하고 길이를 10으로 맞춤)

# 오른쪽 정렬
# print("{0:>10}".format("hi"))       # '        hi'

# 가운데 정렬
# print("{0:^10}".format("hi"))       # '    hi    '

# 공백 채우기
# print("{0:=^10}".format("hi"))      # '====hi===='
# print("{0:=<10}".format("hi"))      # 'hi========'
# print("{0:!>10}".format("hi"))      # '!!!!!!!!hi'

# 소수점 표현하기
# y = 3.42134234
# print("{0:0.4f}".format(y))     # '3.4213' (소수점 4자리까지 표시)
# print("{0:10.4f}".format(y))     # '    3.4213'  (문자열 길이 10, 소수점 4자리까지 표시)

# '{' 또는 '}' 문자 표현하기
# print("{{ and }}".format())     # '{ and }'


# ====================
# f 문자열 포매팅 (Python v3.6 이상)
# ====================

# name = '홍길동'
# age = 30
# print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')     # '나의 이름은 홍길동입니다. 나이는 30입니다.'
# # f문자열 포매팅은 위와 같이 name, age와 같은 변수 값을 생성한 후에 그 값을 참조할 수 있다.

# f 문자열 포매팅은 표현식을 지원한다.
# age = 30
# print(f'나는 내년이면 {age+1}살이 된다.')   # '나는 내년이면 31살이 된다.'

#딕셔너리는 Key와 Value라는 것을 한 쌍으로 갖는 자료형.
# d = {'name':'홍길동', 'age':30}
# print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]입니다.)

# 정렬
# print(f'{"hi":<10}')    # 'hi        '
# print(f'{"hi":>10}')    # '        hi'
# print(f'{"hi":^10}')    # '    hi    '

# 공백채우기
# print(f'{"hi":=<10}')   # 'hi========'
# print(f'{"hi":=>10}')   # '========hi'
# print(f'{"hi":=^10}')   # '====hi===='

# 소수점
# y = 3.42134234
# print(f'{y:0.4f}')      # '3.4213'
# print(f'{y:10.4f}')     # '    3.4213'

# '{', '}' 문자 표시
# print(f'{{ and }}')     # { and }


# ====================
# 문자열 관련 함수들
# count, find, index, join, uppper, lower, lstrip, rstrip, strip, replace, split
# ====================

# 문자 개수 세기 (count)
# a = "hobby"
# print(a.count('b'))     # '2' (문자열 중 문자 b의 개수를 반환한다.)

# 위치 알려주기1 (find)
# a = "Python is the best choice"
# print(len(a))               # '25'
# print(a.find('b'))          # '14' (문자열 중 문자 b가 처음으로 나온 위치를 반환한다.)
# print(a.find('z'))          # -1 (찾는 문자나 문자열이 존재하지 않는다면 -1을 반환한다.)
# print(a.find('choice'))     # '19'

# 위치 알려주기2 (index)
# a = "Life is too short"
# print(len(a))           # '17'
# print(a.find('t'))      # '8'
# print(a.index('t'))     # '8'
# print(a.index('k'))     # ValueError: substring not found (찾는 문자나 문자열이 존재하지 않는다면 오류를 발생시킨다.)
# print(a.index('shor'))  # '12'

# 문자열 삽입 (join)
# print(",".join('abcd'))             # 'a,b,c,d' (abcd 문자열의 각각의 문자 사이에 ','를 삽입한다.)
# print(",".join(['a','b','c','d']))  # 'a,b,c,d' (리스트를 입력으로 사용할 수 있다.)

# 소문자를 대문자로 바꾸기 (upper)
# a = "hi"
# b = "Life is too short"
# print(a.upper())        # 'HI'
# print(b.upper())        # 'LIFE IS TOO SHORT'

# 대문자를 소문자로 바꾸기 (lower)
# a = "HI"
# b = "Life Is Too Short"
# print(a.lower())    # 'hi'
# print(b.lower())    # 'life is too short'

# 왼쪽 공백 지우기 (lstrip)
# a = "  hi  "
# b = "  Hi, there!   "
# print(a.lstrip())   # 'hi  ' (문자열 중 가장 왼쪽에 있는 한칸 이상의 연속된 공백들을 모두 지운다.)
# print(b.lstrip())   # 'Hi, there!   '

# 오른쪽 공백 지우기 (rstrip)
# a = "  hi  "
# b = "  Hi, there!   "
# print(a.rstrip())   # '  hi' (문자열 중 가장 오른쪽에 있는 한칸 이상의 연속된 공백을 모두 지운다.)
# print(b.rstrip())   # '  Hi, there!'

# 양쪽 공백 지우기 (strip)
# a = "  hi  "
# b = "  Hi, there!   "
# print(a.strip())    # 'hi' (문자열 양쪽에 있는 한칸 이상의 연속된 공백을 모두 지운다.)
# print(b.strip())    # 'Hi, there!'


# 문자열 바꾸기 (replace)
# a = "Life is too short"
# print(a.replace("Life", "Your leg"))    # 'Your leg is too short' (replace(바뀌게 될 문자열, 바꿀 문자열))

# 문자열 나누기 (split)
# a = "Life is too short"
# print(a.split())    # '['Life', 'is', 'too', 'short']'
# # split() 괄호안에 아무것도 넣지 않은경우에는 공백(스페이스, 탭, 엔터 등)을 기준으로 문자열을 나누어 준다.
# b = "a:b:c:d"
# print(b.split(':'))     # '['a', 'b', 'c', 'd']'
# # b.split(':') 처럼 괄호 안에 특정값이 있는 경우에는 괄호안의 값을 구분자로 해서 문자열을 나누어 준다.
# # 이렇게 나눈 값은 리스트에 하나씩 들어가게 된다.