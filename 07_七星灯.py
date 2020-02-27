class xing :
    def __init__(self,name,ji):
        self.name = name
        self.ji = ji

class deng :
    def __init__(self,name):
        self.name = name
        self.xing = None
    def zhu (self,xin):
        if xin.ji > 7 :
            print("%s星超出%s灯可承载之力"%(xin.name,self.name))
        else:
            self.xing = xin
            print("%s灯中放入了星力%d的%s星魄"%(self.name,xin.ji,xin.name))
    def dian(self):
        if self.xing is not None :
            self.xing.ji += 1
            print("点燃愿力后%s灯中星力增至%d"%(self.name,self.xing.ji))
        else:print("%s中并无星魄"%self.name)
    def xm(self):
        print("点燃了%s灯"%self.name)
        if self.xing is not None:
            if self.xing.ji == 7 :
                print("七星皆至，七魂尽归")
                self.xing.ji -= 7
            else:print("灯不辟命，魂飞魄丧")
        else:print("%s中并无星魄" % self.name)
jin = xing("天狼",4)
hun = deng("七星")
hun.zhu(jin)
hun.dian()
hun.xm()