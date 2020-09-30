import os
userdata = 0
list_of_files = os.listdir("res")
usercat = 0
for file in list_of_files:
    file = open('res/' + file, 'r')
    category = file.readline().split(',')
    print(category)
    if usercat == 0:
        usercat = input('Введите категорию поиска:')
    if usercat in category:
        count = category.index(usercat)
        if userdata == 0:
            userdata = input('Введите искомое слово:')
        for line in file:
            data = line.split(',')
            if userdata == data[count]:
                print('время начала сессии в unixtime:', data[0])
                print('время конца сессии в unixtime:', data[1])
                print('длительность сессии:', data[2])
                print('логин пользователя:', data[3])
                print('мак адрес абонента:', data[4])
                print('идентификатор сессии:', data[5])
                print('ip провайдерского оборудования, через которое шла связь с пользователем:', data[6])
                exit()
    else:
        print('Неверная категория')
        exit()
print('Данные некорректны или совпадений не найдено')
