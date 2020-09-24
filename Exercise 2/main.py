
file = open('res/res_1.csv', 'r')
category = file.readline().split(',')
usercat = input('Введите категорию поиска:')
if usercat in category:
    count = category.index(usercat)
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
print('Данные некорректны')