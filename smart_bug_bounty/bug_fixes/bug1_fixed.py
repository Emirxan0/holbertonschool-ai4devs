def calculate_average(numbers):
    if not numbers: return 0
    total_sum = sum(numbers)
    return total_sum / len(numbers)

data_empty = []
data_with_values = [10, 20, 30, 40, 50]
data_with_one = [100]
print(f"Boş liste ortalaması: {calculate_average(data_empty)}")
print(f"Dolu liste ortalaması: {calculate_average(data_with_values)}")
print(f"Tek elemanlı liste ortalaması: {calculate_average(data_with_one)}")
