import tkinter as tk
from tkinter import ttk
from src.views.View import View

"""
    View associated with HomeController. It will be responsible for program's 
    main screen view.
"""


class HomeMainView(tk.Tk, View):
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
        self.title("Quản Lý Thư Viện")
        self.homeController = controller

        self._make_main_frame()
        self._make_title()
        self._make_options()

    # -----------------------------------------------------------------------
    #        Methods
    # -----------------------------------------------------------------------
    """
        Creates view's frame.
    """

    def _make_main_frame(self):
        self.mainFrame = ttk.Frame(self)
        self.mainFrame.pack(padx=self.PAD, pady=self.PAD)

    """
        Sets view's title.
    """

    def _make_title(self):
        title = ttk.Label(self.mainFrame, text="Phần mềm quản lý thư viện", font=("Helvetica", 20))
        title.pack(padx=self.PAD, pady=self.PAD)

    """
        Creates view's options.
    """

    def _make_options(self):
        frame_btn = ttk.Frame(self.mainFrame)
        frame_btn.pack(fill="x")

        for caption in self.BTN_CAPTION:
            if caption == "Exit":
                btn = ttk.Button(frame_btn, text=caption, command=self.destroy)
            else:
                btn = ttk.Button(frame_btn, text=caption,
                                 command=lambda txt=caption: self.homeController.btn_clicked(txt))

            btn.pack(fill="x")

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
