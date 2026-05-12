"""
Bug 1 - bug1.py
Intended Behavior: Return the last n items from a list.
Issue Type: Off-by-one error
"""

def last_n_items(items, n):
    """Return the last n items of a list."""
    if n == 0:
        return []
    return items[n:]

if __name__ == "__main__":
    data = [10, 20, 30, 40, 50]
    print(last_n_items(data, 2))
    print(last_n_items(data, 5))
    print(last_n_items(data, 0))
    print(last_n_items(data, 1))
