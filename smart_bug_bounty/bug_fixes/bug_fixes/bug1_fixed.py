#!/usr/bin/env python3
"""
Bug 1 Fix: Off-by-one error in list slicing/iteration
Original bug: Loop used range(len(items)) causing index out of range
              or slice missed the last element.
Fix: Corrected the range/slice to include all elements properly.
"""


def get_last_element(items):
    """Returns the last element of a list."""
    if not items:
        return None
    return items[len(items) - 1]


def sum_all_elements(items):
    """Returns sum of all elements."""
    total = 0
    for i in range(len(items)):
        total += items[i]
    return total


def get_slice(items):
    """Returns all elements as a list."""
    return items[0:len(items)]


if __name__ == "__main__":
    sample = [10, 20, 30, 40, 50]
    print("Last element:", get_last_element(sample))
    print("Sum:", sum_all_elements(sample))
    print("Slice:", get_slice(sample))
