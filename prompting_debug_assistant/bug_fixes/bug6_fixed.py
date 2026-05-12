"""
Bug 6 - bug6_fixed.py
Fixes: 1) = -> == in base case  2) fib(n-1)+fib(n-1) -> fib(n-1)+fib(n-2)
"""

def fib(n, cache={}):
    if n == 0 or n == 1:
        return n
    if n in cache:
        return cache[n]
    result = fib(n - 1) + fib(n - 2)
    cache[n] = result
    return result

if __name__ == "__main__":
    expected = [0, 1, 1, 2, 3, 5, 8, 13]
    for i in range(8):
        assert fib(i) == expected[i], f"fib({i}) failed"
        print(f"fib({i}) = {fib(i)} ✅")
    print("All tests passed!")
