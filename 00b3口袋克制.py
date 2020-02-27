#导入随机工具包
import random
#口袋属性测试
palyer = input("你要使用的精灵是？")
print("就决定是你了！%s !"% palyer)
if palyer == "木守宫" :
    palyer = 1
elif palyer == "火雉鸡" :
    palyer = 2
elif palyer == "沼跃鱼" :
    palyer = 3
else :
    print("您没有%s，请重新选择"% palyer)
    palyer = False
    print("(提示：您有火雉鸡，木守宫和沼跃鱼)")
if palyer :
    compurter = random.randint(1,3)
    if palyer > compurter :
        if compurter == 1:
            compurter = "木守宫"
        elif compurter == 2:
            compurter = "火雉鸡"
        elif compurter == 3:
            compurter = "沼跃鱼"
        print("你赢了，对方使用的是%s"% compurter)
    elif palyer == 1 and compurter ==3 :
        if compurter == 1:
            compurter = "木守宫"
        elif compurter == 2:
            compurter = "火雉鸡"
        elif compurter == 3:
            compurter = "沼跃鱼"
        print("你赢了，对方使用的是%s"% compurter)
    elif palyer == compurter :
        if compurter == 1:
            compurter = "木守宫"
        elif compurter == 2:
            compurter = "火雉鸡"
        elif compurter == 3:
            compurter = "沼跃鱼"
        print("你俩用的都是%s"% compurter)
    else :
        if compurter == 1:
            compurter = "木守宫"
        elif compurter == 2:
            compurter = "火雉鸡"
        elif compurter == 3:
            compurter = "沼跃鱼"
        print("你输了,对方使用的是%s"% compurter)

