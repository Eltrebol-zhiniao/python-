woaini = ["xin","gan","pi"]
woaini[2] = "b"
print(woaini[2])
print(woaini.index("gan"))

woaini.append("everything")
woaini.insert(2,"小妹妹")
# 使用参数
xixi = ["deijiner","cipi","shuhu"]
woaini.extend(xixi)

woaini.remove("b")
woaini.pop(2)

print(woaini)
