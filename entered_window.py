from reg.windows import Window


class Entered_window(Window):
    def __init__(self, path, wind_name, db):
        super().__init__(path, wind_name, db)
        self.form.exit_button.clicked.connect(self.exit_entered_window)

    def exit_entered_window(self):
        self.close_wind()
        Window.reg['enter'].open_wind()

    def open_wind(self, login):
        self.form.label.setText(self.db.name_login(login))
        self.windows.show()
