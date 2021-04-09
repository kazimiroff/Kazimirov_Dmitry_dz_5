#1

def gen(n):
    for i in range(n):
        if i % 2 != 0:
                yield i
odd_to_n = gen(15)

print(list(odd_to_n)) #для проверки генерируемых чисел
print(type(odd_to_n)) #для проверки что это генератор



