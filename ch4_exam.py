

# Q1

# def is_Odd(data):
#     if (data % 2):
#         return True
#     else:
#         return False

# print(is_Odd(3))



# Q2

# def getavg(*args):
#     result = 0
#     for i in args:
#         result += i
    
#     return (result/len(args))

# avg = getavg(1, 2, 3, 4, 5)
# print(avg)



# Q3

# input1 = input("첫번째 숫자를 입력하세요:")
# input2 = input("두번째 숫자를 입력하세요:")

# total = int(input1) + int(input2)
# print("두 수의 합은 %s 입니다." % total)



# Q5

# f1 = open("test.txt", 'w')
# f1.write("Life is too short")
# f1.close()

# f2 = open("test.txt", 'r')
# print(f2.read())
# f2.close()


# with open("test.txt", 'w') as f1:
#     f1.write("Life is too short")

# with open("test.txt", 'r') as f2:
#     print(f2.read())


# Q6

# with open("test.txt", 'a') as f:
#     f.write("\n%s" % input())




# Q7

# f = open("test.txt", 'r')
# body = f.read()
# f.close()

# body = body.replace('python', 'java')

# f = open("test.txt", 'w')
# f.write(body)
# f.close()

