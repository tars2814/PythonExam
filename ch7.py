

data = """
park 800905-1049118
kim 700905-1059119
"""

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

import re

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-******", data))


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