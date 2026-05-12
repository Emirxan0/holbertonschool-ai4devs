"""
Bug 1 - bug1.py
Intended Behavior: Return the last n items from a list. For example,
                   last_n_items([1,2,3,4,5], 2) should return [4, 5].
Issue Type: Off-by-one error.
Notes: The function uses items[n:] instead of items[-n:], slicing from
       the front instead of the end. When n == len(items), items[n:]
       returns an empty list instead of the full list.
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
