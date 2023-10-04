import abc
import importlib
import os

from src.Config import APP_PATH

"""
    Responsible for the communication between views and models in addiction to
    being responsible for the behavior of the program.
"""


class Controller(metaclass=abc.ABCMeta):
    # -----------------------------------------------------------------------
    #        Methods
    # -----------------------------------------------------------------------
    """
        Executes controllers and associated view with it.
    """

    @abc.abstractmethod
    def main(self):
        return

    """
        Given a view name, return an instance of it

        @param viewName:string View to be opened
    """

    def load_view(self, view_name, view_action):
        response = None

        # Set view name
        view_src = (view_name.lower() + "." + view_name[0].upper() + view_name[1:] +
                    view_action[0].upper() + view_action[1:] + "View")
        view_path = (view_name.lower() + "/" + view_name[0].upper() + view_name[1:] +
                     view_action[0].upper() + view_action[1:] + "View")
        view_name = view_name[0].upper() + view_name[1:] + view_action[0].upper() + view_action[1:] + "View"
        # Check if file exists
        if os.path.exists(APP_PATH + "/views/" + view_path + ".py"):
            module = importlib.import_module("views." + view_src)
            class_ = getattr(module, view_name)
            response = class_(self)

        return response
