
# Q1

# a = 80
# b = 75
# c = 55
# d = (a + b + c) / 3
# print(d)    # 70.0



# Q2

# a = 13
# print(a % 2)    # 1 (나머지가 1이므로 홀수)



# Q3

# a = "881120-1068234"
# print(a[:6])      # 881120
# print(a[7:])      # 1068234



# Q4

# pin = "881120-1068234"
# print(pin[-7])      # 1



# Q5

# a = "a:b:c:d"
# print(a.replace(':','#'))     # a#b#c#d



# Q6

# a = [1, 3, 5, 4, 2]
# a.sort()
# a.reverse()
# print(a)        # [5, 4, 3, 2, 1]



# Q7

# a = ['Life','is','too','short']
# print(" ".join(a))      # Life is too short



# Q8

# a = (1, 2, 3)
# a = a + (4,)
# print(a)      # (1, 2, 3, 4)



# Q9

# a = dict()
# a['name'] = 'python'
# a[('a',)] = 'python'
# a[250] = 'python'
# # a[[1]] = 'python'     # TypeError: unhashable type: 'list', 리스트는 Key 로 사용될 수 없다.
# print(a)



# Q10

# a = {'A':90, 'B':80, 'C':70}
# a.pop('B')
# print(a)        # {'A': 90, 'C': 70}



# Q11

# a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
# a = list(set(a))
# print(a)        # [1, 2, 3, 4, 5]



# Q12

# a = b = [1, 2, 3]
# a[1] = 4
# print(b)        # [1, 4, 3]