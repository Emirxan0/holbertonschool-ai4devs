## Bug 1 – bug1.py
**Intended Behavior**: The function should calculate the mathematical average of all positive temperature readings from a provided list. It must handle empty lists without crashing and iterate through all elements correctly.
**Issue Type**: Logical Error, Off-by-one, Runtime Exception.
**Notes**: The loop condition incorrectly targets negative values, fails to process the final list element, and causes a division by zero error when no valid readings are found.

## Bug 2 – bug2.js
**Intended Behavior**: The function must validate a user object by ensuring they are at least 18 years old and their password meets a minimum length of 8 characters. It should also verify user roles without modifying the object properties.
**Issue Type**: Syntax Error, Reference Error, Logical Error.
**Notes**: Missing parentheses in the if-statement, a typo in the variable name 'minLength', and the use of an assignment operator instead of a comparison operator for role checking.

## Bug 3 – bug3.cpp
**Intended Behavior**: The program is designed to identify and print the largest integer value stored within a fixed-size array by comparing each element one by one.
**Issue Type**: Logical Error, Runtime Error (Out of Bounds), Syntax Error.
**Notes**: The loop boundary attempts to access memory outside the array limits, and the initialization of max_val with a high number prevents correct identification.

## Bug 4 – bug4.java
**Intended Behavior**: The system should iterate through the product inventory and print an alert message only for items whose stock count is exactly zero, while processing all product names into lowercase for display.
**Issue Type**: Logical Error, Array Index Out of Bounds.
**Notes**: An extra semicolon after the if-condition nullifies the check, causing the alert to trigger for bll items. The loop also exceeds array bounds by using a <= condition.
