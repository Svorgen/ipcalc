def write_ips(ips_list):
    """
    Функция для записи списка ip-адресов в файл
    :param ips_list:
    :return:
    """
    with open('tests/test_ips.txt', 'w') as file:
        file.write('\n'.join(ips_list))
