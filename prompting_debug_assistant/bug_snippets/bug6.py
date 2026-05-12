def fib(n, cache={}):
    if n = 0 or n = 1:
        return n
    if n in cache:
        return cache[n]
    result = fib(n - 1) + fib(n - 1)
    cache[n] = result
    return result

if __name__ == "__main__":
    for i in range(8):
        print(f"fib({i}) = {fib(i)}")
