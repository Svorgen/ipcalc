from argparse import ArgumentParser
from net_calc_classes import CalcSubnetIpv4

parser = ArgumentParser()
parser.add_argument('file', type=str, help='Путь к файлу со списком ip-адресов')
parser.add_argument('version', type=int, help='Версия ip-адреса.')
args = parser.parse_args()


def main(args):
    if args.version == 4:
        calculator = CalcSubnetIpv4()
        result = calculator.run(args.file)
        print(result[1]) if result[0] else print(calculator.validator.get_error_string(result[1]))

    else:
        print('В настоящий момент поддерживатся только ip версии 4')


if __name__ == '__main__':
    main(args)
