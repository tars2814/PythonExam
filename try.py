
# ex1

# try:
#     a = [1,2]
#     print(a[3])
#     4/0
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")
# except IndexError:
#     print("인덱싱 할 수 없습니다.")





# ex2

# try:
#     a = [1,2]
#     print(a[3])
#     4/0
# except ZeroDivisionError as e:
#     print("0으로 나눌 수 없습니다.")
#     print(e)
# except IndexError as e:
#     print("인덱싱 할 수 없습니다.")
#     print(e)





# ex3

# try:
#     a = [1,2]
#     print(a[3])
#     4/0
# except (ZeroDivisionError, IndexError) as e:
#     print(e)




# ex4

# try:
#     age = int(input("나이를 입력하세요:"))
# except:
#     print("입력이 정확하지 않습니다.")
# else:
#     if age <= 18:
#         print("미성년자는 출입금지입니다.")
#     else:
#         print("환영입니다.")




# ex5
# 오류 회피하기

# try:
#     f = open("나없는파일", 'r')
# except FileNotFoundError:
#     pass




# ex6
# 오류 일부러 발생시키기

# class Bird:
#     def fly(self):
#         raise NotImplementedError

# class Eagle(Bird):
#     def fly(self):
#         print("very fast")

# eagle = Eagle()
# eagle.fly()




# 예외 만들기


# ex7

# class MyError(Exception):
#     pass

# def say_nick(nick):
#     if nick == '바보':
#         raise MyError()
#     print(nick)

# say_nick("천사")
# say_nick("바보")




# ex8

class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)





