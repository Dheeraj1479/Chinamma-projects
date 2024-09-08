#Find odd and even numbers from 1 - 100 using for loop

def evennumbers():
    for num in range(1, 101):
        if num % 2 == 0:
            print(f"{num} is even")

def oddnumbers():
    for num in range(1, 101):
        if num % 2 != 0:
            print(f"{num} is odd")

choice = input("Enter 1 for even number and 2 for odd number")
if choice == "1":
    evennumbers()
else:
    oddnumbers()