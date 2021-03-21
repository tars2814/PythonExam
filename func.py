
# ====================
# Function
# ====================
# def 함수명(매개변수):
#    <수행할 문장1>
#    <수행할 문장2>
#    ...
    



# def add(a, b):
#     return a + b

# a = 3
# b = 4
# print(add(a, b))        # 7



# def say():
#     return "Hi"

# print(say())


# def add(a, b):
#     print("%d, %d의 합은 %d입니다." % (a, b, a+b))

# a = add(3, 5)   # 3, 5의 합은 8입니다.
# print(a)        # None


# def say():
#     print("Hi")

# say()


# 매개변수 지정하여 호출하기

# def add(a, b):
#     return a+b

# result = add(a=3, b=4)
# print(result)       # 7

# result = add(b=4, a=3)
# print(result)       # 7



# 입력값이 몇개가 될지 모를때
# def 함수이름(*매개변수) -> 입력값을 전부 모아서 튜플로 만들어 준다
#     <수행할 문장>
#     ...

# def add_many(*args):
#     result = 0
#     for i in args:
#         result = result + i

#     return result

# c = add_many(3, 5, 7, 9)
# print(c)    # 24
# c = add_many(1,2,3,4,5,6,7,8,9)
# print(c)    # 45


# def add_mul(choice, *args):
#     if choice == "add":
#         result = 0
#         for i in args:
#             result = result + i
#     elif choice == "mul":
#         result = 1
#         for i in args:
#             result = result * i
#     return result

# result = add_mul('add', 1,2,3,4,5)
# print(result)       # 15
# result = add_mul('mul', 1,2,3,4,5)
# print(result)       # 120


# 키워드 파라미터
# 키워드 파라미터를 사용할 때는 매개변수 앞에 별 두 개(**)를 붙인다.
# 입력되는 매개변수는 딕셔너리가 되고 모든 key=value형태의 결과값이 그 딕셔너리에 저장된다.

# def print_kwargs(**kwargs):
#     print(kwargs)

# print_kwargs(a=1)
# print_kwargs(name='foo', age=3)



# def add_and_mul(a,b):
#     return a+b, a*b

# result = add_and_mul(3, 4)              # 결과값으로 튜플을 반환한다.
# result1, result2 = add_and_mul(5, 6)    # 결과값을 따로 받고 싶을때
# print(result)       # (7, 12)   결과값으로 튜플을 반환한다.
# print(result1)      # 7 
# print(result2)      # 12


# 매개변수에 초기값 미리 설정하기
# def say_myself(name, old, man=True):
#     print("나의 이름은 %s 입니다." % name)
#     print("나이는 %d살입니다." % old)
#     if man:
#         print("남자입니다.")
#     else:
#         print("여자입니다.")

# say_myself("김동원", 45)
# # >>>
# # 나의 이름은 김동원 입니다.
# # 나이는 45살입니다.
# # 남자입니다.


# def say_myself(name, man=True, old=33):
#     print("나의 이름은 %s 입니다." % name)
#     print("나이는 %d살 입니다." % old)
#     if man:
#         print("남자입니다.")
#     else:
#         print("여자입니다.")

# say_myself("김동원")

# # >>>
# # SyntaxError: non-default argument follows default argument
# # 초기값을 놓은 매개변수 뒤에 초기값을 설정해 놓지 않은 매개변수는 사용할 수 없다.
# # def say_myself(name, man=True, old=33): 는 가능.


# a = 1
# def vartest(a):
#     a = a + 1

# vartest(a)
# print(a)    # 1


# a = 1
# def vartest(a):
#     a = a + 1
#     return a

# a = vartest(a)
# print(a)        # 2



# a = 1
# def vartest():
#     global a
#     a = a + 1

# vartest()
# print(a)        # 2


# lambda : 보통 함수를 한줄로 간결하게 만들때 사용한다.
# lambda 매개변수1, 매개변수2, ... : 매개변수를 이용한 표현식
# lambda 예약어로 만든 함수는 return 명령어가 없어도 결과값을 돌려준다.

# add = lambda a, b: a+b
# result = add(3,4)
# print(result)   # 7


# a = input("숫자를 입력하세요:")
# print(a)


print("life" "is" "too short")  # lifeistoo short
print("life"+"is"+"too short")  # lifeistoo short
print("life","is","too short")  # life is too short

for i in range(10):
    print(i, end=' ')

# >>> 0 1 2 3 4 5 6 7 8 9

