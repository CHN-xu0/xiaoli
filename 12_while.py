"""
for循环有明确的循环次数或对象更合适
while循环通用，特别是不知道循环次数的
while 条件：
    命令
"""
# 写一个计算器，最后输入q表示结束，输入数字求平均值
print("哈喽呀！我是一个求平均值的程序。")
total = 0
count = 0
user_input = input("请输入数字 (完成所有数字输入后，请输入q终止程序) :")
while user_input != "q":
    num = float(user_input)
    total += num
    count += 1
    user_input = input("请输入数字 (完成所有数字输入后，请输入q终止程序) :")
if count == 0:
    result = 0
else:
    result = total / count    # 存在count等于0的情况，需考虑
print("您输入的数字平均值为" + str(result))
