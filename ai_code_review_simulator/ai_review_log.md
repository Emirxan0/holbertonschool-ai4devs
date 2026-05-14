# AI Review Log

**Reviewed File:** `task_filter.py`
**AI Tool Used:** Claude (Anthropic)
**Review Date:** 2025-05-15
**Review Personas:** Security Engineer, Performance Engineer, Maintainability Reviewer, Documentation Reviewer

---

## Inline Comments

### Security Persona

- **(line 6)** `TASKS` is a mutable global list. Any function can modify it at runtime causing unexpected side effects across calls. Use a deep copy or immutable structure: `import copy; tasks = copy.deepcopy(TASKS)` before processing.

- **(line 38)** No whitelist validation for `status` parameter. A caller passing `"OPEN"` or `"done"` gets an empty list with no error — silent failure is a security and UX anti-pattern. Add: `VALID_STATUSES = ("open", "in_progress", "closed")` and raise `ValueError` if input is not in the whitelist.

- **(line 42)** Same problem for `priority` parameter — no validation against allowed values `("high", "medium", "low")`. An attacker or buggy client can pass arbitrary strings with no feedback.

- **(line 45)** Date strings from external input are passed directly to `datetime.strptime` without try/except. A malformed date like `"not-a-date"` raises an unhandled `ValueError` that crashes the entire function. Wrap in try/except and raise a descriptive error.

- **(line 63)** `summarize_tasks()` hardcodes status keys. If the data source ever includes a new status like `"blocked"`, it is silently ignored in the summary — this could mask data integrity issues in production.

### Performance Persona

- **(line 45)** `datetime.strptime(due_before, "%Y-%m-%d")` is called inside the list comprehension body — but it only needs to be called once before the loop. Move it outside: `due_before_dt = datetime.strptime(due_before, "%Y-%m-%d")` and reference `due_before_dt` inside the comprehension.

- **(line 50)** Same performance issue for `due_after` — `datetime.strptime` is called N times (once per task) instead of once. For 10,000 tasks this is 9,999 unnecessary function calls.

- **(line 30)** `filter_tasks()` applies each filter sequentially creating a new list after each step. For four active filters this creates four intermediate lists in memory. A single-pass approach using `all()` with a conditions list would reduce memory allocations to one output list.

- **(line 55)** `get_task_by_id()` is O(n) linear search. If called repeatedly in a loop (e.g., to resolve task relationships), performance degrades to O(n²). Recommend building an index: `task_index = {t["id"]: t for t in tasks}` at load time.

- **(line 63)** `summarize_tasks()` iterates all tasks but uses a hardcoded dict with `.get()` fallback. Using `collections.Counter` would be more Pythonic and handle dynamic statuses automatically: `Counter(t["status"] for t in tasks)`.

### Maintainability Persona

- **(line 1)** No module-level docstring explaining the purpose, usage, or author of this module. Every Python module should start with a docstring.

- **(line 30)** `filter_tasks()` violates the Single Responsibility Principle — it handles status filtering, priority filtering, and two date filters in one function body. Extract helper functions: `_filter_by_status()`, `_filter_by_priority()`, `_filter_by_date_range()` for independent testability.

- **(line 30)** Function signature `filter_tasks(tasks, status=None, priority=None, due_before=None, due_after=None)` has 5 parameters. This is hard to extend — adding a new filter requires changing the function signature. Use a `filters: dict` parameter instead.

- **(line 55)** `get_task_by_id()` returns `None` silently when not found. Callers must remember to check for `None`. Consider raising `KeyError` or a custom `TaskNotFoundError` for explicit error handling.

- **(line 63)** Variable name `summary` inside `summarize_tasks()` is initialized with hardcoded zeros. This creates a maintenance burden — adding a new status requires updating this function manually.

- **(line 75)** The `if __name__ == "__main__"` block is used for manual testing but there is no `try/except` block. Any runtime error will produce a raw Python traceback instead of a user-friendly message.

### Documentation Persona

- **(line 30)** The `filter_tasks()` docstring does not document what happens when no filters are applied (returns all tasks), or what happens on invalid input. The `Raises:` section is missing entirely.

- **(line 55)** `get_task_by_id()` docstring does not mention that it returns `None` when the task is not found — callers cannot know this without reading the implementation.

- **(line 63)** `summarize_tasks()` docstring does not explain that only the three hardcoded statuses are counted. Tasks with other statuses are silently excluded from the summary.

- **(line 1)** No type hints anywhere in the module. PEP 484 type hints should be added to all function signatures: `def filter_tasks(tasks: list[dict], status: str | None = None) -> list[dict]`.

---

## Global Feedback

### Security
- All filter inputs (`status`, `priority`, `due_before`, `due_after`) are accepted without validation. A production API built on this code would silently accept invalid inputs. Implement a validation layer at the entry point of every public function using a whitelist approach.
- Date inputs are not sanitized before being parsed. Passing extremely long strings or special characters could cause unexpected behavior. Validate string length and format with a regex before calling `datetime.strptime`.

### Performance
- The current implementation creates up to four intermediate lists when all filters are active. Refactoring to a single-pass filter using combined conditions would reduce time complexity from O(4n) to O(n) and cut memory allocations by 75%.
- For production use with large datasets, consider adding pagination support to `filter_tasks()` with `limit` and `offset` parameters to avoid returning unbounded result sets.
- `get_task_by_id()` should be replaced with a pre-built index dictionary if it is called more than once in any workflow.

### Maintainability
- The module mixes data (`TASKS`), business logic (`filter_tasks`), and a manual test runner (`__main__`) in a single file. Separate these into `data.py`, `filters.py`, and a proper test file using `unittest` or `pytest`.
- No constants are defined for valid status and priority values. These strings are implicit knowledge — define them as module-level constants: `VALID_STATUSES = ("open", "in_progress", "closed")` and reuse across all functions.
- The `filter_tasks()` function is not easily extensible. A strategy pattern or filter pipeline would allow adding new filter types without modifying existing code (Open/Closed Principle).

### Documentation
- Docstrings exist but are incomplete — none include a `Raises:` section despite multiple functions raising or potentially raising exceptions.
- No usage examples in the docstrings. Adding `Example:` sections following Google docstring style would make the module self-documenting.
- No `CHANGELOG` or inline comment explaining why design decisions were made (e.g., why `None` is returned instead of raising an exception in `get_task_by_id`).

### Testing
- Tests rely on the shared global `TASKS` constant. Any modification to `TASKS` in one test could affect others. Use `setUp()` with a local fixture copy in each test class.
- Edge cases are not tested: empty list input, all-None filters, invalid date strings, unknown status values.
- No performance tests or benchmarks are included to catch regressions on large datasets.
