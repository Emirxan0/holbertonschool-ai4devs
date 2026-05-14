# AI Review Log

**Reviewed File:** `task_filter.py`
**AI Tool Used:** Claude (Anthropic)
**Review Date:** 2025-05-15
**Review Personas:** Security, Performance, Maintainability

---

## Inline Comments

- **(line 6)** Global `TASKS` list should not be defined in the module scope. It couples data to logic and makes testing harder. Move it to a separate data layer or pass it as a parameter.

- **(line 30)** `filter_tasks()` has too many parameters. Consider accepting a single `filters` dictionary instead: `filter_tasks(tasks, filters={})`. This improves extensibility and reduces function signature complexity.

- **(line 38)** No input validation for `status` parameter. Invalid values like `"done"` or `"OPEN"` will silently return empty results. Add validation: `if status not in ("open", "in_progress", "closed"): raise ValueError(...)`.

- **(line 42)** No input validation for `priority` parameter. Same issue as `status` — invalid values fail silently without any error message to the caller.

- **(line 45)** `datetime.strptime` inside the list comprehension is called once per task. For large datasets this is inefficient. Parse `due_before` once before the list comprehension and reuse the result.

- **(line 50)** Same performance issue as line 45 — `datetime.strptime(due_after, ...)` should be parsed outside the list comprehension.

- **(line 55)** `get_task_by_id()` uses a linear search O(n). If the task list grows large, consider using a dictionary keyed by ID for O(1) lookup: `tasks_dict = {t["id"]: t for t in tasks}`.

- **(line 63)** `summarize_tasks()` hardcodes status values `("open", "in_progress", "closed")`. If a new status is added in the future, this function will silently ignore it. Use dynamic grouping instead.

- **(line 75)** The `if __name__ == "__main__"` block lacks error handling. If the data or date format is wrong, the script will crash with an unhandled exception.

- **(line 1)** No logging is implemented. For a production system, add Python `logging` module instead of `print()` statements to allow log level control.

---

## Global Feedback

- **Error Handling:** The module has no try/except blocks. Date parsing with `datetime.strptime` will raise `ValueError` on invalid date strings. Wrap date parsing in try/except and return meaningful error messages.

- **Security:** No input sanitization is applied to filter parameters. While this is not a SQL-injection risk (no DB), it is good practice to validate and sanitize all inputs before processing, especially if this becomes an API endpoint.

- **Performance:** For datasets with thousands of tasks, chaining multiple list comprehensions creates multiple intermediate lists. Consider using `filter()` with combined conditions or a single-pass loop for better memory efficiency.

- **Maintainability:** The `filter_tasks()` function handles four different filter types in one function body. Splitting into smaller helper functions (`_filter_by_status()`, `_filter_by_date()`) would improve readability and unit testability.

- **Type Hints:** No type annotations are used. Adding type hints (e.g., `def filter_tasks(tasks: list[dict], status: str = None) -> list[dict]`) would improve IDE support and catch type errors early.

- **Documentation:** Docstrings are present but do not document possible exceptions (e.g., `ValueError` for bad date format). Update docstrings to include `Raises:` section following Google or NumPy docstring style.

- **Testing:** Tests use the global `TASKS` constant directly. Tests should use isolated fixture data so that changes to `TASKS` do not break unrelated tests.

- **Naming:** The variable name `result` used throughout `filter_tasks()` is too generic. More descriptive names like `filtered_tasks` would improve readability.
