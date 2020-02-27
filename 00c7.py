choumeimei = [
    {"luoli":"jinkesi"},
    {"luoli":"anni"}
]
zhao = input("你找啥呢")
for lol in choumeimei:
    print(lol)
    if lol["luoli"] == zhao:
        print("有的")
        break
else:
    print("莫德")
print("over")
