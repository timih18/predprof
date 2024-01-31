from random import randint
import csv


def password_generator(passwords):
    symbols = ['QWERTYUIOPASDFGHJKLMNBVCXZ', 'qwertyuiopasdfghjklzxcvbnm', '1234567890']
    password = ''
    checker = set()
    for _ in range(8):
        ind = randint(0, 2)
        checker.add(ind)
        password = password + symbols[ind][randint(0, len(symbols[ind])-1)]
    if checker == {0, 1, 2} and password not in passwords:
        passwords.add(password)
        return password
    else:
        password_generator(passwords)


with open('students.csv', encoding='utf8') as file:
    reader = csv.reader(file, delimiter=',')
    answer = list(reader)
    answer = answer[1:]

used_passwords = set()

with open('students_password.csv', 'w', encoding='utf8', newline='') as file:
    write = csv.writer(file)
    write.writerow(['id', 'Name', 'titleProject_id', 'class', 'score', 'login', 'password'])
    for ID, FIO, title, CLASS, score in answer:
        login = f"{FIO[:FIO.find(' ')]}_{FIO[FIO.find(' ') + 1]}{FIO[FIO.rfind(' ') + 1]}"
        PASSWORD = password_generator(used_passwords)
        write.writerow([ID, FIO, title, CLASS, score, login, PASSWORD])

