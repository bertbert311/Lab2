import Lab2 as temp


def test_find_min_max():
    result = 0
    temp.find_min_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    if min == 1 and max == 10:
        result = 1
        assert (result == 1)


def test_calc_average():
    assert (5.5 == temp.calc_average([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


def test_calc_median_temperature():
    temp.calc_median_temperature([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    if  temp.calc_median_temperature([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5.5:
        result = 0
        assert (result ==  0)



