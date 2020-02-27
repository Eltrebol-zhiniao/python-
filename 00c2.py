laopo = {"name":"地理热巴",
         "zu":"维吾尔",
         "height":"170"}

print(laopo["zu"])
laopo["xiaosan"] = "星悦"
# laopo.pop("name")
sanwei = {"xiong":36,
          "yao":30,
          "pi":35}
laopo.update(sanwei)
# laopo.clear()
# print(len(laopo))
for wo in laopo :
    print("%s-%s"% (wo,laopo[wo]))