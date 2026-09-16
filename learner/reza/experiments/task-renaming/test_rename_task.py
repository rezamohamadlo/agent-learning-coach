from copy import deepcopy
import unittest

from rename_task import rename_task


class RenameTaskTests(unittest.TestCase):
    def setUp(self):
        self.tasks = [
            {"id": 2, "title": "Practice Python", "done": True},
            {"id": 1, "title": "Read chapter", "done": False},
        ]
        self.before = deepcopy(self.tasks)

    def test_success_preserves_records_and_order(self):
        for task_id in (1, 2):
            with self.subTest(task_id=task_id):
                result = rename_task(self.tasks, task_id, "New title")
                expected = deepcopy(self.before)
                for task in expected:
                    if task["id"] == task_id:
                        task["title"] = "New title"
                self.assertEqual(result, expected)
                self.assertIsNot(result, self.tasks)
                self.assertEqual(self.tasks, self.before)

    def test_trims_both_ends(self):
        for title in (" name", "name ", " name ", "\tname\n"):
            with self.subTest(title=title):
                result = rename_task(self.tasks, 1, title)
                self.assertEqual(result[1]["title"], "name")
                self.assertEqual(self.tasks, self.before)

    def test_rejects_empty_titles_without_mutation(self):
        for title in ("", "   ", "\t\n"):
            with self.subTest(title=title):
                with self.assertRaises(ValueError):
                    rename_task(self.tasks, 1, title)
                self.assertEqual(self.tasks, self.before)

    def test_rejects_unknown_id_without_mutation(self):
        with self.assertRaises(ValueError):
            rename_task(self.tasks, 99, "New title")
        self.assertEqual(self.tasks, self.before)

    def test_empty_list_has_no_matching_id(self):
        with self.assertRaises(ValueError):
            rename_task([], 1, "New title")


if __name__ == "__main__":
    unittest.main()
