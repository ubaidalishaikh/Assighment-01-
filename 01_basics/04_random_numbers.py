import random

def print_random_numbers():
    for _ in range(10):
        number = random.randint(1, 100)
        print(number, end=" ")

# Run the function
if __name__ == "__main__":
    print_random_numbers()
