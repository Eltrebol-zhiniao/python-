#.#!后面加解释器路径就可以用终端直接运行
#chmod + x 跟文件名可以给执行权限
choes = "0"
zhanghao = []
while choes < "4" :
    #TO do(显示没做完的) 数据储存和回车不修改！
    print("="*50)
    print("1.创建角色\n2.查看角色\n3.角色管理\n4.退出游戏")
    print("-"*50)
    choes = input("快给我选！\n" )
    if choes == "1" :
        mz = input("请输入角色名\n" )
        xb = input("角色性别\n" )
        nl = input("努力值\n" )
        new = {"名字":mz,"性别":xb,"努力值":nl}
        zhanghao.append(new)
        input("添加%s成功,回车返回"% mz)
    elif choes == "2" :
        print("-"*50)
        print("名字\t\t性别\t\t努力值")
        for kan in zhanghao :
            print("%-8s%-7s%-8s"% (kan["名字"],
                  kan["性别"],kan["努力值"]))
        else:input("--任意健返回")
    elif choes == "3" :
        nage = input("你想改谁？\n")
        for gai in zhanghao :
            xl = -1
            xl += 1
            if gai["名字"] == nage :
                zazuo = input("你想对%s做什么?\n1.修改属性\t2.删除角色"% nage)
                if zazuo == "1":
                    def inpu(yao,gai,bie) :
                        """输入账号信息
                        :param yao:修改对象
                        :param gai:对象属性
                        :param bie:修改参数"""
                        bie = input("输入新的角色%s："% yao)
                        if len(bie) == 0 :
                            return gai
                        else:
                            return bie

                    print(gai)
                    zhanghao[xl] = {"名字":inpu("名字",gai["名字"],"bie"),
                                        "性别":inpu("性别",gai["性别"],"bie"),
                                        "努力值":inpu("努力值",gai["努力值"],"bie")}

                elif zazuo == "2":
                    zhanghao.remove(zhanghao[xl])
                break
        else:
            print("不存在该角色")
        input("--回车键返回")
