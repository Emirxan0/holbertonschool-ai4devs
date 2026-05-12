## Bug 1 – bug1.py
**Intended Behavior**: Return the last n items of a list.
**Issue Type**: Off-by-one error.
**Notes**: The function uses `items[n:]` instead of `items[-n:]`, returning elements from the front instead of the end. Fails completely when n == len(items), returning an empty list instead of the full list.

## Bug 2 – bug2.js
**Intended Behavior**: Apply a tiered discount to a shopping cart total: purchases >= $200 get 20% off, >= $100 get 10% off, otherwise no discount.
**Issue Type**: Logical error (wrong condition order).
**Notes**: Conditions are evaluated smallest-first. Any total >= 200 also satisfies >= 100, so the 20% branch is dead/unreachable code. Customers spending $200+ only ever receive 10% off.

## Bug 3 – bug3.py
**Intended Behavior**: Parse a comma-separated string of ages, filter out anyone under 18, and return the average age of the remaining adults as a float.
**Issue Type**: Runtime exception (TypeError).
**Notes**: `str.split()` returns a list of strings. Comparing a string to an integer with `>=` raises TypeError in Python 3. A missing `int()` cast causes both the filter and the sum to fail.

## Bug 4 – bug4.c
**Intended Behavior**: Reverse a C string in-place using two pointers starting from both ends, swapping characters until the pointers meet in the middle. Must handle empty strings without crashing.
**Issue Type**: Off-by-one error + undefined behaviour on empty string.
**Notes**: `strlen()` returns `size_t` (unsigned). For an empty string, `strlen(str) - 1` wraps around to SIZE_MAX due to unsigned underflow, causing an out-of-bounds write, crash, or infinite loop.

## Bug 5 – bug5.js
**Intended Behavior**: Fetch a user record from a REST API by numeric ID, extract and return the user's email address. Return null when the user does not exist.
**Issue Type**: Runtime exception (unhandled Promise rejection).
**Notes**: Three bugs: (1) missing `await` on `response.json()` so `data` is a Promise and `data.email` is always undefined; (2) no try/catch so network errors cause unhandled rejections; (3) no HTTP status check so missing users return undefined instead of null.

## Bug 6 – bug6.py
**Intended Behavior**: Compute the nth Fibonacci number recursively with dictionary-based memoization. fib(0)=0, fib(1)=1, fib(n)=fib(n-1)+fib(n-2).
**Issue Type**: Syntax error + logical error.
**Notes**: Two bugs: (1) base case uses `=` (assignment) instead of `==` (comparison), causing a SyntaxError at parse time; (2) recursive step calls `fib(n-1) + fib(n-1)` instead of `fib(n-1) + fib(n-2)`, producing powers of 2 instead of Fibonacci numbers.
