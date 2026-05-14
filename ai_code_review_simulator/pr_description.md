# Pull Request: Add Task Filtering Feature

## Summary
Implements a task filtering system that allows filtering tasks by status, priority, and due date range. Adds core filtering logic and a task summary function.

## Changes
- Added `filter_tasks()` in `task_filter.py` — filters by status, priority, due_before, due_after
- Added `get_task_by_id()` — retrieves a single task by ID
- Added `summarize_tasks()` — returns task count grouped by status
- Added `test_task_filter.py` with 8 unit tests covering all functions

## Context
~120 LOC. This feature enables users to query tasks efficiently without loading all data. Motivation: improve task management workflow and support future API endpoint `/tasks/filter`.
