import csv

with open('anketa.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow({'Name', 'Surname', 'Age', 'Human Gender', 'City', 'Email', 'Phone' })

def input_data():
    name = input('Enter your name: ')
    surname = input('Enter your surname: ')
    age = input('Enter your age: ')
    human_gender = ('Enter Human gender: ')
    city = input('Enter your city: ')
    email = input('Enter your email: ')
    phone = input('Enter your phone: ')
    return[name, surname, age, gender, city, email, phone]

with open('anketa.csv', 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    data = input_data()
    writer.writerow(data)

with open('anketa.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
