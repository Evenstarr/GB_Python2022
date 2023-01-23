def read_data_from_file(name):
    result = []
    with open(name, 'r', encoding='utf8') as datafile:
        for line in datafile:
            result.append(line.strip('\n').split(";"))
        return result


def save_data_to_file(name, data_list, rewrite='a'):
    with open(name, rewrite, encoding='utf8') as datafile:
        datafile.writelines(data_list)


def show_data():
    data = read_data_from_file('phones.txt')
    return data


def search_name():
    search_str = input("Введите часть имени: ")
    data = read_data_from_file('phones.txt')

    new_list = []
    for line in data:
        if search_str in line[0]:
            new_list.append(line)

    return new_list


def add_record():
    name = input("Введите имя: ")
    patr = input("Введите отчество: ")
    surname = input("Введите фамилию: ")
    phone = input("Введите телефон: ")
    data = name + ";" + patr + ";" + surname + ";" + phone + "\n"
    save_data_to_file('phones.txt', data)

    return "Запись добавлена"


def search_phone():
    search_str = input("Введите часть телефона: ")
    data = read_data_from_file('phones.txt')

    new_list = []
    for line in data:
        if search_str in line[3]:
            new_list.append(line)

    return new_list


def change_phone():
    data = show_data()

    i = 0
    for line in data:
        print(f'{i} - {line}')
        i += 1

    str_to_change = int(input("Введите номер записи, у которой хотите изменить телефон: "))
    new_phone = input("На что меняем? ")

    data[str_to_change][3] = new_phone

    new_lines = []
    for line in data:
        new_lines.append(";".join(line) + '\n')

    save_data_to_file("phones.txt", new_lines, "w")

    return "Телефон изменен"


def del_record():
    data = show_data()

    i = 0
    for line in data:
        print(f'{i} - {line}')
        i += 1

    str_to_change = int(input("Введите номер записи, которую хотите удалить: "))

    del data[str_to_change]

    new_lines = []
    for line in data:
        new_lines.append(";".join(line) + '\n')

    save_data_to_file("phones.txt", new_lines, "w")

    return "Запись удалена"

