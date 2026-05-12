"""
Bug 3 - bug3_fixed.py
Fix: Added int(age.strip()) to convert strings to integers before
     comparison and arithmetic.
"""

def average_adult_age(csv_ages: str) -> float:
    ages = [int(age.strip()) for age in csv_ages.split(",")]
    adults = [age for age in ages if age >= 18]
    if not adults:
        return 0.0
    return sum(adults) / len(adults)

if __name__ == "__main__":
    sample = "15, 22, 17, 34, 28, 16, 45"
    assert average_adult_age(sample) == 32.25
    assert average_adult_age("10, 12, 15") == 0.0
    assert average_adult_age("18, 18, 18") == 18.0
    print("All tests passed!")
    print(average_adult_age(sample))

# Additional test cases
assert average_adult_age("18") == 18.0
assert average_adult_age("0, 1, 2") == 0.0
assert average_adult_age("20, 25, 30") == 25.0
print("Extended tests passed!")
