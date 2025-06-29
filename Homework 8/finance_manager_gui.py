import tkinter as tk
from tkinter import ttk, messagebox
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
            raise TypeError("Amount must be a number.")
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        self.income.append({"source": source, "amount": amount})
        self.save_data()

    def add_expense(self, description, category, amount, date_str):
        if not description:
            raise ValueError("Description is required.")
        if not category:
            raise ValueError("Category is required.")
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number.")
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date must be YYYY-MM-DD.")
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
        return sum(i["amount"] for i in self.income)

    def total_expenses(self):
        return sum(e["amount"] for e in self.expenses)

    def remaining_balance(self):
        return self.total_income() - self.total_expenses()

    def save_data(self):
        with open("finance_data.txt", "w") as f:
            f.write("Income:\n")
            for i in self.income:
                f.write(f"{i['source']} - {i['amount']}\n")
            f.write("\nExpenses:\n")
            for e in self.expenses:
                f.write(f"{e['description']} - {e['category']} - {e['amount']} - {e['date']}\n")
            f.write("\nSummary:\n")
            f.write(f"Total Income: {self.total_income()}\n")
            f.write(f"Total Expenses: {self.total_expenses()}\n")
            f.write(f"Remaining Balance: {self.remaining_balance()}\n")

        with open("finance_data.json", "w") as f_json:
            json.dump({"income": self.income, "expenses": self.expenses}, f_json, indent=4)

    def load_data(self):
        if os.path.exists("finance_data.json"):
            try:
                with open("finance_data.json", "r") as f_json:
                    data = json.load(f_json)
                    self.income = data.get("income", [])
                    self.expenses = data.get("expenses", [])
            except (IOError, json.JSONDecodeError) as e:
                print("Error loading data:", e)

class FinanceApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Personal Finance Manager")
        self.geometry("700x600")
        self.manager = FinanceManager()
        self.create_widgets()
        self.refresh_summary()
        self.refresh_lists()

    def create_widgets(self):
        # Income Inputs
        tk.Label(self, text="Add Income").grid(row=0, column=0, columnspan=2, pady=5, sticky="w")
        tk.Label(self, text="Source:").grid(row=1, column=0, sticky="e")
        self.income_source_entry = tk.Entry(self)
        self.income_source_entry.grid(row=1, column=1)
        tk.Label(self, text="Amount:").grid(row=2, column=0, sticky="e")
        self.income_amount_entry = tk.Entry(self)
        self.income_amount_entry.grid(row=2, column=1)
        tk.Button(self, text="Add Income", command=self.add_income).grid(row=3, column=0, columnspan=2, pady=5)

        # Expense Inputs
        tk.Label(self, text="Add Expense").grid(row=4, column=0, columnspan=2, pady=5, sticky="w")
        tk.Label(self, text="Description:").grid(row=5, column=0, sticky="e")
        self.expense_desc_entry = tk.Entry(self)
        self.expense_desc_entry.grid(row=5, column=1)
        tk.Label(self, text="Category:").grid(row=6, column=0, sticky="e")
        self.expense_category = ttk.Combobox(self, values=["Food", "Rent", "Utilities", "Entertainment", "Health", "Other"])
        self.expense_category.grid(row=6, column=1)
        tk.Label(self, text="Amount:").grid(row=7, column=0, sticky="e")
        self.expense_amount_entry = tk.Entry(self)
        self.expense_amount_entry.grid(row=7, column=1)
        tk.Label(self, text="Date (YYYY-MM-DD):").grid(row=8, column=0, sticky="e")
        self.expense_date_entry = tk.Entry(self)
        self.expense_date_entry.grid(row=8, column=1)
        tk.Button(self, text="Add Expense", command=self.add_expense).grid(row=9, column=0, columnspan=2, pady=5)

        # Summary
        self.summary_label = tk.Label(self, text="", justify="left", font=("Arial", 12, "bold"))
        self.summary_label.grid(row=0, column=2, rowspan=4, padx=10, sticky="nw")

        # Income List
        tk.Label(self, text="Incomes").grid(row=4, column=2, sticky="w", padx=10)
        self.income_listbox = tk.Listbox(self, width=40)
        self.income_listbox.grid(row=5, column=2, rowspan=4, padx=10)
        tk.Button(self, text="Delete Selected Income", command=self.delete_income).grid(row=9, column=2, pady=5)

        # Expense List
        tk.Label(self, text="Expenses").grid(row=10, column=0, sticky="w")
        self.expense_listbox = tk.Listbox(self, width=80)
        self.expense_listbox.grid(row=11, column=0, columnspan=3, padx=10)
        tk.Button(self, text="Delete Selected Expense", command=self.delete_expense).grid(row=12, column=0, columnspan=3, pady=5)

    def add_income(self):
        source = self.income_source_entry.get().strip()
        try:
            amount = float(self.income_amount_entry.get())
            self.manager.add_income(source, amount)
            self.income_source_entry.delete(0, tk.END)
            self.income_amount_entry.delete(0, tk.END)
            self.refresh_lists()
            self.refresh_summary()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def add_expense(self):
        description = self.expense_desc_entry.get().strip()
        category = self.expense_category.get().strip()
        date_str = self.expense_date_entry.get().strip()
        try:
            amount = float(self.expense_amount_entry.get())
            self.manager.add_expense(description, category, amount, date_str)
            self.expense_desc_entry.delete(0, tk.END)
            self.expense_category.set("")
            self.expense_amount_entry.delete(0, tk.END)
            self.expense_date_entry.delete(0, tk.END)
            self.refresh_lists()
            self.refresh_summary()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_income(self):
        selection = self.income_listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "Please select an income to delete.")
            return
        index = selection[0]
        try:
            self.manager.delete_income(index)
            self.refresh_lists()
            self.refresh_summary()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_expense(self):
        selection = self.expense_listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "Please select an expense to delete.")
            return
        index = selection[0]
        try:
            self.manager.delete_expense(index)
            self.refresh_lists()
            self.refresh_summary()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def refresh_lists(self):
        self.income_listbox.delete(0, tk.END)
        for i in self.manager.income:
            self.income_listbox.insert(tk.END, f"{i['source']} - {i['amount']}")
        self.expense_listbox.delete(0, tk.END)
        for e in self.manager.expenses:
            self.expense_listbox.insert(tk.END, f"{e['description']} - {e['category']} - {e['amount']} - {e['date']}")

    def refresh_summary(self):
        self.summary_label.config(
            text=(
                f"Summary:\n"
                f"Total Income: {self.manager.total_income()}\n"
                f"Total Expenses: {self.manager.total_expenses()}\n"
                f"Remaining Balance: {self.manager.remaining_balance()}"
            )
        )

if __name__ == "__main__":
    app = FinanceApp()
    app.mainloop()
