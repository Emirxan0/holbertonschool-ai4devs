## Bug 1 – bug1.py

**Intended Behavior**: The function should accept a list and an integer n, then return a new list containing only the last n elements, preserving their original order.
**Issue Type**: Off-by-one error.
**Notes**: Using items[n:] slices from index n to the end, returning elements from the front. The correct slice is items[-n:] which counts from the end. When n equals the list length, items[n:] returns an empty list instead of all elements.

## Bug 2 – bug2.js

**Intended Behavior**: The function should calculate a final price after applying the correct discount tier based on the total amount spent.
**Issue Type**: Logical error (wrong condition order).
**Notes**: The >= 100 condition is checked before >= 200. Because any value satisfying >= 200 also satisfies >= 100, the larger discount branch is never reached. The conditions must be ordered from largest to smallest to work correctly.

## Bug 3 – bug3.py

**Intended Behavior**: The function should convert a CSV string into a list of integer ages, keep only those aged 18 or above, and return the arithmetic mean of the filtered values as a float.
**Issue Type**: Runtime exception (TypeError).
**Notes**: The split method produces strings, not integers. The comparison age >= 18 fails with TypeError because Python 3 cannot compare str and int. Adding int() conversion around each element before comparison and summation fixes both issues.

## Bug 4 – bug4.c

**Intended Behavior**: The function should swap characters from both ends of the string moving inward until all characters are reversed. It must also handle an empty string input without crashing or entering an infinite loop.
**Issue Type**: Off-by-one error and undefined behaviour on empty string.
**Notes**: strlen returns an unsigned size_t value. Subtracting 1 from 0 produces SIZE_MAX due to unsigned underflow, not -1. This makes the while condition true with an enormous right index, causing out-of-bounds writes. A length check before the loop is required.

## Bug 5 – bug5.js

**Intended Behavior**: The function should send an HTTP request to a user endpoint, parse the JSON response body, and return the email field as a string. When the user ID does not exist, it should return null. When a network error occurs, it should fail gracefully without an unhandled rejection.
**Issue Type**: Runtime exception (missing await, unhandled Promise rejection, missing null return).
**Notes**: response.json() returns a Promise and must be awaited before accessing properties. Without await, data.email is always undefined. Additionally, the function has no try-catch for network failures and no response.ok check to return null for missing users.

## Bug 6 – bug6.py

**Intended Behavior**: The function should return the nth number in the Fibonacci sequence, where each value is the sum of the two values before it. A shared cache dictionary should store previously computed values to avoid recalculating them on repeated calls.
**Issue Type**: Syntax error and logical error.
**Notes**: The base case uses = instead of == which is a SyntaxError that prevents the file from being parsed at all. After correcting the syntax, the recursive call uses fib(n-1) + fib(n-1) instead of fib(n-1) + fib(n-2), doubling rather than summing consecutive terms and producing powers of 2.
