## bug1.py
- Original Issue: Risk of ZeroDivisionError when the provided list is empty.
- Fix Applied: Added a conditional check to return 0 immediately if the list is empty and refactored loop to use native sum().
- Test Results: Verified with empty, single-element, and multi-element lists. All test cases passed.

## bug2.py
- Original Issue: Asynchronous fetch called synchronously, causing an empty object to be logged and returned.
- Fix Applied: Converted the function into an async/await block to ensure data is fetched before execution proceeds.
- Test Results: Handled resolve and reject execution states perfectly.

## bug3.py
- Original Issue: Out-of-bounds array access and incorrect loop boundary causing string to reverse back to original.
- Fix Applied: Adjusted the loop to terminate at n / 2 and fixed indices to target elements correctly within valid bounds.
- Test Results: Verified with "Hello" successfully printing reversed outputs.

## bug4.py
- Original Issue: Used incorrect slice step (-2) and did not handle string normalization for uppercase letters or spaces.
- Fix Applied: Implemented proper string lowering, removed spaces, and used the correct standard reverse slice [::-1].
- Test Results: Evaluates "Racecar" properly as True. All test cases passed.
