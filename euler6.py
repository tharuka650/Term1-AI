sum_of_squares = 0
sum_numbers = 0
for i in range(1, 101):
    sum_of_squares += i * i
    sum_numbers += i
square_of_sum = sum_numbers * sum_numbers
difference = square_of_sum - sum_of_squares
print(difference)
