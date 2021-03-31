# 하위 디렉터리 검색하기


import os


def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py':
                    print(full_filename)
    except PermissionError:
        pass

search("c:/Users/kim/Documents")


# os.walk 를 이용한 방법

# for (path, dir, files) in os.walk("c:/Users/kim/Documents"):
#     for filename in files:
#         ext = os.path.splitext(filename)
#         if ext[-1] == '.py':
#             print("%s/%s" % (path, filename))


