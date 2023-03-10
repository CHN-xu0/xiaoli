"""
三行四列 长方形
****
****
****
"""
for i in range(1, 4):
    for j in range(1, 5):
        print("*", end="")
    print()
print("____________")
"""
五行 直角三角形
*
**
***
****
*****
"""
for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end="")
    print()
print("____________")
"""
倒直角三角形
*****
****
***
**
*
"""
for i in range(1, 6):
    for j in range(1, 7-i):
        print("*", end="")
    print()
print("____________")
"""
输出等腰三角形
    *
   ***
  *****
 *******
*********

"""
for i in range(1, 6):
    for j in range(1, 6-i):
        print(" ", end="")
    for k in range(1, 2*i):
        print("*", end="")
    print()
print("____________")
"""
菱形
   *
  ***
 *****
*******
 *****
  ***
   *
"""
# try:
#     row = int(input("请输入菱形的行数："))
#     top_row = (row + 1) // 2
#     # 上半部分
#     for i in range(1, top_row + 1):
#         for j in range(1, top_row + 1 - i):
#             print(" ", end="")
#         for k in range(1, 2*i):
#             print("*", end="")
#         print()
#     # 下半部分
#     bottom_row = row // 2
#     for i in range(1, bottom_row + 1):
#         for j in range(1, i + 1):
#             print(" ", end="")
#         for k in range(1, 2 * (bottom_row + 1 - i)):
#             print("*", end="")
#         print()
# except ValueError:
#     print("请输入合理的数字，并重新运行程序。")
# print("____________")
"""
空心菱形
"""
row = int(input("请输入菱形的行数："))
top_row = (row + 1) // 2
# 上半部分
for i in range(1, top_row + 1):
    for j in range(1, top_row + 1 - i):
        print(" ", end="")
    for k in range(1, 2 * i):
        if k == 1 or k == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
# 下半部分
bottom_row = row // 2
for i in range(1, bottom_row + 1):
    for j in range(1, i + 1):
        print(" ", end="")
    for k in range(1, 2 * (bottom_row + 1 - i)):
        if k == 1 or k == 2 * (bottom_row + 1 - i) - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
