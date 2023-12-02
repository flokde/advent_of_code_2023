from typing import List

from numpy import loadtxt

digits_str_to_int = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def concat_first_and_last_digit(input_array: List[str]) -> int:
    numbers = []
    for string in input_array:
        only_digits = [x for x in string if x.isdigit()]
        numbers.append(int(only_digits[0] + only_digits[-1]))

    return sum(numbers)


def concat_including_strings(input_array: List[str]) -> int:
    numbers = []
    for string in input_array:
        only_digits = []
        for i, value in enumerate(string):
            if value.isdigit():
                only_digits.append(value)
            for digit in digits_str_to_int.keys():
                if string[i:].startswith(digit):
                    only_digits.append(digits_str_to_int[digit])
        numbers.append(int(only_digits[0] + only_digits[-1]))

    return sum(numbers)


if __name__ == "__main__":
    with open("input", "r") as file:
        input_array = file.read().splitlines()

    result_1 = concat_first_and_last_digit(input_array)
    print(result_1)

    result_2 = concat_including_strings(input_array)
    print(result_2)
