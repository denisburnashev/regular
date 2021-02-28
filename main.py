import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# print(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ

edit_contacts_list = []
edit_phone = []

for info in contacts_list:
    new_dict_lastname = info[0].split(' ')
    if new_dict_lastname[-1] == 'Мартиняхин' not in edit_contacts_list:
        pass
    else:
        edit_contacts_list.append(new_dict_lastname)
    if info[1] != '':
        for elem in info[1].split(' '):
            new_dict_lastname.append(elem)
    if info[2] != '':
        new_dict_lastname.append(info[2])
    if info[3] != '':
        new_dict_lastname.append(info[3])
    if info[4] != '':
        new_dict_lastname.append(info[4])
    if info[5] != '':
        phones = info[5]
        find_phones = re.compile(r'(\+7|8)\s*\(*(\d{3})\)*[\s-]*(\d{3})[\s-]*'
                                 r'(\d{2})[\s-]*(\d{2})[\s]*(\(*(\D{3}\.)\s(\d+)\)*)*')
        edit_phones = find_phones.sub(r'+7(\2)\3-\4-\5 \7\8', phones)
        new_dict_lastname.append(edit_phones)
    if info[6] != '':
        new_dict_lastname.append(info[6])

edit_contacts_list.pop()


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(edit_contacts_list)
