import importlib
import os

from src.Config import APP_PATH

"""
    Class responsible for opening controllers
"""


class Core:
    # -----------------------------------------------------------------------
    #        Methods
    # -----------------------------------------------------------------------
    """
        Given a controllers name, return an instance of it

        @param controllers:string Controller to be opened
    """

    @staticmethod
    def open_controller(controller, action):
        response = None

        # Set controllers name
        controller = controller[0].upper() + controller[1:]

        c_src = (controller.lower() + "." + controller[0].upper() + controller[1:] +
                 action[0].upper() + action[1:] + "Controller")
        c_path = (controller.lower() + "/" + controller[0].upper() + controller[1:] +
                  action[0].upper() + action[1:] + "Controller")
        c_name = controller[0].upper() + controller[1:] + action[0].upper() + action[1:] + "Controller"
        # Check if file exists
        if os.path.exists(APP_PATH + "/controllers/" + c_path + ".py"):
            module = importlib.import_module("controllers." + c_src)
            class_ = getattr(module, c_name)
            response = class_()

        return response
