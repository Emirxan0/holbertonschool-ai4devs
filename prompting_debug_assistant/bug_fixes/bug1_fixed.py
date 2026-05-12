"""
Bug 1 - bug1_fixed.py
Fix: Changed items[n:] to items[-n:] to correctly return the last n items.
"""

def last_n_items(items, n):
    """Return the last n items of a list."""
    if n == 0:
        return []
    return items[-n:]

if __name__ == "__main__":
    data = [10, 20, 30, 40, 50]
    assert last_n_items(data, 2) == [40, 50]
    assert last_n_items(data, 5) == [10,20,30,40,50]
    assert last_n_items(data, 0) == []
    assert last_n_items(data, 1) == [50]
    print("All tests passed!")
    print(last_n_items(data, 2))
    print(last_n_items(data, 5))
