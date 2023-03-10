"""
输入一个年份，判断是否为闰年
输入一个四位数年份
能被4整除不能被100整除或者可以被四百整除的为闰年，否则为平年
"""
try:
    year = int(input("请输入一个四位数年份: "))
    if (year % 4 == 0 or year % 100 != 0) and (year % 400 == 0):
        print(f"{year}是闰年。")
    else:
        print(f"{year}是平年。")
except ValueError:
    print("请输入合理的年份，并重新运行程序。")

