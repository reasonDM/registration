from PyQt6 import uic


class Window:
    reg = {}

    def __init__(self, path, wind_name, db):
        Form, Windows = uic.loadUiType(path)
        self.windows = Windows()
        self.form = Form()
        self.form.setupUi(self.windows)
        self.db = db
        Window.reg[wind_name] = self


    def open_wind(self):
        self.windows.show()

    def close_wind(self):
        self.windows.hide()