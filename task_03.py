#3

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]

klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]



if len(tutors) < len(klasses):
    tutors.append(None)

def tup_zip():
    for i in range(len(tutors)):
        yield tutors[i], klasses[i]

gen = tup_zip()

print(list(gen))#для проверки генерируемых чисел
print(type(gen)) #для проверки что это генератор


