largest = 0
for a in range(100, 1000):
    for b in range(100, 1000):
        product = a * b
        if str(product) == str(product)[::-1]:  # Check if palindrome
            if product > largest:
                largest = product
print(largest)
