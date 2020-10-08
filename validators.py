from __future__ import annotations


class ValidatorIpV4:
    """
    Класс валидации IP-адресов версии 4
    """
    error_codes = {
        1: 'Количество октетов в ip-адресе v4 должно равняться 4',
        2: 'Значения в октетах должны быть числами в диапазоне от 0 до 255',
        3: 'Файл пуст'
    }

    def validating(self, ips_list: list[str]) -> tuple(bool, dict[str, list[int]]):
        """
        Основной метод, вызываемый для проверки списка адресов
        Возвращает словарь, ключами которого являются строки, описывающие ip-адрес в файле
        Значениями является список кодов результатов валидаций
        """
        if not ips_list:
            return False, {'': [3]}
        result_validating = self.validating_ips(ips_list)
        if not any(result_validating.values()):
            return True, result_validating
        return False, result_validating

    def get_error_string(self, result_validating: dict[str, list[int]]) -> str:
        """
        Метод принимает словарь с результатами валидаций и возвращает строку
        Используется для получения описания ошибок, которое нужно отобразить пользователю
        """
        error_string = 'Не все ip-адреса корректны\n'
        for key, codes in result_validating.items():
            if codes == [3]:
                return self.error_codes[3]
            if not all(codes):
                error_string += f'{key}: {codes}\n'
            else:
                for code in codes:
                    error_string += f'{key}: {self.error_codes[code]}\n'
        return error_string

    def validating_ips(self, ips_list: list[str]) -> dict[str, list[int]]:
        """
        Вызывает валидацию каждого ip-адреса из списка и возвращает словарь с результатами
        """
        results = {}
        for number, ip in enumerate(ips_list):
            results[f'№{number + 1}, {ip}'] = self.validating_ip(ip)
        return results

    def validating_ip(self, ip: str) -> list[int]:
        """
        Вызывает необходимые валидации ip-адреса и возвращает список с кодами результатов
        """
        validations = [self.validating_count_octets, self.validating_octets_values]
        result = []
        for validation_func in validations:
            validation_result = validation_func(ip)
            if validation_result:
                result.append(validation_result)
        return result

    def validating_count_octets(self, ip: str) -> int:
        """
        Проверяет количество октетов в ip-адресе
        """
        if len(ip.split('.')) == 4:
            return 0
        return 1

    def validating_octets_values(self, ip: str) -> int:
        """
        Проверяет корректность значений в октетах
        """
        octets_values = map(int, ip.split('.'))
        try:
            for value in octets_values:
                if not -1 < value < 256:
                    return 2
        except ValueError:
            return 2
        return 0
