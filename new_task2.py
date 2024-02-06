import csv


with open('students (1).csv', encoding='utf8') as file:
    reader = csv.reader(file, delimiter=',')
    sp = list(reader)

for i in range(2, len(sp)):
    while i > 1 and sp[i][4] > sp[i-1][4]:
        sp[i], sp[i-1] = sp[i-1], sp[i]
        i -= 1

place = 1
print('10 класс:')
for ID, FIO, title, CLASS, score in sp:
    if score != 'None' and '10' in CLASS and place <= 3:
        name = FIO[FIO.find(' ') + 1]
        surname = FIO[:FIO.find(' ')]
        print(f'{place} место: {name}. {surname}')
        place += 1
