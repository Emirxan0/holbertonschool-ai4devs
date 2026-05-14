#!/usr/bin/env python3
"""
Bug 3 Fix: Logic error in conditional statement
Original bug: Wrong boolean operator used (or instead of and).
Fix: Replaced or with and so both conditions must be true.
"""


def classify_score(score):
    if score == 100:
        return "Perfect"
    elif score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "F"


def is_eligible(age, has_id):
    if age >= 18 and has_id:
        return True
    return False


if __name__ == "__main__":
    print(classify_score(100))
    print(classify_score(85))
    print(classify_score(50))
    print(is_eligible(20, True))
    print(is_eligible(16, True))
    print(is_eligible(20, False))
