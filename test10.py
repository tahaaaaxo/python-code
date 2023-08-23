def print_formatted(number):
    width = len(bin(number)[2:])  # Width for formatting

    for i in range(1, number + 1):
        decimal_value = str(i).rjust(width)  # Decimal value
        octal_value = oct(i)[2:].rjust(width)  # Octal value
        hexadecimal_value = hex(i)[2:].upper().rjust(
            width)  # Hexadecimal value
        binary_value = bin(i)[2:].rjust(width)  # Binary value

        print(f"{decimal_value} {octal_value} {hexadecimal_value} {binary_value}")


if __name__ == '__main__':
    n = int(input("Enter a number: "))
    print_formatted(n)
