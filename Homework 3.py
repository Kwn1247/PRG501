# Homework 3
# Haixiang Yu
# 2025/5/24

# Calculate average
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)


# Find max number
def find_max(numbers):
    if len(numbers) == 0:
        return None
    return max(numbers)


# Find min number
def find_min(numbers):
    if len(numbers) == 0:
        return None
    return min(numbers)

def main():
    uinput = input("Enter a list of numbers (separated by spaces): ")

    numbers = list(map(float, uinput.split()))

    avg = calculate_average(numbers)
    max = find_max(numbers)
    min = find_min(numbers)

    # Print the results
    print("Average:", avg)
    print("Maximum:", max)
    print("Minimum:", min)


# Run the main program
main()
