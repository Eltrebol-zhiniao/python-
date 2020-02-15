def gui(chong):
    if chong == 1 :
        return 1
    lian = gui(chong - 1)
    return chong + lian

wocao = gui(5)
print(wocao)