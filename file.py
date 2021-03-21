
# ====================
# Function
# ====================

# 파일 생성하기
# 파일객체 = open(파일이름, 파일 열기 모드)
# 파일 열기모드:
# 'r' 읽기모드 - 파일을 읽기만 할때 사용
# 'w' 쓰기모드 - 파일에 내용을 쓸 때 사용
# 'a' 추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬 떄 사용

# ex1
# f = open("NewFile.txt", 'w')
# f.close()

# 파일을 쓰기 모드로 열면 해당 파일이 이미 존재할 경우 원래 있던 내용이 모두 사라지고,
# 해당 파일이 존재하지 않으면 새로운 파일이 생성된다.



# 파일을 쓰기 모드로 열어 출력값 적기

# ex2
# f = open("NewFile.txt", 'w')
# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()


# 프로그램의 외부에 저장된 파일을 읽는 여러가지 방법

#readline() 함수 이용하기

#ex3
# f = open("NewFile.txt", 'r')
# line = f.readline()
# print(line)
# f.close()
# >>>
# 1번째 줄입니다.
# 파일의 첫번째 줄을 읽어 출력하였음


# 모든 줄을 읽어서 화면에 출력
# ex4
# f = open("NewFile.txt", 'r')
# while True:
#     line = f.readline()
#     if not line: break      # readline() 은 더이상 읽을 줄이 없을 경우 빈 문자열 ('')을 리턴한다
#     print(line)
# f.close()




# readlines 함수 이용하기
# readlines 함수는 파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 돌려준다.
# ex5
# f = open("NewFile.txt", 'r')
# lines = f.readlines()
# for line in lines:
#     print(line)
# f.close()




# read 함수 이용하기

#ex6
# f = open("NewFile.txt", 'r')
# data = f.read()
# print(data)
# f.close
# # f.read() 는 파일의 내용 전체를 문자열로 돌려준다.




# 파일에 새로운 내용 추가하기

# ex7
# f = open("NewFile.txt", 'a')
# for i in range(11, 20):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()




# with문과 함께 사용하기
# with문을 사용하면 with 블록을 벗어나는 순간 열린 파일 객체가 자동으로 close되어 편리하다

# ex8
# f = open("foo.txt", 'w')
# f.write("Life is too short, you need python")
# f.close()


# ex9
# with open("foo.txt", 'a') as f:
#     f.write("Life is too short, you need python")


# ex10
# import sys

# args = sys.argv[1:]
# for i in args:
#     print(i)


# ex11
# import sys
# args = sys.argv[1:]
# for i in args:
#     print(i.upper(), end=' ')

