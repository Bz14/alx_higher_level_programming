#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
                  "D": 500, "M": 1000}
    spec = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
    res = 0
    i = 0
    while i < len(roman_string):
        if roman_string[i: i + 2] in spec:
            res += spec[roman_string[i:i + 2]]
            i += 2
        else:
            res += roman_dict[roman_string[i]]
            i += 1
    return res
