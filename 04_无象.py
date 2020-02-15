class YeMao:
    def __init__(self,she,zhang):
        self.name = she
        self.shen = zhang
    def __del__(self):
        # 在类之外del会立即删除,否则最后
        print("baybay")
    def __str__(self):
        return "它是只%s的小猫，名叫%s"%(self.shen,self.name)
    def lueying(self):
        print("黑夜中掠过一道%s的影子"%self.shen)
    def aiming(self):
        print("夜色里仿佛有婴儿啼哭,原来是%s"%self.name)

pty = YeMao("胖头🐟鱼","圆滚滚")
# pty.name = "胖头鱼"
pty.aiming()
pty.lueying()
print(pty)
# print(pty) pty的地址
# difan = id(pty)
# print("%x" % difan) d是十进制x是16进制