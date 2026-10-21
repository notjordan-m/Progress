def main():
    num1 = float(input("Enter the First number: "))
    num2 = float(input("Enter the second number: "))
    print(f"The sum of {num1} and {num2} is {add(num1, num2)}")
    print(f"The difference of {num1} and {num2} is {subtract(num1, num2)}")


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

main()

