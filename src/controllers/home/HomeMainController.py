# -*- encoding:utf-8 -*-
from src.core.Controller import Controller
from src.core.Core import Core

"""
    Main controllers. It will be responsible for program's main screen behavior.
"""


class HomeMainController(Controller):
    # -----------------------------------------------------------------------
    #        Constructor
    # -----------------------------------------------------------------------
    def __init__(self):
        self.home_view = self.load_view("Home", "Main")

    # -----------------------------------------------------------------------
    #        Methods
    # -----------------------------------------------------------------------
    """
        Opens controllers according to the option chosen
    """

    def btn_clicked(self, caption):
        if caption == "Danh Sách Sách Trong Thư Viện":
            c = Core.open_controller("book", "List")
            c.main()
        elif caption == "Thêm Sách":
            c = Core.open_controller("book", "add")
            c.main()

    """
        @Override
    """

    def main(self):
        self.home_view.main()
