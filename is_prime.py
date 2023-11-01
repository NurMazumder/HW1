def is_prime(n):
    if n == 3:
        return True
    else:
        divisor = 2
        while divisor * divisor <= n:
            if n % divisor == 0:
                return False
            divisor += 1
        return True

# Test the function for numbers between 3 and 100
for number in range(3, 101):
    if is_prime(number):
        print(f"{number} is prime.")
    else:
        print(f"{number} is not prime.")
