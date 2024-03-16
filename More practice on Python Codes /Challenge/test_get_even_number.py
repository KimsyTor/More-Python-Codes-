# BEGIN: xg7d5f8h3jw1
from get_even_numbers import get_even_numbers


def test_get_even_numbers():
    assert get_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [
        2, 4, 6, 8, 10]
    assert get_even_numbers([2, -10, 6, 80, -3, 4, 10]
                            ) == [2, -10, 6, 80, 4, 10]
    assert get_even_numbers([1, 3, 5, 7, 9]) == []
    assert get_even_numbers([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [
        0, 2, 4, 6, 8, 10]
    assert get_even_numbers([]) == []


test_get_even_numbers()
# END: xg7d5f8h3jw1
