
s = "MXC"

conversion_dict = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000,
    }

def convert_to_digit(s, conversion):
    i = 0
    number = 0
    while i < len(s):
        if i + 1 < len(s) and s[i:i+2] in conversion:
            number += conversion[s[i:i+2]]
            i += 2
        else:
            number += conversion[s[i]]
            i += 1
    return number



print(convert_to_digit(s, conversion_dict))