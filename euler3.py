n = 600851475143
factor = 2
while factor * factor <= n:
    if n % factor == 0:
        n //= factor  
    else:
        factor += 1  
print(n) 
