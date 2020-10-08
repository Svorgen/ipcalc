import pytest
from net_calc_classes import CalcSubnetIpv4
from tests.write_ips import write_ips


@pytest.mark.parametrize(
    ('ips_list', 'result'),
    [
        (['192.168.1.2', '192.168.1.3', '192.168.1.5'], '192.168.1.0/29'),
        (['192.168.1.2', '192.168.2.1'], '192.168.0.0/23'),
        (['192.169.1.2', '192.168.2.1', '192.168.1.2'], '192.168.0.0/15'),
        (['0.169.2.1', '1.168.1.2'], '0.0.0.0/7'),
        (['0.0.0.0', '0.0.0.0'], '0.0.0.0/32'),

    ]
)
def test_correct_ips(ips_list, result):
    write_ips(ips_list)
    assert str(CalcSubnetIpv4().run('tests/test_ips.txt')[1]) == result


@pytest.mark.parametrize(
    ('ips_list', 'result'),
    [
        (['192.168.1.fds'], [[2]]),
        (['168.1.1'], [[1]]),
        (['256.168.1.1'], [[2]]),
        (['256.168.fds'], [[1, 2]]),
        ([], [[3]]),
    ]
)
def test_not_correct_ips(ips_list, result):
    write_ips(ips_list)
    assert list(CalcSubnetIpv4().run('tests/test_ips.txt')[1].values()) == result
