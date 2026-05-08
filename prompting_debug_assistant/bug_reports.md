# Structured Bug Reports

## Bug Report - bug1.py
**Summary**: Off-by-one error and incorrect filtering logic in Python.
**Root Cause**: The loop used `range(len(readings) + 1)` which caused an index out of bounds error, and the filter incorrectly targeted negative values.
**Resolution**: Updated the range to `len(readings)` and corrected the filter to `readings[i] >= 0`. Added a check for empty lists.
**Lessons Learned**: Always verify loop boundaries and ensure conditional logic matches the intended business rules.

## Bug Report - bug2.js
**Summary**: Syntax error and incorrect variable referencing in JavaScript.
**Root Cause**: A missing closing parenthesis in the `if` statement and a typo in the variable name `minLenght`.
**Resolution**: Fixed the syntax by adding the missing parenthesis and corrected the variable to `minLength`.
**Lessons Learned**: Use a linter or IDE highlights to catch basic syntax and spelling errors before execution.

## Bug Report - bug3.cpp
**Summary**: Out-of-bounds memory access and incorrect max initialization in C++.
**Root Cause**: Loop condition `i <= n` accessed memory outside the array, and `max_val` was initialized with a high number.
**Resolution**: Changed the loop condition to `i < n` and initialized `max_val` with the first element of the array.
**Lessons Learned**: Be extremely cautious with array indexing in C++ as it does not have built-in bounds checking.

## Bug Report - bug4.java
**Summary**: Logical nullification due to trailing semicolon in Java.
**Root Cause**: A semicolon after the `if` condition `if (stock[i] == 0);` made the code block execute unconditionally.
**Resolution**: Removed the accidental semicolon to correctly link the print statement to the condition.
**Lessons Learned**: Small syntax characters like semicolons can completely change program logic.
