lookup = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'
}


final = ''
for i in range(1, 1001):
    thousands = (int(i) // 1000) % 10
    hundreds = (int(i) // 100) % 10
    tens = (int(i) // 10) % 10
    ones = int(i) % 10

    if thousands:
        final += 'onethousand'
    if hundreds:
        final += lookup[hundreds] + 'hundred'
    if hundreds and (tens or ones):
        final += 'and'
    if tens == 1 and ones:
        final += lookup[tens*10 + ones]
    else:
        if tens:
            final += lookup[tens * 10]
        if ones:
            final += lookup[ones]

print(len(final))
