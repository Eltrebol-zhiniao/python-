
ec = "*"
ro = 1

while ro <= 5:
    rb = "^"*(8 - ro)
    print(ec,end=rb)
    ec += "*"
    ro += 1
    if ro:
        print()


