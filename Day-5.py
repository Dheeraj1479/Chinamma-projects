#Print multiplication table for a given number

print("Enter a number to find its multiplication table")
num = int(input())

for table in range(1,11):
    print(f"{num} x {table} = {num*table}")