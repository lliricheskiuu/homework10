# 1. Написать функцию read_file которая принимает один параметр - полный путь к файлу.
# В зависимости от расширения файла (txt, csv, json) считывает и возвращает данные из файла.
# Для csv использовать reader.
# Если расширение не соответствует заданным, то вывести текст "Unsupported file format"

import json
import csv


def read_txt(filename):
    with open(filename, 'r') as txt_file:
        data = txt_file.read()
    return data


def read_json(filename):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data


def read_csv(filename):
    with open(filename, 'r', encoding="utf-8") as csv_file:
        data = []
        reader = csv.reader(csv_file)
        for row in reader:
            data.append(row)
    return data


def read_file(filename):
    extension = filename.rsplit('.', 1)[-1]
    if extension == 'txt':
        res = read_txt(filename)
    elif extension == 'json':
        res = read_json(filename)
    elif extension == 'csv':
        res = read_csv(filename)
    else:
        res = "Unsupported file format"
    return res


print(read_file('json_file_r.json'))

###

# 2. Написать функцию write_file которая принимает два параметра - полный путь к файлу и данные.
# В зависимости от расширения файла (txt, csv, json) записывает данные в данный файл.
# Для csv использовать DictWriter.
# Если расширение не соответствует заданным, то вывести текст "Unsupported file format"


def write_txt(filename, data):
    with open(filename, 'w') as txt_file:
        txt_file.write(data)


def write_json(filename, data):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=2)


def write_csv(filename, data):
    with open(filename, 'w', encoding="utf-8") as csv_file:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def write_file(filename, data):
    extension = filename.rsplit('.', 1)[-1]
    if extension == 'txt':
        write_txt(filename, data)
    elif extension == 'json':
        write_json(filename, data)
    elif extension == 'csv':
        write_csv(filename, data)
    else:
        print("Unsupported file format")


# data = {"random": {"text_1": "qw", "text_2": "er", "text_3": "ty"}}
data = [{"Name": "Emma", "Age": 13, "Hair_color": "orange"}]
write_file('csv_file_w.csv', data)
