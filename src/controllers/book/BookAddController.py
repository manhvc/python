from tkinter import messagebox
from tkinter.constants import END

from src.core.Controller import Controller
from src.core.Core import Core
from src.models.BookModel import BookModel


# Controller
class BookAddController(Controller):
    def __init__(self):
        self.book_model = BookModel()
        self.add_view = self.load_view("Book", "Add")
        self.core = Core()

    """
        Clear all fields of AddView

        @param fields Fields to be cleared
    """

    def btn_clear(self, fields):
        for field in fields:
            field.delete(0, END)

    """
        Adds a new customer with field data

        @param fields Fields with customer data
    """

    def btn_add(self, fields):
        response = self.book_model.add(fields)

        if response > 0:
            messagebox.showinfo("Add Books", "Books successfully added!")
        else:
            messagebox.showerror("Add Books", "Error while adding Books")

        self.add_view.close()

    def main(self):
        self.add_view.main()
