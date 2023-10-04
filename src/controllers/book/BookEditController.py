from tkinter import messagebox

from src.core.Controller import Controller
from src.models.BookModel import BookModel

"""
    Responsible for EditView behavior.
"""


class BookEditController(Controller):
    # -----------------------------------------------------------------------
    #        Constructor
    # -----------------------------------------------------------------------
    def __init__(self):
        self.edit_view = self.load_view("book", "edit")
        self.book_model = BookModel()

    # -----------------------------------------------------------------------
    #        Methods
    # -----------------------------------------------------------------------
    """
        @Override
    """

    def main(self, book, show_view):
        self.show_view = show_view
        self.book = book
        self.edit_view.main()

    """
        @return Customer being edited
    """

    def get_book(self):
        return self.book

    """
        Saves customer edited

        @param fields Customer data edited
    """

    def btn_save(self, fields):
        response = self.book_model.update(fields)
        self.show_view.attributes("-topmost", False)
        if response > 0:
            messagebox.showinfo("Update customer", "Customer updated with success!")
        else:
            messagebox.showerror("Update customer", "Error while updating")
        self.show_view.attributes("-topmost", True)
        self.show_view.update()
        self.show_view.close()
        self.show_view.attributes("-topmost", False)
