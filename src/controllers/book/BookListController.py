from tkinter import messagebox

from src.core.Controller import Controller
from src.core.Core import Core
from src.models.BookModel import BookModel


# Controller
class BookListController(Controller):
    def __init__(self):
        self.book_model = BookModel()
        self.book_view = self.load_view("Book", "List")
        self.core = Core()

    def get_list_books(self):
        data = self.book_model.get_all()
        return data

    """
           Opens EditController

           @param id_customer Customer id that will be edited
       """

    def btn_edit(self, book_id):
        book = self.book_model.get(book_id)
        c = self.core.open_controller("Book", "Edit")
        c.main(book, self.book_view)

    """
        Deletes the chosen customer and updates the ShowView

        @param id_customer Customer id that will be edited
    """

    def btn_del(self, book_id):
        self.book_model.delete(book_id)
        self.book_view.update()
        messagebox.showinfo("Delete Book", "Book deleted with success!")

    def main(self):
        self.book_view.main()

    """
        Clear all fields of AddView

        @param fields Fields to be cleared
    """
