from multiprocessing import Process


def proc_func(num:int):
    num_list = []
    for i in range(2, num + 1):
        num_list.append(i)

    for x in num_list:
        for z in num_list:
            if z == x:
                continue
            if z % x == 0:
                num_list.remove(z)
    num_list.insert(0, 1)
    print(num_list)


if __name__ == '__main__':
    var = 0
    num = int(input('Введите диапазон '))
    new_process = Process(target=proc_func, args=(num,))
    new_process.start()
    new_process.join()
    print(f"{new_process.name} finished")
