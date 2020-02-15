class yuan :
    def __init__(self,zhong,li):
        self.zhong =zhong
        if "骑兵" in zhong:
            self.zhon = 2
        else :
            self.zhon = 1
        self.li = li*self.zhon
    def __str__(self):
        if self.zhon == 2 :
            return "此处有%s%d,可以一敌二"%(self.zhong,self.li/2)
        elif self.zhon == 1 :
            return "此处有%s%d"%(self.zhong,self.li)

class cheng :
    def __init__(self,name,rong):
        self.name = name
        self.rong = rong
        self.shen = rong
        self.bing = []
    def add(self,bing):
        if self.shen-bing.li >= 0 :
            self.bing.append(bing.zhong)
            self.shen += -bing.li
        else:
            print("城内无法容纳如此兵力")
    def __str__(self):
        return "%s中可容%d兵力，现还可进%d，兵营中有%s"%(self.name,self.rong,self.shen,self.bing)

red = yuan("狼骑兵",100)
belu = yuan("弓兵",500)
wangsi = cheng("枉死城",1000)
wangsi.add(red)
wangsi.add(belu)
print(wangsi)
print(red)
print(belu)

