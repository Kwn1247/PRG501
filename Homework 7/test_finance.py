
import unittest
import os
from finance_manager import FinanceManager

class TestFinanceManager(unittest.TestCase):

    def setUp(self):
        # Use a fresh instance for each test
        self.fm = FinanceManager()
        self.fm.income = []
        self.fm.expenses = []

    def test_add_income(self):
        self.fm.add_income("Salary", 15000)
        self.assertEqual(len(self.fm.income), 1)
        self.assertEqual(self.fm.total_income(), 15000)

    def test_add_expense(self):
        self.fm.add_expense("Groceries", "Food", 2200, "2024-06-20")
        self.assertEqual(len(self.fm.expenses), 1)
        self.assertEqual(self.fm.total_expenses(), 2200)

    def test_remaining_balance(self):
        self.fm.add_income("Job", 6000)
        self.fm.add_expense("Rent", "Housing", 1000, "2024-06-20")
        self.assertEqual(self.fm.remaining_balance(), 5000)

    def test_invalid_income_amount(self):
        with self.assertRaises(TypeError):
            self.fm.add_income("Freelance", "not a number")

    def test_negative_income(self):
        with self.assertRaises(ValueError):
            self.fm.add_income("Freelance", -100)

    def test_missing_income_source(self):
        with self.assertRaises(ValueError):
            self.fm.add_income("", 100)

    def test_invalid_expense_amount(self):
        with self.assertRaises(TypeError):
            self.fm.add_expense("Dinner", "Food", "abc", "2024-06-20")

    def test_negative_expense(self):
        with self.assertRaises(ValueError):
            self.fm.add_expense("Dinner", "Food", -20, "2024-06-20")

    def test_invalid_date_format(self):
        with self.assertRaises(ValueError):
            self.fm.add_expense("Dinner", "Food", 20, "06-20-2024")

    def test_delete_income(self):
        self.fm.add_income("Job", 1000)
        self.fm.delete_income(0)
        self.assertEqual(len(self.fm.income), 0)

    def test_delete_expense(self):
        self.fm.add_expense("Dinner", "Food", 50, "2024-06-20")
        self.fm.delete_expense(0)
        self.assertEqual(len(self.fm.expenses), 0)

    def test_invalid_delete_income_index(self):
        with self.assertRaises(IndexError):
            self.fm.delete_income(0)

    def test_invalid_delete_expense_index(self):
        with self.assertRaises(IndexError):
            self.fm.delete_expense(0)

if __name__ == "__main__":
    unittest.main()
