
data = []

_file = open('day_1.txt', 'r') 
lines = _file.readlines()

for line in lines:
    stripped = int(line.strip())
    data.append(stripped)

def find_two_elements_from_sum(_list: list, _sum: int) -> list:
    result = []
    mirrors = {}

    for value in _list:
        mirror = _sum - value
        mirrors[value] = mirror
        if mirrors.get(mirror) is not None:
            result = [value, mirror]
            break

    return result

def find_three_elements_from_sum(_list: list, _sum: int) -> list:
    result = None

    for index_a, a in enumerate(_list):
        if result is not None:
            break
        
        for index_b, b in enumerate(_list):
            if result is not None:
                break
            if index_b == index_a:
                continue

            for index_c, c in enumerate(_list):
                if index_c == index_b or index_c == index_a:
                    continue

                if (a + b + c) == _sum:
                    result = [a, b, c]
                    break

    return result

def multiply_elements(_list: list) -> int:
    result = None

    for num in _list:
        if result is None:
            result = num
        else:
            result *= num

    return result
