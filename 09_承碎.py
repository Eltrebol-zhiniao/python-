class dao :
    def pi(self):
        print("劈")

    def kan(self):
        print("砍")

class taidao(dao):
    def ci(self):
        print("刺")

cunyu = taidao()
cunyu.pi()
cunyu.kan()
cunyu.ci()