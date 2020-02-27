xiuxian = input("道友的法术是？")
if  not xiuxian == "大罗洞观" or xiuxian == "双全手" :
    menpai = input("阁下师从何门？")
    if menpai == "禹皇门":
        input("失敬失敬")
    elif menpai == "射日神山" :
        input("打扰了")
    elif menpai == "洪天城":
       input("改日定当上门赔罪")
    else:
        input("%s的小辈也敢在此bb"% menpai)
else :
    menpai = "假的"
input("他是%s的人" % menpai)






