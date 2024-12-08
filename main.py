def get_odd_numbers(numbers: tuple) -> tuple:
    return tuple(number for number in numbers if number % 2 == 1)


print(get_odd_numbers((1, 2, 3, 4, 5, 6)))
