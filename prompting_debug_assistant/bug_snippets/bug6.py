"""
Bug 6 - bug6.py
Intended Behavior: Compute the nth Fibonacci number recursively with
                   dictionary-based memoization.
                   fib(0)=0, fib(1)=1, fib(n)=fib(n-1)+fib(n-2).
Issue Type: Syntax error + logical error.
Notes: Two bugs: (1) base case uses = instead of == causing SyntaxError;
       (2) recursive step calls fib(n-1)+fib(n-1) instead of fib(n-1)+fib(n-2),
       producing powers of 2 instead of Fibonacci numbers.
"""

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
