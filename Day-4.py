#Find odd and even numbers from 1 to 100 using while loop

num = 1

while num <= 100:
    if num % 2 == 0:
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")

    num += 1
