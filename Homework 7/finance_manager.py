

import json
import os
from datetime import datetime

class FinanceManager:
    def __init__(self):
        self.income = []
        self.expenses = []
        self.load_data()

    def add_income(self, source, amount):
        if not source:
            raise ValueError("Income source is required.")
        if not isinstance(amount, (int, float)):
            raise TypeError("Income amount must be a number.")
        if amount < 0:
            raise ValueError("Income amount cannot be negative.")
        self.income.append({"source": source, "amount": amount})
        self.save_data()

    def add_expense(self, description, category, amount, date_str):
        if not description:
            raise ValueError("Expense description is required.")
        if not category:
            raise ValueError("Expense category is required.")
        if not isinstance(amount, (int, float)):
            raise TypeError("Expense amount must be a number.")
        if amount < 0:
            raise ValueError("Expense amount cannot be negative.")
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format.")
        self.expenses.append({
            "description": description,
            "category": category,
            "amount": amount,
            "date": date_str
        })
        self.save_data()

    def delete_income(self, index):
        if index < 0 or index >= len(self.income):
            raise IndexError("Invalid income index.")
        del self.income[index]
        self.save_data()

    def delete_expense(self, index):
        if index < 0 or index >= len(self.expenses):
            raise IndexError("Invalid expense index.")
        del self.expenses[index]
        self.save_data()

    def total_income(self):
        return sum(entry["amount"] for entry in self.income)

    def total_expenses(self):
        return sum(entry["amount"] for entry in self.expenses)

    def remaining_balance(self):
        return self.total_income() - self.total_expenses()

    def save_data(self):
        try:
            with open("finance_data.txt", "w") as f:
                f.write("Income:\n")
                for i in self.income:
                    f.write(f"{i['source']} - {i['amount']}\n")
                f.write("Expenses:\n")
                for e in self.expenses:
                    f.write(f"{e['description']} - {e['category']} - {e['amount']} - {e['date']}\n")
            with open("finance_data.json", "w") as f_json:
                json.dump({"income": self.income, "expenses": self.expenses}, f_json, indent=4)
        except IOError as e:
            print("Error saving data:", e)

    def load_data(self):
        if os.path.exists("finance_data.json"):
            try:
                with open("finance_data.json", "r") as f_json:
                    data = json.load(f_json)
                    self.income = data.get("income", [])
                    self.expenses = data.get("expenses", [])
            except (IOError, json.JSONDecodeError) as e:
                print("Error loading data:", e)
