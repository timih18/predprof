import csv


def insertion_sort(lst):
    for i in range(1, len(lst)):
        for j in range(i, 0, -1):
            if lst[j][0] < lst[j-1][0]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
            else:
                break
    return lst


sp = []

with open('students.csv', encoding='utf8') as file:
    reader = csv.reader(file, delimiter=',')
    answer = list(reader)
    answer = answer[1:]

    for ID, name, title, CLASS, score in answer:
        if '10' in CLASS:
            sp.append([int(score), name])

insertion_sort(sp)
sp = sp[::-1]
sp = sp[:3]

print('10 класс:')
place = 1
for score, FIO in sp:
    name = FIO[FIO.find(' ') + 1]
    surname = FIO[:FIO.find(' ')]
    print(f'{place} место: {name}. {surname}')
    place += 1
