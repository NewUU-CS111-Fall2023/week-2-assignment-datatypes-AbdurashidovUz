import random

def generate_large_number():
    return random.randint(10**99, 10**100 - 1)

def divide_by_input(number):
    return large_number // number

number_A = int(input("Enter a number: "))

large_number = generate_large_number()

result = divide_by_input(number_A)

print("The result of dividing the 100-digit number", large_number, " by ", number_A, "is:", result)

