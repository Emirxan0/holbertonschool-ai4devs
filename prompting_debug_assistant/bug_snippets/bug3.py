"""
Bug 3 - bug3.py
Intended Behavior: Parse a CSV string of ages, filter adults (age >= 18),
                   and return their average age as a float.
Issue Type: Runtime exception - TypeError due to missing type conversion.
Notes: str.split() returns strings. Comparing str >= int raises TypeError.
       Missing int() cast before comparison and arithmetic.
"""

def average_adult_age(csv_ages: str) -> float:
    raw = csv_ages.split(",")
    adults = [age for age in raw if age >= 18]
    if not adults:
        return 0.0
    return sum(adults) / len(adults)

if __name__ == "__main__":
    sample = "15, 22, 17, 34, 28, 16, 45"
    print(average_adult_age(sample))
