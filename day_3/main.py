"""
Loi trong python :
- La nhung bat thuong xay ra khi chay chuong trinh
- Co cac loai loi trong python: TypeError, ValueError, KeyError, SyntaxError, IndexError
- Cach xu ly cac loi: dung cac khoi try- except- finally- else
"""

# # IndexError
# lst = [1, 2, 3, 4]
# print(lst[4])

# # ValueError
# print(int("4.5"))

# # KeyError
# d = {'a': 1, 'b': 2, 'c': 3}
# print(d['f'])

"""
- khoi try: thu xem chuong trinh co loi hay khong?
- khoi except: neu khoi try co loi thi xu ly loi trong khoi except
- khoi finally: luon chay cho du trong try co loi 
- khoi else: chay khi trong try khong co loi
"""

# #Vd1
# try:
#     print(1/0)
# except Exception as e:
#     print(e)
# else:
#     print("Success")
# finally:
#     print("Always run")

#vd2
try:
    print(1/2)
except Exception as e:
    print(e)
else:
    print("Success")
finally:
    print("Always Run")


"""Module
+ Module thong thuong la 1 file python trong do chua code ma cac file python khac co the import va su dung
+ Co hai loai Module:
    - module co san: sys, random, math, ..
    - module tu dinh nghia: cac file python ma chung ta tao ra trong thu muc du an
"""

