## bug1.py
- Original Issue: Off-by-one error in loop range causing an IndexError.
- Fix Applied: Adjusted slice/range index logic to stop before the boundary.
- Test Results: All 3 test cases passed.

## bug2.py
- Original Issue: Missing input validation allowing potential code injection or crash.
- Fix Applied: Added explicit type checking and boundary validation.
- Test Results: Verified with edge cases, 100% success rate.
