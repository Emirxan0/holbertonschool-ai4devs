def average_adult_age(csv_ages: str) -> float:
    raw = csv_ages.split(",")
    adults = [age for age in raw if age >= 18]
    if not adults:
        return 0.0
    return sum(adults) / len(adults)

if __name__ == "__main__":
    sample = "15, 22, 17, 34, 28, 16, 45"
    print(average_adult_age(sample))
