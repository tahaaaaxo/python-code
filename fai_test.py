# single_file_example.py

public_variable = 0


def increment_variable():
    global public_variable
    public_variable += 1


def double_variable():
    global public_variable
    public_variable *= 2


# Test the functions
print(public_variable)  # Output: 0

increment_variable()
print(public_variable)  # Output: 1

double_variable()
print(public_variable)  # Output: 2
