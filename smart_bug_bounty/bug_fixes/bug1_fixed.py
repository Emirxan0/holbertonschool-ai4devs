def calculate_average(numbers):
    # Fix: Check for empty list to prevent ZeroDivisionError
    if not numbers:
        return 0

    # Fix: Use sum() instead of manual loop starting from wrong index
    total_sum = sum(numbers)
    return total_sum / len(numbers)

# Tests
data_empty = []
data_with_values = [10, 20, 30, 40, 50]
data_with_one = [100]
print(f"Empty list average: {calculate_average(data_empty)}")
print(f"Full list average: {calculate_average(data_with_values)}")
print(f"Single element average: {calculate_average(data_with_one)}")
