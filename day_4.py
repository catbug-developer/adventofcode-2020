import typing
import functools
import re

data = []

_file = open("day_4.txt", "r")
lines = _file.readlines()

credentials = []

for line in lines:
    if line != "\n":
        _line = line.strip()
        credentials.append(_line.split())
        continue
    else:
        credential_line = functools.reduce(
            lambda _el, _next_el: [*_el, *_next_el], credentials
        )
        credentials_dict = {}

        for cred in credential_line:
            _cred, _cred_value = cred.split(":")
            credentials_dict[_cred] = _cred_value

        data.append(credentials_dict)
        credentials = []

required_fields = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
]

iscolor = re.compile(r"^#[0-9a-f]{6}$")
ispid = re.compile(r"^\d{9}$")
colors_dict = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}


def validate_hgt(hgt: str) -> bool:
    return (hgt.endswith("cm") and 150 <= int(hgt[:-2]) <= 193) or (
        hgt.endswith("in") and 59 <= int(hgt[:-2]) <= 76
    )


def count_not_strict(_data: list, _required_fields: list) -> int:
    count = 0

    for credentials_dict in _data:
        is_valid = True

        for valid_north_pole_field in _required_fields:
            if valid_north_pole_field in credentials_dict:
                continue
            else:
                is_valid = False
                break

        if is_valid:
            count += 1

    return count


def count_strict(_data: list, _colors_dict: dict) -> int:
    count = 0

    for credentials_dict in _data:
        byr = credentials_dict.get("byr")
        iyr = credentials_dict.get("iyr")
        eyr = credentials_dict.get("eyr")
        hgt = credentials_dict.get("hgt")
        hcl = credentials_dict.get("hcl")
        ecl = credentials_dict.get("ecl")
        pid = credentials_dict.get("pid")

        if (
            byr
            and 1920 <= int(byr) <= 2002
            and iyr
            and 2010 <= int(iyr) <= 2020
            and eyr
            and 2020 <= int(eyr) <= 2030
            and hgt
            and validate_hgt(hgt)
            and hcl
            and iscolor.match(hcl)
            and ecl
            and ecl in colors_dict
            and pid
            and ispid.match(pid)
        ):
            count += 1

    return count


print(count_not_strict(_data=data, _required_fields=required_fields))
print(count_strict(_data=data, _colors_dict=colors_dict))
