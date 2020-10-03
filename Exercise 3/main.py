import PySimpleGUI as sg
print('Вы находитесь в главном меню. Выберите нужную операцию:\n1) Зашифровать/Расшифровать\n2) Сгенерировать ключ')
choice = int(input('Операция под номером:'))
if choice == 1:
    print('Выбран вариант 1')
    choice = int(input('1) Шифровать\n2) Дешифровать\nВаш выбор:'))
    if choice == 1:
        text = sg.popup_get_file('Выберите файл с текстом:')

    #elif choice == 2:

    #choice = int(input('Шифры:\n1) Замены\n2) Перестановки\n3) Гаммирования\nВаш выбор:'))

elif choice == 2:
    print('Выбран вариант 2')