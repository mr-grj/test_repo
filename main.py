def get_odd_numbers(numbers: tuple) -> tuple:
    return tuple(number for number in numbers if number % 2 == 1)


def get_even_numbers(numbers: tuple) -> tuple:
    return tuple(number for number in numbers if number % 2 == 0)


def main():
    numbers = (1, 2, 3, 4, 5, 6)
    print(get_odd_numbers(numbers))
    print(get_even_numbers(numbers))


if __name__ == "__main__":
    main()
