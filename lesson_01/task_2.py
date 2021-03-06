"""
2. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона.
Меняться должен только последний октет каждого адреса.
По результатам проверки должно выводиться соответствующее сообщение.
"""

from ipaddress import ip_address
from task_1 import host_ping, get_host_by_name


def host_range_ping():
    """
    Функция для перебора ip-адресов из заданного диапазона.
    :return: возврат списка адресов из указанного диапазона с указанием на доступность
    """
    while True:
        # запрос первоначального адреса
        start_ip = input('Введите первоначальный адрес: ')
        try:
            # смотрим чему равен последний октет
            last_octet = int(start_ip.split('.')[3])
            break
            # обойдём исключение: IndexError
        except IndexError:
            try:
                start_ip = get_host_by_name(start_ip)
                last_octet = int(start_ip.split('.')[3])
                break
            except Exception as e:
                print(e)
    while True:
        # запрос на количество проверяемых адресов
        quantity_ip = input('Сколько адресов проверить?: ')
        if not quantity_ip.isnumeric():
            print('Необходимо ввести число: ')
        else:
            # по условию меняется только последний октет
            if (last_octet+int(quantity_ip)) > 254:
                print(f"Можем менять только последний октет, т.е. "
                      f"максимальное число хостов для проверки: {254-last_octet}")
            else:
                break

    host_list = []
    # формируем список ip адресов
    [host_list.append(str(ip_address(start_ip)+x)) for x in range(int(quantity_ip))]
    # передаем список в функцию из задания 1 для проверки доступности
    return host_ping(host_list)


if __name__== "__main__":
    host_range_ping()

# Введите первоначальный адрес: yandex.ru