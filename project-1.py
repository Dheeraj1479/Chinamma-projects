print("Welcome to the temperature conversion!")
print("Type 'c' to convert from fahrenheit to celsius and 'f' to convert from celsius to fahrenheit")
choice = input()

if choice == 'c':
    print("Enter the number that you want to convert to celsius")
    num1 = int(input())
    celsius = ((num1 - 32) / 1.8, 2)
    print(f"Your temperature from fahrenheit to celsius is: {celsius}")
else:
    print("Enter the number that you want to convert to fahrenheit: ")
    num2 = int(input())
    fahrenheit = ((num2 * 1.8) + 32)
    print(f"Your temperature from celsius to fahrenheit is: {fahrenheit}")


