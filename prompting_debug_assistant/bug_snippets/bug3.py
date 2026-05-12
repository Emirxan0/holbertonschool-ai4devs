"""
Bug 3 - bug3.py
Intended Behavior: Read a list of user ages from a CSV-like string,
                   filter out anyone under 18, and return the average
                   age of the remaining adults as a float.
Issue Type: Runtime exception - TypeError due to missing type conversion.
Notes: str.split() returns strings. Comparing str >= int raises TypeError.
       Missing int() cast before comparison and arithmetic.
"""

def average_adult_age(csv_ages: str) -> float:
    """Parse ages from a comma-separated string and return
    the mean age of adults (age >= 18)."""
    raw = csv_ages.split(",")
    adults = [age for age in raw if age >= 18]
    if not adults:
        return 0.0
    return sum(adults) / len(adults)

if __name__ == "__main__":
    sample = "15, 22, 17, 34, 28, 16, 45"
    print(average_adult_age(sample))
