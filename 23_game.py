# 用python设计第一个游戏
# 猜数游戏
"""
temp = input("不妨猜一下小甲鱼心里想的是哪个数字：")
guess = int(temp)

if guess == 8:
    print("你是小甲鱼心里的蛔虫嘛！")
    print("哼，猜中了也没奖励！")
else:
    print("猜错了，小甲鱼现在心里想的是8！")
print("游戏结束，不玩啦（*＾-＾*）")
"""
import random
anwser = random.randint(1, 100)
count = 10
try:
    while count > 0:
        print(f"您还有{count}次机会。")
        temp = input("请输入1到100的一个整数：")
        guess = int(temp)
        if guess == anwser:
            print("恭喜您答对了！")
            print("游戏结束！")
            break
        else:
            if guess > anwser:
                print("很遗憾，您猜的数大了。")
            else:
                print("很遗憾，您猜的数小了。")
        count -= 1
        if count == 0:
            print("很遗憾，您的次数用完了！")
            print("游戏结束")
except ValueError:
    print("请输入合理的数字，并再次运行程序")