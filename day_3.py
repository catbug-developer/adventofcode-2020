import typing
import functools

data = []

_file = open("day_3.txt", "r")
lines = _file.readlines()

for line in lines:
    data.append(line.strip())


def is_on_tree(_line: str, _position: int, _tree_char = "#") -> bool:
    chars = [char for char in _line]
    return chars[_position] == tree_char


def calculate_trees(
    _data: list,
    _fn: typing.Callable[[str, int], bool],
    _rule: dict,
    _line_len: int = 31,
) -> str:
    _lines_count = len(_data)

    _trees_count = 0
    _pointer_position = 0
    _pointer_line = 0

    while _pointer_line < _lines_count:
        if _fn(_line=_data[_pointer_line], _position=_pointer_position):
            _trees_count += 1

        _pointer_position += _rule["right"]
        _pointer_line += _rule["down"]

        if _pointer_position >= _line_len:
            _pointer_position = _pointer_position - _line_len

    return _trees_count


rules = [
    {"right": 1, "down": 1},
    {"right": 3, "down": 1},
    {"right": 5, "down": 1},
    {"right": 7, "down": 1},
    {"right": 1, "down": 2},
]

count_list = [
    calculate_trees(_data=data, _fn=is_on_tree, _rule=_rule) for _rule in rules
]

multiplication = functools.reduce(lambda _curr, _next: _curr * _next, count_list)

print(multiplication)
