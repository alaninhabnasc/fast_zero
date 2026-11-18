from fast_zero.app import read_root


def test_read_root():
    assert read_root() == {'message': 'Olá Mundo!'}