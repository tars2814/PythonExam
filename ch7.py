

# data = """
# park 800905-1049118
# kim 700905-1059119
# """

# result = []
# for line in data.split("\n"):
#     word_result = []
#     for word in line.split(" "):
#         if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
#             word = word[:6] + "-" + "*******"
#         word_result.append(word)
#     result.append(" ".join(word_result))
# print(result)
# print("\n".join(result))



# 정규표현식

# import re

# pat = re.compile("(\d{6})[-]\d{7}")
# print(pat.sub("\g<1>-******", data))




### 메타문자(meta characters)
# 원래 그 문자가 가진 뜻이 아닌 특별한 용도로 사용하는 문자를 말한다.
# . ^ $ * + ? { } [ ] \ | ( )
# 정규표현식에 메타문자를 사용하면 특별한 의미를 갖게 된다.


### 문자 클래스(character class) []

# 문자 클래스로 만들어진 정규식은 "[] 사이의 문자들과 매치" 라는 의미를 갖는다
# [] 안의 두 문자 사이에 하이프(-)을 사용하면 두 문자 사이의 범위(From - To)를 의미한다.
# 문자 클래스[] 안에 어떤 문자나 메타 문자도 사용할수 있지만 ^ 를 사용할 경우에는 반대(not)의 의미를 갖는다.
# 예를들어 [^0-9] 는 숫자가 아닌 문자만 매치된다.

# \d - 숫자와 매치, [0-9] 와 동일
# \D - 숫자가 아닌것과 매치, [^0-9] 와 동일
# \s - whitespace 문자와 매치, [ \t\n\r\f\v]와 동일, 맨앞의 빈칸은 공백문자(space)를 의미한다
# \S - whitespace 문자가 아닌것과 매치, [^ \t\n\r\f\v]와 동일
# \w - 문자+숫자(alphanumeric)와 매치, [a-zA-Z0-9_]와 동일
# \W - 문자+숫자(alphanumeric)가 아닌 문자와 매치, [^a-zA-Z0-9_]와 동일


### Dot(.)
# 정규 표현식의 Dot(.) 메타 문자는 줄바꿈 문자인 \n을 제외한 모든 문자와 매치됨을 의미한다.

## a.b      : 정규식의 의미는 "a + 모든문자 + b"
# "aab" - a.b 와 매치
# "a0b" - a.b 와 매치
# "abc" - a.b 와 미채되지 않음. a 와 b 사이에 어떤문자 하나는 있어야 함.

## a[.]b    : 정규식의 의미는 "a + Dot(.)문자 + b"


### 반복 (*)
# 바로 앞에 있는 문자가 0부터 무한대(메모리 제한으로 사실상 2억개정도 가능)로 반복될 수 있다는 의미

# 정규식 ca*t
# ct    - 0번 반복되어 매치
# cat   - 1번 반복되어 매치
# caaat - 3번 반복되어 매치


### 반복 (+)
# (*) 와 다르게 최소 한번이상 반복될때 사용.

# 정규식 ca+t
# ct    - 0번 반복되어 매치되지 않음
# cat   - 1번 반복되어 매치
# caaat - 3번 반복되어 매치



### 반복 ({m,n},?)
# m 은 최소 횟수 생략하면 0
# n 은 최대 횟수 생략하면 무한대
# {1,} 은 + 와 동일하고 {0,}은 *와 동일하다

## 정규식 ca{2}t 는 "c + a(반드시 2번 반복) + t"
# cat   - 매치되지 않음
# caat  - 매치

## 정규식 ca{2,5}t
# cat           - 매치 안됨
# caat          - 매치
# caaaaat       - 매치


## ?
# ? 메타문자가 의미하는 것은 {0,1} 이다

# 정규식 ab?c 는 "a + b(있어도 되고 없어도 된다) + c"

# abc       - 매치
# ac        - 매치



### 정규식을 이용한 문자열 검색
# match()       - 문자열의 처음부터 정규식과 매치되는지 조사
# search()      - 문자열 전체를 검색하여 정규식과 매치되는지 조사
# findall()     - 정규식과 매치되는 모든 문자열(substring)을 리스트로 돌려준다
# finditer()    - 정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 돌려준다

# match, searc 는 정규식과 매치될 때는 match 객체를 돌려주고, 매치되지 않을때는 None을 돌려준다.

# import re                       # 정규표현식을 지원하기 위한 모듈
# p = re.compile('[a-z]+')        # 정규표현식을 컴파일하고 돌려받는 객체를 패턴이라고 한다.

## match
"""
m = p.match("python")
print(m)

if m:
    print("Match found")
else:
    print("No match")

m = p.match("3 python")
print(m)

if m:
    print("Match found")
else:
    print("No match")
"""

## search
"""
s = p.search("python")
print(s)
s = p.search("3 python")
print(s)
"""


## findall
'''
result = p.findall("Life is too short")
print(result)
# >>>
# ['ife', 'is', 'too', 'short']
'''


### finditer
# 반복 가능한 객체를 돌려준다. 반복 가능한 객체가 포함하는 각가의 요소는 match 객체이다.
'''
result = p.finditer("Life is too short")
print(result)
# >>>
# <callable_iterator object at 0x00000247127EF5B0>

for r in result:
    print(r)
# >>>
# <re.Match object; span=(1, 4), match='ife'>     
# <re.Match object; span=(5, 7), match='is'>      
# <re.Match object; span=(8, 11), match='too'>    
# <re.Match object; span=(12, 17), match='short'> 
'''



### match 객체의 메서드

# group()       - 매치된 문자열을 돌려준다.
# start()       - 매치된 문자열의 시작 위치를 돌려준다.
# end()         - 매치된 문자열의 끝 위치를 돌려준다.
# span()        - 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 돌려준다.

'''
import re
p = re.compile('[a-z]+')

m = p.search("365 python")
if m:
    print(m.group())    # python
    print(m.start())    # 4
    print(m.end())      # 10
    print(m.span())     # (4, 10)
'''

## 모듈 단위로 수행하기
'''
import re

m = re.search('[a-z]+', '365 python')

if m:
    print(m.group())    # python
    print(m.start())    # 4
    print(m.end())      # 10
    print(m.span())     # (4, 10)
'''



### 컴파일 옵션
# DOTALL(S)         - (.) 이 줄바꿈 문자를 포함하여 모든 문자와 매치할 수 있도록 한다.
# IGNORECASE(I)     - 대소문자에 관계없이 매치할 수 있도록 한다.
# MULTILINE(M)      - 여러줄과 매치할 수 있도록 한다. (^, $ 메타문자의 사용과 관계가 있는 옵션)
# VERBOSE(X)        - verbose 모드를 사용할 수 있도록 한다. (정규식을 보기 편하게 만들수 있고 주석등을 사용할 수 있게된다.)



import re

## DOTALL, S

# p = re.compile('a.b')
# m = p.match('a\nb')
# print(m)    # None


# p = re.compile('a.b', re.DOTALL)
# # p = re.compile('a.b', re.S)
# m = p.match('a\nb')
# print(m)    # <re.Match object; span=(0, 3), match='a\nb'> 



## IGNORECASE, I
'''
p = re.compile('[a-z]', re.I)
m = p.match('python')
print(m)            # <re.Match object; span=(0, 1), match='p'>
m = p.match('PYTHON')
print(m)            # <re.Match object; span=(0, 1), match='p'>
'''



## MULTILINE, M
'''
p = re.compile("^python\s\w+", re.M)

data = """python one
life is too short
python two
you need python
python three python four"""

print(p.findall(data))      # ['python one', 'python two', 'python three']

'''


## VERBOSE, X
'''
charref = re.compile(r'&[#](0[07]+|[0-9]+|x[0-9a-fA-F]+);')

charref = re.compile(r"""
&[#]                    # Start of a numeric entity reference
(
    0[0-7]+             # Octal form
    | [0-9]+            # Decimal form
    | x[0-9a-fA-F]+     # Hexadecimal form
)
;                       # Trailing semicolon
""", re.VERBOSE)

'''



## |
## or 와 동일한 의미로 사용된다.

# p = re.compile('Crow|Servo')
# m = p.match('CrowHellow')
# print(m)            # <re.Match object; span=(0, 4), match='Crow'>



## ^
# 문자열의 맨 처음과 일치함을 의미

# print(re.search('^Life', 'Life is too short'))          # <re.Match object; span=(0, 4), match='Life'>
# print(re.search('^Life', 'My Life'))                    # None



## $
# 문자열의 끝과 매치함을 의미한다.

# print(re.search('short$', 'Life is too short'))             # <re.Match object; span=(12, 17), match='short'>
# print(re.search('short$', 'Life is too short, you need python'))        # None


## \A
# ^ 와 동일한 의미지만 re.MULTILINE 옵션을 사용할 경우 다르게 해석됨
# re.MULTILINE 옵션을 사용할 경우 ^는 각 줄의 문자열의 처음과 매치되지만
# \A 는 줄과 상관없이 전체 문자열의 처음하고만 매치 되낟.

## \Z
# 문자열의 끝과 매치됨을 의미한다.
# \A 와 동일하게 re.MULTILINE 옵션을 할 경우 $와 달리 전체 문자열의 끝과 매치된다.


## \b
# 단어 구분자(Word boundary)이다. 보통 단어는 whitespace에 의해 구분된다.

# p = re.compile(r'\bclass\b')
# print(p.search('no class at all'))                  # <re.Match object; span=(3, 8), match='class'>
# print(p.search('the declassified algorithm'))       # None
# print(p.search('one subclass is'))                  # None


## \B
# \b 의 반대 경우. 즉 whitespace로 구분된 단어가 아닌 경우에만 매치된다.
'''
p = re.compile(r'\Bclass\B')
print(p.search('no class at all'))                  # None
print(p.search('the declassified algorithm'))       # <re.Match object; span=(6, 11), match='class'>
print(p.search('on sebclass is'))                   # None
'''


### 구루핑 (Grouping)
# 메타문자는 ( ) 이다
# group 인덱스
# group(0)      - 매치된 전체 문자열
# group(1)      - 첫번째 그룹에 해당되는 문자열
# group(2)      - 두번째 그룹에 해당되는 문자열
# group(n)      - n번째 그룹에 해당되는 문자열

# p = re.compile('(ABC)+')
# m = p.search('ABCABCABC OK?')
# print(m)                # <re.Match object; span=(0, 9), match='ABCABCABC'>
# print(m.group())        # ABCABCABC

# p = re.compile(r'(\w+)\s+((\d+)[-]\d+[-]\d+)')
# m = p.search('park 010-1234-1234')
# print(m)                    # <re.Match object; span=(0, 18), match='park 010-1234-1234'>
# print(m.group(0))           # park 010-1234-1234
# print(m.group(1))           # park
# print(m.group(2))           # 010-1234-1234
# print(m.group(3))           # 010



### 그루핑된 문자열 재참조(Backreferences)하기

# p = re.compile(r'(\b\w+)\s+\1')
# print(p.search('Paris in the the spring').group())      # the the


### 그루핑된 문자열에 이름 붙이기

# p = re.compile(r'(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)')
# m = p.search('park 010-1234-5678')
# print(m.group("name"))              # park


# p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
# m = p.search('Paris in the the spring')
# if m:
#     print(m.group())        # the the




### 전방 탐색 (Lookahead Assertions)

# p = re.compile(".+:")
# m = p.search("http://google.com")
# print(m.group())            # http:


## 긍정형(Positive) 전방 탐색 (?=...)       ... 에 해당되는 정규식과 매치되어야 하며 조건이 통과되어도 문자열이 소비되지 않는다.

p = re.compile(".+(?=:)")
m = p.search("http://google.com")
print(m.group())            # http

# :에 해당하는 문자열이 정규식 엔진에 의해 소비되지 않아(검색에는 포함되지만 검색 결과에는 제외됨) 검색 결과에서는
# :이 제거된 후 돌려주는 효과가 있다.



## 부정형(Negative) 전방 탐색 (?!...)       ... 에 해당되는 정규식과 매치되지 않아야 하며 조건이 통과되어도 문자열이 소비되지 않는다.


