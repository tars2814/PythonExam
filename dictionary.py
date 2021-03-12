
# ====================
# Dictionary
# ====================
# 대응관계를 나타낼수 있는 자료형. 이를 연관배열(Associative array) 또는 해시(Hash)라고 한다.
# Key 와 Value를 한쌍으로 갖는 자료형이다.
# 리스트나 튜플처럼 순차적으로(sequential) 해당 요솟값을 구하지 않고 Key를 통해 Value를 얻는다.

# 기본 Dictionary의 모습
# {Key1:Value1, Key2:Value2, Key3:Value3, ...}
# Key 에는 변하지 않는 값을 사용하고, Value에는 변하는 값과 변하지 않는 값 모두 사용할 수 있다.
# dic = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
# a = {1: 'hi'}
# a = {'a':[1,2,3]}


# ====================
# Dictionary 쌍 추가하기
# ====================
# a = {1:'a'}
# a[2] = 'b'          # Key가 2, Value가 'b'라는 딕셔너리 쌍을 추가
# print(a)            # '{1: 'a', 2: 'b'}'   
# a['name'] = 'pey'   # Key가 'name', Value가 'pey'라는 딕셔너리 쌍을 추가
# print(a)            # '{1: 'a', 2: 'b', 'name': 'pey'}'
# a[3] = [1,2,3]      # Key가 3, Value가 리스트 [1,2,3]인 딕셔너리 쌍을 추가


# ====================
# Dictionay 요소 삭제하기
# ====================
# del a[1]            # Key가 1인 요소를 삭제.
# print(a)            # {2: 'b', 'name': 'pey', 3: [1, 2, 3]}


# ====================
# Key 사용해 Value 얻기
# 딕셔너리변수이름[Key]
# ====================
# grade = {'pey':10, 'julliet':99}
# print(grade['pey'])         # '10'
# print(grade['julliet'])     # '99'

# a = {1:'a', 2:'b'}
# print(a[1])       # 'a'
# print(a[2])       # 'b'

# a = {'a':1, 'b':2}
# print(a['a'])       # '1'
# print(a['b'])       # '2'

# dic = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
# print(dic['name'])      # 'pey'
# print(dic['phone'])     # '0119993323'
# print(dic['birth'])     # '1118'

# 리스트는 Key 로 쓸수 없다. (튜플은 Key로 쓸 수 있다.)
# a = {[1,2]:'hi'}        # TypeError: unhashable type: 'list'


# ====================
# 딕셔너리 관련 함수들
# keys, values, items, clear, get
# ====================

# Key 리스트 만들기 (keys)
# keys 함수를 호출하면 dict_keys 객체를 반환한다.
# a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
# print(a.keys())     # dict_keys(['name', 'phone', 'birth'])
# print(a)            # {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}

# for k in a.keys():
#     print(k)
# # name
# # phone
# # birth

# dict_keys 객체를 리스트로 변환
# print(list(a.keys()))       # ['name', 'phone', 'birth']


# Value 리스트 만들기 (values)
# values 함수를 호출하면 dict_values 객체를 반환한다.
# a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
# print(a.values())   # dict_values(['pey', '0119993323', '1118'])


# Key, Value 쌍 얻기 (items)
# items 함수는 Key와 Value의 쌍을 튜플로 묶은 값을 dict_items 객체로 돌려준다.
# a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
# print(a.items())    # dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')])

# Key:Value 쌍 모두 지우기 (clear)
# clear 함수는 딕셔너리 안의 모든 요소를 삭제한다. 빈 리스트를 [], 빈 튜픙르 ()로 표현하는 것과 마찬가지로
# 빈 딕셔너리도 {}로 표현한다.
# a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
# print(a.clear())        # 'None'
# print(a)                # {}


# Key로 Value얻기 (get)
# a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
# print(a.get('name'))    # 'pey'
# print(a.get('nokey'))   # 'None'
# # print(a['nokey'])       # KeyError: 'nokey'

# 딕셔너리 안에 찾으려는 Key 값이 없을 경우 미리 정해둔 디폴트 값('bar')을 가져오게 하고 싶을때
# get(x, '디폴트 값')을 사용한다.
# print(a.get('nokey', 'bar'))    # 'bar'


# 해당 Key가 딕셔너리 안에 있는지 조사하기 (in)
# a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
# print('name' in a)      # 'True'
# print('email' in a)     # 'False'
