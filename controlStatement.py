


# ====================
# if 문
# ====================

# if 조건문:
#     수행할 문장1
#     수행할 문장2
#     ...
# else:
#     수행할 문장A
#     수행할 문장B
#     ...


# money = True

# if money:
#     print("택시를 타고 가라")
# else:
#     print("걸어 가라")

# # > 택시를 타고 가라



# money = 2000
# card = True

# if money >= 3000 or card:
#     print("택시를 타고 가라")
# else:
#     print("걸어가라")

# # > 택시를 타고 가라



# ====================
# x in s, x not in s
# ====================

# x in 리스트
# x in 튜플
# x in 문자열
# x not in 리스트
# x not in 튜플
# x not in 문자열

# a = [1,2,3]
# if 1 in a:
#     print(bool(1))
# else:
#     print(bool(0))

# # > True


# a = (1,2,3)
# if 4 in a:
#     print(bool(1))
# else:
#     print(bool(0))

# # > False


# pocket = ['paper', 'cellphone', 'money']

# if 'money' in pocket:
#     print(bool(1))
# else:
#     print(bool(0))

# # > True


# pocket = ['paper', 'cellphone', 'money']

# if 'paper' in pocket:
#     pass      # 아무일도 하지 않는다.
# else:
#     print("paper")



# pocket = ['paper', 'cellphone', 'money']
# card = True

# if 'money' in pocket:
#     print("택시를 타고 가라")
# elif card:
#     print("택시를 타고 가라")
# else:
#     print("걸어가라")

# > 택시를 타고 가라



# ====================
# 조건부 표현시
# 조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우
# ====================

# if score >= 60:
#     message = "success"
# else:
#     message = "failure"

# message = "successs" if socre >= 60 else "failure"




# ====================
# while 문
# ====================
# while <조건문>:
#   <수행할 문장1>
#   <수행할 문장2>
#   <수행할 문장3>
#   ...


# treeHit = 0
# while treeHit < 10:
#     treeHit = treeHit + 1
#     print("나무를 %d번 찍었습니다." % treeHit)
#     if treeHit == 10:
#         print("나무 넘어갑니다.")



# prompt = """
# 1. Add
# 2. Del
# 3. List
# 4. Quit

# Enter number:"""

# number = 0
# while number != 4:
#     print(prompt)
#     number = int(input())




# coffee = 10
# money = 300
# while money:
#     print("돈을 받았으니 커피를 줍니다.")
#     coffee = coffee - 1
#     print("남은 커피의 양은 %d개 입니다." % coffee)
#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
#         break;



# coffee = 10
# while True:
#     money = int(input("돈을 넣어주세요: "))
#     if money == 300:
#         print("커피를 줍니다.")
#         coffee = coffee - 1
#     elif money > 300:
#         print("거스름돈 %d를 주고 커피를 줍니다." % (money - 300))
#         coffee = coffee - 1
#     else:
#         print("돈을 다시 돌려주고 커피를 주지 않습니다.")
#         print("남은 커피의 양은 %d개 입니다." % coffee)

#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
#         break;



# a = 0
# while a < 10:
#     a = a + 1
#     if a % 2 == 0: continue
#     print(a)






# ====================
# for 문
# ====================
# for 변수 in 리스트(또는 튜플, 문자열):
#    수행할 문장1
#    수행할 문장2
#    ...


# test_list = ['one', 'two', 'three']
# for i in test_list:
#     print(i)
# # > one
# # > two
# # > three


# a = [(1,2), (3,4), (5,6)]
# for (first, last) in a:
#     print(first + last)

# # > 3
# # > 7
# # > 11


# marks = [90, 25, 67, 45, 80]
# number = 0

# for mark in marks:
#     number = number + 1
#     if mark > 60:
#         print("%d번 학생은 합격입니다." % number)
#     else:
#         print("%d번 학생은 불합격입니다." % number)

# # 1번 학생은 합격입니다.
# # 2번 학생은 불합격입니다.
# # 3번 학생은 합격입니다.  
# # 4번 학생은 불합격입니다.
# # 5번 학생은 합격입니다.



# marks = [90, 25, 67, 45, 80]
# number = 0
# for mark in marks:
#     number = number + 1
#     if mark < 60:
#         continue

#     print("%d번 학생 축하합니다. 합격입니다." % number)

# # 1번 학생 축하합니다. 합격입니다.
# # 3번 학생 축하합니다. 합격입니다.
# # 5번 학생 축하합니다. 합격입니다.



# a = range(10)
# print(a)    # range(0, 10)

# range(시작 숫자, 끝 숫자), 이때 끝 숫자는 포함되지 않는다.

# add = 0
# for i in range(1, 11):
#     add = add + i

# print(add)      # 55



# marks = [90, 25, 67, 45, 80]

# for number in range(len(marks)):
#     if marks[number] < 60:
#         continue
#     print("%d번 학생 축하합니다. 합격입니다." % number)

# # 0번 학생 축하합니다. 합격입니다.
# # 2번 학생 축하합니다. 합격입니다.
# # 4번 학생 축하합니다. 합격입니다.



# for i in range(2, 10):
#     for j in range(1, 10):
#         print(i*j, end=" ")
#     print('')

# 2 4 6 8 10 12 14 16 18    
# 3 6 9 12 15 18 21 24 27   
# 4 8 12 16 20 24 28 32 36  
# 5 10 15 20 25 30 35 40 45 
# 6 12 18 24 30 36 42 48 54 
# 7 14 21 28 35 42 49 56 63 
# 8 16 24 32 40 48 56 64 72 
# 9 18 27 36 45 54 63 72 81 



# List comprehension (리스트 내포) 사용하기
# 일반 문법 > "표현식 for 항목 in 반복가능객체 if 조건문", if 조건문은 생략 가능

# a = [1, 2, 3, 4]
# result = []

# for num in a:
#     result.append(num*3)

# print(result)   # [3, 6, 9, 12]

# # 위의 코드를 List comprehension 으로 표현
# a = [1, 2, 3, 4]
# result = [num * 3 for num in a]
# print(result)   # [3, 6, 9, 12]


# 요소값 중 짝수인 경우에만 3을 곱하여 리스트를 구성
# a = [1, 2, 3, 4]
# result = [num * 3 for num in a if num % 2 == 0]
# print(result)   # [6, 12]


result = [x*y for x in range(2, 10)
    for y in range(1, 10)]

print(result)

# [2, 4, 6, 8, 10, 12, 14, 16, 18, 3, 6, 9, 12, 15, 18, 21, 24, 27, 4, 8, 12, 16, 20, 24, 28, 32, 36, 5, 10, 15, 20, 25, 30, 35, 40, 45, 6, 12, 18, 24, 30, 36, 42, 48, 54, 7, 14, 21, 28, 35, 42, 49, 56, 63, 8, 16, 24, 32, 40, 48, 56, 64, 72, 9, 18, 27, 36, 45, 54, 63, 72, 81]
