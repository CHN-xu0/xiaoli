"""
模拟10086查询功能
输入1，显示当前话费余额
输入2，显示当前流量余额，单位为G
输入3，显示当前通话余额，单位为分钟
输入0，退出查询系统
"""
try:
    answer = "y"
    while answer == "y":
        print("___________欢迎使用10086查询功能___________")
        print("1.显示当前话费余额")
        print("2.显示当前流量余额")
        print("3.显示当前通话余额")
        print("0.退出查询系统")
        i = int(input("请选择要查询的功能："))
        if i == 1:
            print("当前余额还剩234.5元。")
        elif i == 2:
            print("当前流量余额20GB。")
        elif i == 3:
            print("当前通话余额200分钟。")
        elif i == 0:
            print("即将退出系统，感谢您的使用。再见！")
            break
        else:
            print("对不起，您输入的有误。请重新输入。")
        answer = input("还继续操作吗y/n:")
    else:
        print("即将退出系统，感谢您的使用。再见！")
except ValueError:
    print("请输入正确的数字，并重新启动系统。")
