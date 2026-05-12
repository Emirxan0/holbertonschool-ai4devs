# AI Debug Log
**Project**: AI-Assisted Debugging  
**Directory**: `prompting_debug_assistant/bug_snippets`  
**Assistant Used**: Claude (Anthropic)

---

## Bug 1 – `bug1.py`

**Prompt Used**:
> "This code is supposed to return the last n items from a list, but it doesn't behave as expected. Can you identify and explain the issue and how to fix it?"

**AI Diagnosis**:
The slice `items[n:]` starts from index `n` from the front of the list, not the end. For example, `last_n_items([1,2,3,4,5], 2)` returns `[3,4,5]` instead of `[4,5]`. When `n == len(items)`, it returns an empty list instead of the full list.

**Root Cause**:
`items[n:]` slices forward from position `n`. The correct approach uses negative indexing: `items[-n:]`.

**Suggested Fix**:
```python
def last_n_items(items, n):
    if n == 0:
        return []
    return items[-n:]
```

**Alternative Fixes Tested**:
`items[len(items) - n:]` also works but is more verbose.

**Result**: Fix works as expected.

---

## Bug 2 – `bug2.js`

**Prompt Used**:
> "This discount function doesn't apply the correct discount for purchases over $200. Can you identify and explain the issue and how to fix it?"

**AI Diagnosis**:
Conditions are evaluated in the wrong order. Since `total >= 100` is checked first, any value >= 200 matches the first branch and only gets 10% off. The `>= 200` branch is dead/unreachable code.

**Root Cause**:
In an if/else if chain the more specific (larger) condition must come first.

**Suggested Fix**:
```javascript
function applyDiscount(total) {
  let discount = 0;
  if (total >= 200) {
    discount = 0.20;
  } else if (total >= 100) {
    discount = 0.10;
  }
  const discountAmount = total * discount;
  const finalPrice = total - discountAmount;
  return parseFloat(finalPrice.toFixed(2));
}
```

**Alternative Fixes Tested**: Explicit range check with separate if statements — works but less clean.

**Result**: Fix works as expected.

---

## Bug 3 – `bug3.py`

**Prompt Used**:
> "This function throws a TypeError when comparing ages. Can you identify and explain the issue and how to fix it?"

**AI Diagnosis**:
`str.split()` returns strings. Comparing a string to an integer raises `TypeError: '>=' not supported between instances of 'str' and 'int'`. Also, spaces after commas must be stripped.

**Root Cause**:
Missing `int()` type conversion before comparison and arithmetic.

**Suggested Fix**:
```python
def average_adult_age(csv_ages: str) -> float:
    ages = [int(age.strip()) for age in csv_ages.split(",")]
    adults = [age for age in ages if age >= 18]
    if not adults:
        return 0.0
    return sum(adults) / len(adults)
```

**Alternative Fixes Tested**: Inline double-call to `int(age.strip())` in list comprehension — works but converts twice.

**Result**: Fix works as expected. Input `"15, 22, 17, 34, 28, 16, 45"` → `32.25`

---

## Bug 4 – `bug4.c`

**Prompt Used**:
> "This C function crashes on empty strings. Can you identify and explain the issue and how to fix it?"

**AI Diagnosis**:
`strlen()` returns `size_t` (unsigned). For an empty string, `0 - 1` wraps to `SIZE_MAX` due to unsigned underflow, causing out-of-bounds access, segfault, or infinite loop.

**Root Cause**:
Unsigned integer underflow on `strlen(str) - 1` when string is empty.

**Suggested Fix**:
```c
void reverse_string(char *str) {
    if (str == NULL || str[0] == '\0')
        return;
    int left = 0;
    int right = (int)strlen(str) - 1;
    while (left < right) {
        char tmp  = str[left];
        str[left] = str[right];
        str[right] = tmp;
        left++;
        right--;
    }
}
```

**Alternative Fixes Tested**: Using `size_t len = strlen(str); if (len == 0) return;` — also valid.

**Result**: Fix works as expected. Empty string no longer crashes.

---

## Bug 5 – `bug5.js`

**Prompt Used**:
> "This async function returns undefined and has unhandled promise rejections. Can you identify all issues and how to fix them?"

**AI Diagnosis**:
Three bugs: (1) missing `await` on `response.json()` so `data` is a Promise and `data.email` is always undefined; (2) no HTTP status check so missing users return undefined instead of null; (3) no try/catch so network errors cause unhandled rejections.

**Root Cause**:
Forgetting `await` before `response.json()` is a common async/await mistake. The other issues are missing defensive programming.

**Suggested Fix**:
```javascript
async function getUserEmail(userId) {
  try {
    const response = await fetch(`https://jsonplaceholder.typicode.com/users/${userId}`);
    if (!response.ok) return null;
    const data = await response.json();
    return data.email ?? null;
  } catch (err) {
    console.error("Network error:", err);
    return null;
  }
}
```

**Alternative Fixes Tested**: None needed — the three-part fix addresses all issues.

**Result**: Fix works as expected. Valid ID returns email, invalid ID returns null.

---

## Bug 6 – `bug6.py`

**Prompt Used**:
> "This Fibonacci function has a syntax error and produces wrong results. Can you identify all issues and how to fix them?"

**AI Diagnosis**:
Two bugs: (1) `n = 0` uses assignment `=` instead of equality `==`, causing SyntaxError; (2) recursive call is `fib(n-1) + fib(n-1)` instead of `fib(n-1) + fib(n-2)`, producing powers of 2 instead of Fibonacci numbers.

**Root Cause**:
Bug 1: `=` vs `==` confusion. Bug 2: copy-paste error writing `n-1` twice.

**Suggested Fix**:
```python
def fib(n, cache={}):
    if n == 0 or n == 1:
        return n
    if n in cache:
        return cache[n]
    result = fib(n - 1) + fib(n - 2)
    cache[n] = result
    return result
```

**Alternative Fixes Tested**: None needed.

**Result**: Fix works as expected. fib(0..7) = 0,1,1,2,3,5,8,13 ✅

---

## Summary Table

| Bug | File    | Language   | Bug Type                        | Fixed |
|-----|---------|------------|---------------------------------|-------|
| 1   | bug1.py | Python     | Off-by-one error (slicing)      | ✅    |
| 2   | bug2.js | JavaScript | Logical error (condition order) | ✅    |
| 3   | bug3.py | Python     | TypeError (missing type cast)   | ✅    |
| 4   | bug4.c  | C          | Unsigned underflow / UB         | ✅    |
| 5   | bug5.js | JavaScript | Missing await + no error guard  | ✅    |
| 6   | bug6.py | Python     | SyntaxError + logical error     | ✅    |
