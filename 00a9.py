#输入一个布尔变量x，使他大于1但不等于10
x = input("你听不听话嘛？")
if x == "我听话" or x == "听话" or x == "听":
    x = True
else:
    x = False
if not x:
    print("不听话就不给你买！")
else:
    print("听话咱不买")