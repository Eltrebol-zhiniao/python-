class tianshi:
    def __init__(self,name,gongli):
        self.name = name
        self.gongli = gongli
    def __del__(self):
        print("%s现在修为有%d"%(self.name,self.gongli))
    def bu (self,ci):
        print("%s修习了%d遍雷法"%(self.name,ci))
        self.gongli += ci
    def xie (self):
        print("%s泄露了元阳"%self.name)
        self.gongli += -10

yang = tianshi("张楚岚",40)
ying = tianshi("张灵玉",80)

yang.bu(22)
ying.xie()