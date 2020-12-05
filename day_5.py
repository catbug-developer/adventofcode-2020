_file = open("day_5.txt", "r")
lines = _file.readlines()

data = [line.strip() for line in lines]

seat_ids = []

for line in data:
    row = line[:-3]
    column = line[-3:]

    row_translation = str.maketrans('FB', '01')
    col_translation = str.maketrans('LR', '01')

    row_translated = row.translate(row_translation)
    col_translated = column.translate(col_translation)

    _id = int(row_translated, 2) * 8 + int(col_translated, 2)

    seat_ids.append(_id)

max_seat_id = max(seat_ids)

print(max_seat_id)

for _id in seat_ids:
    if _id + 1 not in seat_ids and _id + 2 in seat_ids:
        print(_id + 1)