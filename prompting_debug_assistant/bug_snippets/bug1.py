def last_n_items(items, n):
    if n == 0:
        return []
    return items[n:]

if __name__ == "__main__":
    data = [10, 20, 30, 40, 50]
    print(last_n_items(data, 2))
    print(last_n_items(data, 5))
    print(last_n_items(data, 0))
    print(last_n_items(data, 1))
