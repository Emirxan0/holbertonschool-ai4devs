## Bug 1 – bug1.py
**Intended Behavior**: Return the last n items of a list.
**Issue Type**: Off-by-one error.
**Notes**: The function uses items[n:] instead of items[-n:], returning wrong elements. Fails completely when n == len(items).

## Bug 2 – bug2.js
**Intended Behavior**: Apply a tiered discount (>=200 → 20%, >=100 → 10%) to a cart total.
**Issue Type**: Logical error.
**Notes**: Conditions are checked smallest-first, making the 20% branch dead/unreachable code.

## Bug 3 – bug3.py
**Intended Behavior**: Parse a CSV string of ages, filter adults (>=18), return their average.
**Issue Type**: Runtime exception (TypeError).
**Notes**: str.split() returns strings; comparing str >= int raises TypeError. Missing int() cast.

## Bug 4 – bug4.c
**Intended Behavior**: Reverse a C string in-place using two pointers.
**Issue Type**: Off-by-one error + undefined behaviour.
**Notes**: strlen returns size_t (unsigned); strlen("")-1 wraps to SIZE_MAX causing crash or infinite loop.

## Bug 5 – bug5.js
**Intended Behavior**: Fetch a user by ID from an API and return their email, or null if not found.
**Issue Type**: Runtime exception (unhandled Promise rejection).
**Notes**: Missing await on response.json(), no try/catch, no HTTP status check.

## Bug 6 – bug6.py
**Intended Behavior**: Compute the nth Fibonacci number recursively with memoization.
**Issue Type**: Syntax error + logical error.
**Notes**: Uses = instead of == in base case (SyntaxError). Second recursive call uses n-1 instead of n-2.
