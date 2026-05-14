def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

if __name__ == "__main__":
    print(calculate_average([]))
    print(calculate_average([10, 20, 30, 40, 50]))
