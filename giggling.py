import random
import string

# Function to generate a random string of specified length
def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Function to create a list of random integers
def generate_random_integers(size=5, start=1, end=100):
    return [random.randint(start, end) for _ in range(size)]

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Generate random string and list of integers
random_string = generate_random_string()
random_integers = generate_random_integers()

# Print random string and integers
print(f"Random String: {random_string}")
print(f"Random Integers: {random_integers}")

# Find prime numbers from the generated random integers
primes = [num for num in random_integers if is_prime(num)]

# Check if there are any primes
if primes:
    print(f"Prime Numbers Found: {primes}")
else:
    print("No prime numbers found in the random integers.")

# Loop through numbers and print if it's even or odd
for num in random_integers:
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")

# Create a dictionary with random strings as keys and random integers as values
random_dict = {generate_random_string(5): random.randint(1, 10) for _ in range(3)}

# Print the generated dictionary
print(f"Random Dictionary: {random_dict}")

# Function to calculate the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Calculate and print factorial of a random number
random_num = random.randint(1, 10)
print(f"The factorial of {random_num} is {factorial(random_num)}.")
