#Find sum of even numbers and odd number from 1 to 100

even_sum = 0
odd_sum = 0

for num in range(1, 101):
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)