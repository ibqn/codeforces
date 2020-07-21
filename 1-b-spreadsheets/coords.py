import string

n = int(input())

coordinates = [input() for _ in range(n)]
base = len(string.ascii_uppercase)


def to_rx_cy(col, row):
    col_value = 0
    for l in col:
        col_value = col_value * base + 1 + string.ascii_uppercase.index(l)
    
    return f"R{row}C{col_value}"


def to_letters_num(col, row):
    letters = ''
    while col > 0:
        col, idx = divmod(col - 1, base)

        letters = string.ascii_uppercase[idx] + letters

    return f"{letters}{row}"


def get_format(value):
    digits = [i for i, c in enumerate(value) if c.isdigit()]
    idx = digits[0]

    is_letters_num = value[idx:].isdigit()

    if is_letters_num:
        row = int(value[idx:])
        col = value[:idx]
    else:
        idx = value.index("C")
        row = int(value[1:idx])
        col = int(value[idx + 1:])

    return (is_letters_num, row, col)


for c in coordinates:
    is_letters_num, row, col = get_format(c)
    # print("value", c, is_letters_num, row, col)
    result = to_letters_num(col, row) if not is_letters_num else to_rx_cy(col, row)
    print(result)