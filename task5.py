import csv


def gen_hash(fio):
    s = 'ЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮёйцукенгшщзхъфывапролджэячсмитьбю '
    p = 67
    m = 10**9 + 9
    power = 1
    hash = 0
    for c in fio:
        hash += ((s.index(c) + 1) * power) % m
        power = (power * p) % m
    return hash


with open('students (1).csv', encoding='utf8') as file:
    reader = csv.reader(file, delimiter=',')
    answer = list(reader)
    for i in range(1, len(answer)):
        answer[i][0] = gen_hash(answer[i][1])


with open('students_with_hash.csv', 'w', encoding='utf8', newline='') as file:
    write = csv.writer(file)
    write.writerows(answer)
