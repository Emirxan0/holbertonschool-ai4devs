#!/usr/bin/env python3
"""
Feature: Task Filtering System
Allows filtering tasks by status, priority, and due date.
"""

from datetime import datetime


TASKS = [
    {"id": 1, "title": "Fix login bug", "status": "open", "priority": "high", "due_date": "2025-05-20"},
    {"id": 2, "title": "Write unit tests", "status": "in_progress", "priority": "medium", "due_date": "2025-05-25"},
    {"id": 3, "title": "Update README", "status": "closed", "priority": "low", "due_date": "2025-05-10"},
    {"id": 4, "title": "Code review", "status": "open", "priority": "high", "due_date": "2025-05-18"},
    {"id": 5, "title": "Deploy to staging", "status": "in_progress", "priority": "medium", "due_date": "2025-05-30"},
]


def filter_tasks(tasks, status=None, priority=None, due_before=None, due_after=None):
    """
    Filter tasks by status, priority, and due date range.

    Args:
        tasks (list): List of task dictionaries.
        status (str): Filter by task status (open, in_progress, closed).
        priority (str): Filter by priority (high, medium, low).
        due_before (str): Filter tasks due before this date (YYYY-MM-DD).
        due_after (str): Filter tasks due after this date (YYYY-MM-DD).

    Returns:
        list: Filtered list of tasks.
    """
    result = tasks

    if status:
        result = [t for t in result if t["status"] == status]

    if priority:
        result = [t for t in result if t["priority"] == priority]

    if due_before:
        due_before_dt = datetime.strptime(due_before, "%Y-%m-%d")
        result = [t for t in result if datetime.strptime(t["due_date"], "%Y-%m-%d") <= due_before_dt]

    if due_after:
        due_after_dt = datetime.strptime(due_after, "%Y-%m-%d")
        result = [t for t in result if datetime.strptime(t["due_date"], "%Y-%m-%d") >= due_after_dt]

    return result


def get_task_by_id(tasks, task_id):
    """Return a single task by its ID."""
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


def summarize_tasks(tasks):
    """Return a summary count grouped by status."""
    summary = {"open": 0, "in_progress": 0, "closed": 0}
    for task in tasks:
        status = task.get("status")
        if status in summary:
            summary[status] += 1
    return summary


if __name__ == "__main__":
    print("All tasks:", TASKS)
    print("Open tasks:", filter_tasks(TASKS, status="open"))
    print("High priority:", filter_tasks(TASKS, priority="high"))
    print("Due before 2025-05-21:", filter_tasks(TASKS, due_before="2025-05-21"))
    print("Summary:", summarize_tasks(TASKS))
