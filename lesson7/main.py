from menu import Menu
import function as fn

menuitems = [
        ("1", "Вывод автобусов"),
        ("2", "Добавление автобуса"),
        ("3", "Вывод водителей"),
        ("4", "Добавление водителей"),
        ("5", "Вывод маршрута"),
        ("6", "Добавление маршрута"),
        ("7", "Удаление записи"),
        ("8", "Детализация маршрута"),
        ("9", "Выход")
]

for i in menuitems:
    print(i[0], i[1])

while True:
    text = input("Введите номер: ")
    if text == '1':
        print(fn.show_data('bus.txt'))
    elif text == '2':
        fn.add_bus()
    elif text == '3':
        print(fn.show_data('driver.txt'))
    elif text == '4':
        fn.add_driver()
    elif text == '5':
        print(fn.show_data('route.txt'))
    elif text == '6':
        fn.add_route()
    elif text == '7':
        fn.del_record()
    elif text == '8':
        fn.route_details()
    elif text == '9':
        break
