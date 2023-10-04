# -*- encoding:utf-8 -*-
from src.core.Controller import Controller
from src.core.Core import Core

"""
    Main controllers. It will be responsible for program's main screen behavior.
"""


class HomeLoginController(Controller):
    # -----------------------------------------------------------------------
    #        Constructor
    # -----------------------------------------------------------------------
    def __init__(self):
        self.login_view = self.load_view("Home", "Login")

    # -----------------------------------------------------------------------
    #        Methods
    # -----------------------------------------------------------------------

    """
        @Override
    """

    def main(self):
        self.login_view.main()
