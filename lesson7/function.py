def read_data_from_file(name):
    result = []
    with open(name, 'r', encoding='utf8') as datafile:
        for line in datafile:
            result.append(line.strip('\n').split(";"))
        return result


def save_data_to_file(name, data_list, rewrite='a'):
    with open(name, rewrite, encoding='utf8') as datafile:
        datafile.writelines(data_list)


def show_data(filename):
    return read_data_from_file(filename)


def add_bus():
    file_name = 'bus.txt'

    name = input("Введите имя автобуса в формате busХ: ")
    num = input("Введите госномер: ")
    data = name + ";" + num + "\n"
    save_data_to_file(file_name, data)

    return "Запись об автобусе добавлена"


def add_driver():
    file_name = 'driver.txt'

    name = input("Введите ID водителя в формате driverХ: ")
    num = input("Введите ФИО: ")
    data = name + ";" + num + "\n"
    save_data_to_file(file_name, data)

    return "Запись о водителе добавлена"


def add_route():
    file_name = 'route.txt'

    name = input("Введите ID маршрута в формате routeХ: ")
    num = input("Введите номер маршрута: ")
    driver_id = input("Введите ID водителя: ")
    bus_id = input("Введите ID автобуса: ")
    data = name + ";" + num + ";" + driver_id + ";" + bus_id + "\n"
    save_data_to_file(file_name, data)

    return "Запись о маршруте добавлена"


def del_record():
    menuitems = [
        ("1", "Удалить автобус"),
        ("2", "Удалить водителя"),
        ("3", "Удалить маршрут"),
    ]

    for i in menuitems:
        print(i[0], i[1])

    file_name = ''

    text = input("Введите номер: ")

    if text == '1':
        file_name = 'bus.txt'
    elif text == '2':
        file_name = 'driver.txt'
    elif text == '3':
        file_name = 'route.txt'

    data = show_data(file_name)

    i = 0
    for line in data:
        print(f'{i} - {line}')
        i += 1

    str_to_change = int(input("Введите номер записи, которую хотите удалить: "))

    del data[str_to_change]

    new_lines = []
    for line in data:
        new_lines.append(";".join(line) + '\n')

    save_data_to_file(file_name, new_lines, "w")

    return "Запись удалена"


def search_name(file_name, search_str):
    data = read_data_from_file(file_name)

    new_list = []
    for line in data:
        if search_str in line[0]:
            new_list.append(line)

    return new_list


def route_details():
    file_name = 'route.txt'
    data = show_data(file_name)

    i = 0
    for line in data:
        print(f'{i} - {line}')
        i += 1

    route_to_view = int(input("Введите номер маршрута: "))

    bus_search = search_name('bus.txt', data[route_to_view][2])
    driver_search = search_name('driver.txt', data[route_to_view][3])

    bus_str = None
    driver_str = None

    if bus_search:
        bus_str = bus_search[0][1]
    if driver_search:
        driver_str = driver_search[0][1]

    print(f'Название маршрута - {data[route_to_view][0]}, номер маршрута - {data[route_to_view][1]}, '
          f'автобус - { bus_str if bus_str else "Неизвестен"}, водитель - {driver_str if driver_str else "Неизвестен"}')
