import function as fn


menuitems = [
        ("1", "Показать все записи"),
        ("2", "Найти запись по вхождению частей имени"),
        ("3", "Найти запись по телефону"),
        ("4", "Добавить новый контакт"),
        ("5", "Удалить контакт"),
        ("6", "Изменить номер телефона у контакта"),
        ("7", "Выход")]


for i in menuitems:
    print(i[0], i[1])

while True:
    text = input("Введите номер: ")
    if text == '1':
        print(fn.show_data())
    elif text == '2':
        print(fn.search_name())
    elif text == '3':
        print(fn.search_phone())
    elif text == '4':
        print(fn.add_record())
    elif text == '5':
        print(fn.del_record())
    elif text == '6':
        print(fn.change_phone())
    elif text == '7':
        break
