file = open("telegram_clear_data.txt", "r")
nickname = input('Искомый ник: ')
for line in file:
    data = line.split('|')

    if data[6] == nickname:
        print('системный номер: ', data[1])
        print('name: ', data[2])
        print('fname: ', data[3])
        print('phone: ', data[4])
        print('uid: ', data[5])
        print('nik: ', data[6])
        print('wo: ', data[7])
        exit()
print('Не найдено совпадений')

'''
import os
file = open("telegram_clear_data.txt", "r")
b = os.path.getsize("telegram_clear_data.txt")
cntr = b//166
'''
