

# a = [1, 2, 3]
# b = a
# print(id(a))
# print(id(b))
# print(a is b)     # True
# a[1] = 8
# print(a)
# print(b)

# a = [1,2,3]
# b = a[:]
# print(id(a))
# print(id(b))
# print(a is b)     # False
# a[1] = 7
# print(a)
# print(b)

# a = [1,2,3]
# from copy import copy
# b = copy(a)
# print(a is b)     # False
# print(id(a))
# print(id(b))
# a[1] = 5
# print(a)
# print(b)


# 변수를 만드는 여러가지 방법
# a, b = ('python', 'life')   # 튜플을 이용하여 a, b 에 값을 대입
# print(a)
# print(b)
# print(type(a))
# print(type(b))
# print(a is b)     # False

# (a, b) = 'python', 'life'   # 튜플은 괄호를 생략해도 된다.
# print(a)
# print(b)
# print(type(a))
# print(type(b))
# print(a is b)     # False

# [a, b] = ['python', 'life']
# print(a)
# print(b)
# print(type(a))
# print(type(b))
# print(a is b)     # False

# a = b = 'python'
# print(a)
# print(b)
# print(type(a))
# print(type(b))
# print(a is b)     # True

# a = 3
# b = 5
# a, b = b, a
# (a, b) = (b, a)
# [a, b] = [b, a]
# print(a)
# print(b)
# print(type(a))
# print(type(b))
# print(a is b)     # False

