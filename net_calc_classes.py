from __future__ import annotations
from ipaddress import IPv4Address, IPv4Network
from validators import ValidatorIpV4


class CalcSubnetIpv4:
    """
    Класс калькулятора подсети
    """
    def __init__(self):
        self.validator = ValidatorIpV4()

    def run(self, file: str) -> tuple:
        """
        Основной метод.
        Достаёт список ip-адресов из файла, вызывает валидации и находит подсеть
        """
        with open(file) as ips_file:
            ips_list = ips_file.read().splitlines()
            result_validating = self.validator.validating(ips_list)
            if result_validating[0]:
                return result_validating[0], self.calc_subnet(ips_list)
            return result_validating

    def calc_subnet(self, ips_list: list[str]) -> IPv4Network:
        """
        Метод расчёта подсети для списка ip-адресов
        """
        ips_list = [IPv4Address(ip) for ip in ips_list]
        min_ip = min(ips_list)
        max_ip = max(ips_list)
        ip_range = 0
        net = IPv4Network(f'{min_ip}/32', strict=False)
        while max_ip not in net:
            ip_range += 1
            net = IPv4Network(f'{min_ip}/{32 - ip_range}', strict=False)
        return net
