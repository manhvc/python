from core.Core import Core

"""
    Main class. Responsible for running the application.
"""


class Main:
    @staticmethod
    def run():
        try:
            app = Core.open_controller("home", "login")
            app.main()
        except Exception as e:
            print(str(e))


if __name__ == '__main__':
    Main.run()
