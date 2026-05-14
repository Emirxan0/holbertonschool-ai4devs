#!/usr/bin/env python3
"""Unit tests for task_filter.py"""

import unittest
from task_filter import filter_tasks, get_task_by_id, summarize_tasks, TASKS


class TestFilterTasks(unittest.TestCase):

    def test_filter_by_status_open(self):
        result = filter_tasks(TASKS, status="open")
        self.assertTrue(all(t["status"] == "open" for t in result))
        self.assertEqual(len(result), 2)

    def test_filter_by_status_closed(self):
        result = filter_tasks(TASKS, status="closed")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["title"], "Update README")

    def test_filter_by_priority_high(self):
        result = filter_tasks(TASKS, priority="high")
        self.assertEqual(len(result), 2)

    def test_filter_by_due_before(self):
        result = filter_tasks(TASKS, due_before="2025-05-21")
        self.assertTrue(all(t["due_date"] <= "2025-05-21" for t in result))

    def test_filter_combined(self):
        result = filter_tasks(TASKS, status="open", priority="high")
        self.assertEqual(len(result), 2)

    def test_get_task_by_id(self):
        task = get_task_by_id(TASKS, 1)
        self.assertIsNotNone(task)
        self.assertEqual(task["title"], "Fix login bug")

    def test_get_task_by_id_not_found(self):
        task = get_task_by_id(TASKS, 999)
        self.assertIsNone(task)

    def test_summarize_tasks(self):
        summary = summarize_tasks(TASKS)
        self.assertEqual(summary["open"], 2)
        self.assertEqual(summary["in_progress"], 2)
        self.assertEqual(summary["closed"], 1)


if __name__ == "__main__":
    unittest.main()
