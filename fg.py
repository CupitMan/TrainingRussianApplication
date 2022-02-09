import csv
with open('AllAccents.csv', 'r', encoding='utf-8') as file:
    read = csv.reader(file)
    for i in read:
        print(i)