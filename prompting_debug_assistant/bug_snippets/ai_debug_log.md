## Bug 1 - bug1.py
**AI Diagnosis**: The function iterates beyond the list bounds due to `range(len(readings))`. It also incorrectly filters for negative values instead of positive ones and fails when the filtered list is empty (ZeroDivisionError).
**Suggested Fix**: Change the filter condition to `readings[i] >= 0`, adjust the loop range to `len(valid_readings)`, and add a check for an empty list before division.
**Alternative Fixes Tested**: Using `sum(valid_readings) / len(valid_readings)` for a more Pythonic approach.
**Result**: Fix works as expected.

## Bug 2 - bug2.js
**AI Diagnosis**: There is a syntax error (missing parenthesis in `if` statement), a reference error (`minLenght` instead of `minLength`), and a logic error using assignment `=` instead of comparison `===` for the role check.
**Suggested Fix**: Fix the syntax by adding `)`, correct the typo in the variable name, and use `===` for comparison.
**Alternative Fixes Tested**: None.
**Result**: Fix works as expected.

## Bug 3 - bug3.cpp
**AI Diagnosis**: The loop uses `i <= n`, which accesses index 5 of a size-5 array, causing an out-of-bounds error. Also, `max_val` is initialized to a very high number, making it impossible to find the real max value in the array.
**Suggested Fix**: Initialize `max_val` with the first element of the array or a very small number, and change the loop condition to `i < n`. Add the missing semicolon at the end of the `cout` line.
**Alternative Fixes Tested**: None.
**Result**: Fix works as expected.

## Bug 4 - bug4.java
**AI Diagnosis**: The `if` statement has a semicolon immediately after the condition, making it an empty statement. The loop also uses `<=` which causes an `ArrayIndexOutOfBoundsException`.
**Suggested Fix**: Remove the semicolon after the `if` condition and change the loop to `i < products.length`.
**Alternative Fixes Tested**: Using a for-each loop to avoid index issues entirely.
**Result**: Fix works as expected.
