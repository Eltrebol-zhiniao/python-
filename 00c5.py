poetry = ["\n龙绝\t",
          "鸷鸟\t",
          "曾闻龙吟悠悠尔\t",
          "今不见真鳞爪\n",
          "四下求解\n",
          "皆言已绝已绝"]
# for luanxie in poetry :
#     print("|%s|"% luanxie.strip().center(15,"　"))
poetry2 = "龙绝\t鸷鸟\t\n曾闻龙吟悠悠尔\t\n今不见真鳞爪\n四下求解\t\n皆言已绝已绝"

print(poetry2)
print(poetry2.split())

print("&".join(poetry))
