data = []

_file = open('day_2.txt', 'r') 
lines = _file.readlines()

for line in lines:
    data.append(line.strip())

def is_password_correct(_line: str) -> bool:
    _range, _char, _password = _line.split()
    
    _range = [*map(lambda el: int(el), _range.split('-'))]
    _char = _char.replace(':', '')
    _password = _password.strip()

    password_as_list = [char for char in _password]

    count = 0
    for character in password_as_list:
        if character == _char:
            count += 1

    return count >= _range[0] and count <= _range[1]

def calculate_correct_passwords(_data:list) -> int:
    count = 0 

    for line in _data:
        if is_password_correct(line):
            count += 1
    
    return count

print(calculate_correct_passwords(_data=data))