import tkinter as tk
from tkinter import ttk

from src.views.View import View

"""
    View responsible for edit books.
"""


class BookEditView(tk.Tk, View):
    # -----------------------------------------------------------------------
    #        Constants
    # -----------------------------------------------------------------------
    PAD = 10
    THEADER = [
        "Id", "First name", "Last name", "Zipcode", "Price paid"
    ]

    # -----------------------------------------------------------------------
    #        Constructor
    # -----------------------------------------------------------------------
    """
        @param controller Controller of this view
    """

    def __init__(self, controller):
        super().__init__()
        self.c = controller
        self.title("Cập nhật Sách")

    # -----------------------------------------------------------------------
    #        Methods
    # -----------------------------------------------------------------------
    """
        Creates view's frame.
    """

    def _make_main_frame(self):
        self.frame_main = tk.Frame(self)
        self.frame_main.pack()

    """
        Sets view's title.
    """

    def _make_title(self):
        title = ttk.Label(self.frame_main, text="Quản Lý Sách", font=("Helvetica", 20))
        title.pack(padx=self.PAD, pady=self.PAD)

    """
        Creates book fields.
    """

    def _show_book_fields(self):
        book = self.c.get_book()
        frame_book = tk.Frame(self.frame_main)
        frame_book.pack()
        id_book = book[0]
        fields = []

        for i in range(0, len(book)):
            # Show headers
            lbl = tk.Label(frame_book, text=self.THEADER[i])
            lbl.grid(row=i, column=0)

            # Show book data
            e = ttk.Entry(frame_book, width=30)
            e.insert(0, book[i])
            fields.append(e)

            # Let id field as read_only
            if i == 0:
                e.configure(state="readonly")

            e.grid(row=i, column=1)

        # Show clear button
        frame_book_buttons = tk.Frame(self.frame_main)
        frame_book_buttons.pack()
        btn_submit = ttk.Button(frame_book_buttons, text="Save",
                                command=lambda: self.c.btn_save(fields))
        btn_submit.pack(side='right')

    """
    @Overrite
    """

    def main(self):
        self._make_main_frame()
        self._make_title()
        self._show_book_fields()

        self.attributes("-topmost", True)
        self.mainloop()

    """
    @Overrite
    """

    def close(self):
        self.destroy()
