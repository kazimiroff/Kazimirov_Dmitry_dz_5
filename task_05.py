#5

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
src_2 = set(src)
res = []

for i in src:
    if i in src_2 and i in res:
        res.remove(i)

    else:
        res.append(i)
    src_2.add(i)

print(res)