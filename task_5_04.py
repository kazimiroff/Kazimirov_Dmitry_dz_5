#4

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

res = []

for i in range(len(src)):
    if src[i - 1] < src[i]:
        res.append(src[i])
res.pop(0)

print(res)