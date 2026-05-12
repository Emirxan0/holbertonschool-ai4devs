## Bug 1 – bug1.py

**Intended Behavior**: Return the last n items of a list. For example, given [1, 2, 3, 4, 5] and n=2, the function should return [4, 5].
**Issue Type**: Off-by-one error.
**Notes**: The function uses items[n:] instead of items[-n:], slicing from the front instead of the end. When n equals the length of the list, the function returns an empty list instead of the full list.

## Bug 2 – bug2.js

**Intended Behavior**: Apply a tiered discount to a shopping cart total. Purchases of $200 or more receive 20% off, purchases of $100 or more receive 10% off, and purchases below $100 receive no discount.
**Issue Type**: Logical error (wrong condition order).
**Notes**: The if-else chain checks the smaller threshold first. Since any total above $200 also satisfies the $100 condition, the 20% discount branch is unreachable dead code. Customers spending $200 or more only receive 10% off instead of the correct 20%.

## Bug 3 – bug3.py

**Intended Behavior**: Parse a comma-separated string of ages, filter out anyone under 18, and return the average age of the remaining adults as a float value.
**Issue Type**: Runtime exception (TypeError).
**Notes**: The str.split() method returns a list of strings not integers. Comparing a string to an integer using >= raises a TypeError in Python 3. The missing int() cast causes both the filter comparison and the sum calculation to fail immediately at runtime.

## Bug 4 – bug4.c

**Intended Behavior**: Reverse a C string in-place using two pointers starting from both ends, swapping characters until the pointers meet in the middle. The function should handle empty strings gracefully without crashing or looping indefinitely.
**Issue Type**: Off-by-one error and undefined behaviour on empty string.
**Notes**: The strlen() function returns size_t which is an unsigned type. For an empty string, strlen(str) minus 1 wraps around to SIZE_MAX due to unsigned integer underflow. This causes an out-of-bounds memory write, a segmentation fault, or an infinite loop depending on the platform.

## Bug 5 – bug5.js

**Intended Behavior**: Fetch a user record from a REST API using a numeric ID, extract the email field from the JSON response, and return it as a string. If the user does not exist or the request fails, the function should return null instead of throwing an unhandled error.
**Issue Type**: Runtime exception (unhandled Promise rejection, missing await, no error handling).
**Notes**: There are three distinct bugs. First, response.json() is an async method called without await, so data holds a Promise object rather than parsed JSON, making data.email always undefined. Second, there is no try-catch block wrapping the fetch call, so any network failure produces an unhandled Promise rejection that crashes the caller. Third, there is no check on response.ok or response.status, so a 404 response returns undefined instead of the documented null value.

## Bug 6 – bug6.py

**Intended Behavior**: Compute the nth Fibonacci number recursively using dictionary-based memoization to avoid redundant computation. The sequence is defined as fib(0)=0, fib(1)=1, and fib(n)=fib(n-1)+fib(n-2) for all n greater than 1.
**Issue Type**: Syntax error and logical error.
**Notes**: There are two independent bugs. First, the base case condition uses a single equals sign for assignment instead of double equals for equality comparison, which raises a SyntaxError at parse time and prevents the module from loading. Second, after fixing the SyntaxError, the recursive step calls fib(n-1) twice instead of fib(n-1) plus fib(n-2), producing the sequence 0, 1, 2, 4, 8, 16 instead of the correct Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13.
