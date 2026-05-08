# Structured Bug Reports

## Bug Report 1: bug1.py (Python)
**Description**: The loop in `bug1.py` attempted to access an index outside the list's range.
**Root Cause**: The code used `range(len(data) + 1)`, which goes one step beyond the last valid index of the array.
**Fix**: Changed the range to `len(data)` to stay within valid index boundaries.
**AI Interaction**: AI identified the off-by-one error and suggested adding a check for empty lists to prevent ZeroDivisionError.

## Bug Report 2: bug2.js (JavaScript)
**Description**: The code failed to execute due to critical syntax errors and incorrect variable references.
**Root Cause**: A missing closing parenthesis in an `if` statement and a typo in the variable name `minLenght` instead of `minLength`.
**Fix**: Added the missing parenthesis and corrected the variable spelling to match the declaration.
**AI Interaction**: AI pinpointed the syntax location and highlighted the logic error of using assignment `=` instead of comparison `===`.

## Bug Report 3: bug3.cpp (C++)
**Description**: The program failed to find the maximum value and caused a runtime crash by accessing forbidden memory.
**Root Cause**: Initializing `max_val` with an arbitrarily high number and using `i <= n` in the loop condition, leading to an out-of-bounds access.
**Fix**: Initialized `max_val` with the first element of the array and changed the loop condition to `i < n`.
**AI Interaction**: AI explained the risks of out-of-bounds access in C++ and suggested safer initialization techniques.

## Bug Report 4: bug4.java (Java)
**Description**: The inventory alert for empty stock triggered for every single item regardless of the actual stock count.
**Root Cause**: An accidental semicolon was placed after the `if` condition: `if (stock[i] == 0);`, which nullified the conditional check.
**Fix**: Removed the semicolon to correctly link the code block to the conditional statement.
**AI Interaction**: AI detected the "Empty If Statement" pattern and suggested removing the semicolon or using a for-each loop.
