# Structured Bug Reports

## Bug 1: Array Index Out of Bounds in Python
**Description**: The loop in `bug1.py` attempted to access an index outside the list's range.
**Root Cause**: Used `range(len(data) + 1)` which goes one step beyond the last valid index.
**Fix**: Changed the range to `len(data)` to stay within boundaries.
**AI Interaction**: AI identified the off-by-one error and suggested adding a check for empty lists.

## Bug 2: Syntax and Reference Error in JavaScript
**Description**: The code failed to execute due to missing syntax and incorrect variable references.
**Root Cause**: A missing closing parenthesis in an `if` statement and a typo in the variable name `minLenght`.
**Fix**: Added the missing parenthesis and corrected the variable spelling to `minLength`.
**AI Interaction**: AI pinpointed the syntax location and highlighted the assignment `=` vs comparison `===` issue.

## Bug 3: Logic and Boundary Error in C++
**Description**: The program failed to find the maximum value and accessed forbidden memory.
**Root Cause**: Initializing `max_val` with a high number and using `i <= n` in the loop.
**Fix**: Initialized `max_val` with the first element and changed the loop condition to `i < n`.
**AI Interaction**: AI explained the risks of out-of-bounds access in C++ and suggested safer initialization.

## Bug 4: Logical Nullification in Java
**Description**: The alert for empty stock triggered for every single item regardless of the count.
**Root Cause**: An accidental semicolon after the `if` condition: `if (stock[i] == 0);`.
**Fix**: Removed the semicolon to link the code block to the condition correctly.
**AI Interaction**: AI detected the "Empty If" pattern and suggested a more robust for-each loop.
