import pytest as pytest

import morse


@pytest.mark.parametrize('data, target', [
    ('... --- ...', 'SOS'),
    ('-- . --- .-- ', 'MEOW'),
    ('.-- - ..-. ..--..', 'WTF?')
])
def test_decode(data, target):
    assert morse.decode(data) == target


@pytest.mark.parametrize('data, target', [
    ('... --- ...', 'SOS'),
    ('... . -.-. --- -. -..', 'SECOND'),
    ('.-- - ..-. ..--..', 'WTF?')
])
def test_encode(data, target):
    assert morse.encode(target) == data
