
# Q1

# class Calculator:
#     def __init__(self):
#         self.value = 0

#     def add(self, val):
#         self.value += val


# class UpgradeCalculator(Calculator):
#     def minus(self, val):
#         self.value -= val


# cal = UpgradeCalculator()
# cal.add(10)
# cal.minus(7)

# print(cal.value)



# Q2

# class Calculator:
#     def __init__(self):
#         self.value = 0
    
#     def add(self, val):
#         self.value += val


# class MaxLimitCalculator(Calculator):
#     def add(self, val):
#         self.value += val
#         if self.value > 100:
#             self.value = 100

# cal = MaxLimitCalculator()
# cal.add(50)
# cal.add(60)
# print(cal.value)



# Q4

# a = [1,-2,3,-5,8,-3]
# b = list(filter(lambda x:x>0, a))

# print(b)



#Q5

# print(int('ea', 16))



# Q6

# a = [1,2,3,4]
# b = list(map(lambda x:x*3, a))
# print(b)




# Q7

# a = [-8,2,7,5,-3,-5,0,1]

# print(max(a))   # 7
# print(min(a))   # -8




# Q8

# a = 17/3
# print(a)
# print(round(a, 4))




# Q9

# import sys

# numbers = sys.argv[1:]

# result = 0
# for number in numbers:
#     result += int(number)

# print(result)

