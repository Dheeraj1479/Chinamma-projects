#Find the remainder and quotient of a given number

print("Enter two numbers to find remainder or quotient")
num1 = float(input())
num2 = float(input())

print("Please enter 1 to find the remainder for the two numbers or enter 2 to find the quotient for the two numbers")
choice = int(input())

if choice == 1:
    print(f"The remainder is", {num1 % num2})
elif choice == 2:
    print(f"The quotient is", {num1 // num2})

