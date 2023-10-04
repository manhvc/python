import tkinter as tk
from tkinter import ttk
from src.views.View import View

"""
    View associated with HomeController. It will be responsible for program's 
    main screen view.
"""


class HomeLoginView(tk.Tk, View):
    # -----------------------------------------------------------------------
    #        Constants
    # -----------------------------------------------------------------------
    PAD = 10
    BTN_CAPTION = [
        "Danh Sách Sách Trong Thư Viện",
        "Thêm Sách",
        "Exit"
    ]

    # -----------------------------------------------------------------------
    #        Constructor
    # -----------------------------------------------------------------------
    """
        @param controllers Controller of this view
    """

    def __init__(self, controller):
        super().__init__()
        self.title("Phần mềm quản lý thư viện")
        self.c = controller

        self._make_main_frame()
        self._make_title()
        self._show_login()

    # -----------------------------------------------------------------------
    #        Methods
    # -----------------------------------------------------------------------
    """
        Creates view's frame.
    """

    def _make_main_frame(self):
        self.frame_main = ttk.Frame(self)
        self.frame_main.pack(padx=self.PAD, pady=self.PAD)

    """
        Sets view's title.
    """

    def _make_title(self):
        title = ttk.Label(self.frame_main, text="Đăng Nhập", font=("Helvetica", 20))
        title.pack(padx=self.PAD, pady=self.PAD)

    """
        Creates view's options.
    """

    def _show_login(self):
        frame_btn = ttk.Frame(self.frame_main)
        frame_btn.pack(fill="x")

        frame_book_buttons = tk.Frame(self.frame_main)
        frame_book_buttons.pack()

        lbl = tk.Label(frame_btn, text="Username ")
        lbl.grid(row=0, column=0)
        username = ttk.Entry(frame_btn, width=20)
        username.grid(row=0, column=1)

        btn_submit = ttk.Button(frame_book_buttons, text="Login",
                                command=lambda: self.c.btn_save(username.get()))
        btn_submit.pack(side='right')

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
