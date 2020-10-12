from argparse import ArgumentParser
from net_calc_classes import CalcSubnetIpv4


def main():
    parser = ArgumentParser()
    parser.add_argument('file', type=str, help='Путь к файлу со списком ip-адресов')
    parser.add_argument('version', type=int, help='Версия ip-адреса.')
    args = parser.parse_args()
    if args.version == 4:
        calculator = CalcSubnetIpv4()
        # При успешном прохождении валидаций в переменной work_result будет объект искомой подсети
        # В противном случае там будет лежать словарь с кодами ошибок, который необходимо распарсить
        # и показать пользователю сообщения с ошибками
        validate_result, work_result = calculator.run(args.file)
        print(work_result) if validate_result else print(calculator.validator.get_error_string(work_result))
    else:
        print('В настоящий момент поддерживатся только ip версии 4')


if __name__ == '__main__':
    main()
