import what_is_year_now as wiyn
from unittest.mock import patch
import io
import pytest


def test_invalid_input():
    date = '{"currentDateTime": "2001.01.01"}'
    with patch('urllib.request.urlopen') as mock:
        mock.return_value.__enter__.return_value = io.StringIO(date)
        with pytest.raises(ValueError):
            wiyn.what_is_year_now()


@pytest.mark.parametrize('date, target_date', [
    ('{"currentDateTime": "01.01.2001"}', 2001),
    ('{"currentDateTime": "2022-02-02"}', 2022)
])
def test_basic_scenario(date, target_date):
    with patch('urllib.request.urlopen') as mock:
        mock.return_value.__enter__.return_value = io.StringIO(date)
        date = wiyn.what_is_year_now()
        mock.assert_called_once()
    assert date == target_date
