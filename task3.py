import csv


with open('students.csv', encoding='utf8') as file:
    reader = csv.reader(file, delimiter=',')
    answer = list(reader)
    answer = answer[1:]

id_project = input()
while id_project != 'СТОП':
    flag = False
    for ID, FIO, title, CLASS, score in answer:
        if title == id_project:
            flag = True
            name = FIO[FIO.find(' ') + 1]
            surname = FIO[:FIO.find(' ')]
            print(f'Проект № {id_project} делал: {name}. {surname} он(а) получил(а) оценку - {score}')
    if not flag:
        print('Ничего не найдено')
    id_project = input()
