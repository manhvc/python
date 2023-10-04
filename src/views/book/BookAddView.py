# View
import tkinter as tk
from tkinter import ttk


class BookAddView(tk.Tk):
    # -----------------------------------------------------------------------
    #        Constants
    # -----------------------------------------------------------------------
    PAD = 10
    FIELDS = [
        "Tên Sách", "Tác Giả", "Ngày Xuất Bản", "Số lượng"
    ]

    # -----------------------------------------------------------------------
    #        Constructor
    # -----------------------------------------------------------------------
    """
        @param controller Controller of this view
    """

    def __init__(self, controller):
        super().__init__()
        self.title("Quản Lý Sách")
        self.c = controller

        self._make_main_frame()
        self._make_title()
        self._add_books()

    # -----------------------------------------------------------------------
    #        Methods
    # -----------------------------------------------------------------------
    """
        Creates view's frame.
    """

    def _make_main_frame(self):
        self.frame_main = ttk.Frame(self)
        self.frame_main.pack()

    """
        Sets view's title.
    """

    def _make_title(self):
        title = ttk.Label(self.frame_main, text="Thêm Sách", font=("Helvetica", 20))
        title.pack(padx=self.PAD, pady=self.PAD)

    """
        Displays customers on screen.
    """

    """
           Creates view's fields.
       """

    def _add_books(self):
        frame_fields = tk.Frame(self.frame_main)
        frame_fields.pack()
        fields = []

        i = 0
        for field in self.FIELDS:
            # Show headers
            f = ttk.Label(frame_fields, text=field)
            f.grid(row=i, column=0)

            # Show fields
            e = ttk.Entry(frame_fields, width=30)
            e.grid(row=i, column=1)
            fields.append(e)

            i += 1

        # Make buttons
        frame_buttons = tk.Frame(self.frame_main)
        frame_buttons.pack()

        btn_submit = ttk.Button(frame_buttons, text="Create", command=lambda: self.c.btn_add(fields))
        btn_submit.pack(side="left")

        btn_clear = ttk.Button(frame_buttons, text="Clear", command=lambda: self.c.btn_clear(fields))
        btn_clear.pack(side="left")

    """
        @Override
    """

    def main(self):
        self.mainloop()

    """
    @Override
    """

    def close(self):
        return
