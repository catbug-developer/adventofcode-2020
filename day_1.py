
example_list = [1721, 979, 366, 299, 675, 145]

def find_two_elements_from_sum(_list: list, _sum: int) -> int:
    result = None
    mirrors = {}

    for value in _list:
        mirror = _sum - value
        mirrors[value] = mirror
        if mirrors.get(mirror) is not None:
            result = value * mirror
            break

    return result
    