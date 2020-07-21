import string

n = int(input())

coordinates = [input() for _ in range(n)]
base = len(string.ascii_uppercase)


def to_rx_cy(col, row):
    col_value = 0
    for i, l in enumerate(col[::-1]):
        col_value += (1 + string.ascii_uppercase.index(l))*base**i
    
    return f"R{row}C{col_value}"


def to_letters_num(col, row):
    letters = []
    while col > 0:
        idx = int(col % base)
        if idx == 0:
            l = "Z"
            col -= 1
        else:
            l = string.ascii_uppercase[idx - 1]

        letters.append(l)
        # print(col, idx, l)
        col //= base 

    col_str = ''.join(letters[::-1])
    return f"{col_str}{row}"


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