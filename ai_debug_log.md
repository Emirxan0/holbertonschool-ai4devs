## Bug 1 – bug1.py
**AI Diagnosis**: The slice `items[len(items) - n - 1:]` starts one index too early, including an extra element.
**Suggested Fix**: Change the slice to `items[len(items) - n:]`.
**Alternative Fixes Tested**: None.
**Result**: Fix works as expected, correctly returning the last 3 items.

