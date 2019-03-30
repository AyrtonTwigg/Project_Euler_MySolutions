# Variable holding all the even Fibonacci numbers less than 4,000,000
even_fib_numbers = []

# Starting variables
first_num = 1
second_num = 0

# Compute Fibonacci numbers, add the even ones in to the list variable
while True:
    if first_num % 2 == 0:
        even_fib_numbers.append(first_num)

    next_num = first_num + second_num
    second_num = first_num
    first_num = next_num

    if first_num > 4000000:
        break

print(sum(even_fib_numbers))
