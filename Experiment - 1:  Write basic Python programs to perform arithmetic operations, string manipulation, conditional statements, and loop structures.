"""
Experiment 01: Basic Python Programs
-----------------------------------
This script demonstrates:
1. Arithmetic Operations
2. String Manipulation
3. Conditional Statements
4. Loop Structures
(with user input)
"""

# -------------------------------
# 1. Arithmetic Operations
# -------------------------------
def arithmetic_operations(a, b):
    print("\nArithmetic Operations:")
    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    print(f"Division: {a} / {b} = {a / b:.2f}")
    print(f"Modulus: {a} % {b} = {a % b}")
    print(f"Exponentiation: {a} ** {b} = {a ** b}")
    print("-" * 40)


# -------------------------------
# 2. String Manipulation
# -------------------------------
def string_manipulation(text):
    print("\nString Manipulation:")
    print(f"Original text: {text}")
    print(f"Uppercase: {text.upper()}")
    print(f"Lowercase: {text.lower()}")
    print(f"Reversed: {text[::-1]}")
    print(f"Sliced (first 5 chars): {text[:5]}")
    print(f"Replaced spaces with '-': {text.replace(' ', '-')}")
    print("-" * 40)


# -------------------------------
# 3. Conditional Statements
# -------------------------------
def check_number(num):
    print("\nConditional Statements:")
    if num > 0:
        print(f"{num} is Positive")
    elif num < 0:
        print(f"{num} is Negative")
    else:
        print("The number is Zero")
    print("-" * 40)


# -------------------------------
# 4. Loop Structures
# -------------------------------
def loop_examples(n):
    print("\nLoop Structures:")

    print("For loop (1 to n):")
    for i in range(1, n + 1):
        print(i, end=" ")
    print()

    print("While loop (countdown from n):")
    count = n
    while count > 0:
        print(count, end=" ")
        count -= 1
    print()

    print("Nested loop (n x n matrix):")
    for i in range(n):
        for j in range(n):
            print(f"({i},{j})", end=" ")
        print()
    print("-" * 40)


# -------------------------------
# Main function
# -------------------------------
if __name__ == "__main__":
    print("=== Experiment 01: Basic Python Programs ===")

    # Take user input for arithmetic operations
    a = int(input("\nEnter first number: "))
    b = int(input("Enter second number: "))
    arithmetic_operations(a, b)

    # Take user input for string manipulation
    text = input("\nEnter a string: ")
    string_manipulation(text)

    # Take user input for conditional statement
    num = int(input("\nEnter a number to check (positive/negative/zero): "))
    check_number(num)

    # Take user input for loops
    n = int(input("\nEnter a number for loop demonstrations: "))
    loop_examples(n)

    print("\n=== Program Finished ===")
