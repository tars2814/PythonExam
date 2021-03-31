

# 메모장 만들기
# 필요한 기능? 메모 추가하기, 메모 조회하기
# 입력 받는 값은? 메모 내용, 프로그램 실행 옵션
# 출력하는 값은? memo.txt

# 다음 명령을 실행했을 때 메모를 추가할 수 있도록 만들어 봅시다.
# python memo.py -a "Life is too short"

import sys

option = sys.argv[1]

# print(sys.argv[0])
# print(option)
# print(memo)

if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()

# 메모의 출력
# python memo.py -v

elif option == '-v':
    f = open('memo.txt', 'r')
    rm = f.read()
    f.close()
    print(rm)

