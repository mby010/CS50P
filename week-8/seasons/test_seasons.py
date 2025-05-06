from seasons import get_date
from datetime import date

def test_get_date():
    assert get_date('1995-01-13') == date(1995, 1, 13)
