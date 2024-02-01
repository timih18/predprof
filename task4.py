from random import randint
import csv


def password_generator(used_passwords):
    global password
    res = ''
    check_set = set()
    symbols = ['QWERTYUIOPASDFGHJKLMNBVCXZ', 'qwertyuiopasdfghjklzxcvbnm', '1234567890']
    for _ in range(8):
        ind = randint(0, 2)
        res = res + symbols[ind][randint(0, len(symbols[ind])-1)]
        check_set.add(ind)
    if check_set == {0, 1, 2} and res not in used_passwords:
        used_passwords.append(res)
        password = res
    else:
        password_generator(used_passwords)


with open('students.csv', encoding='utf8') as file:
    reader = csv.reader(file, delimiter=',')
    answer = list(reader)
    answer = answer[1:]

passwords = []

with open('students_password.csv', 'w', encoding='utf8', newline='') as file:
    write = csv.writer(file)
    write.writerow(['id', 'Name', 'titleProject_id', 'class', 'score', 'login', 'password'])
    for ID, FIO, title, CLASS, score in answer:
        login = f"{FIO[:FIO.find(' ')]}_{FIO[FIO.find(' ') + 1]}{FIO[FIO.rfind(' ') + 1]}"
        password = ''
        password_generator(passwords)
        write.writerow([ID, FIO, title, CLASS, score, login, password])
