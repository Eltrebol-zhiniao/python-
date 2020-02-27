python_1 = int(input("python考了多少鹅"))
c11_1 = int(input("c++考了多少鸭"))

#总分大于130或者单科大于80分就及格
if python_1>=80 or c11_1>=80 or python_1+c11_1>=130:
    if python_1>100 or c11_1>100 or python_1+c11_1>200:
        print("小孩子不要吹牛逼")
    else:print("小火鸡恭喜你通过了咱的考验！"
          "明天来上班！")
else:
    print("我们公司是有狼性的"
          "你这个情况不太符合哟")
