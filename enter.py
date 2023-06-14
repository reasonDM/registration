from PyQt6.QtWidgets import QMessageBox

from reg.windows import Window



class Enter(Window):
    def __init__(self, path, wind_name, db):
        super().__init__(path, wind_name, db)
        self.form.enter_button.clicked.connect(self.open_enter_wind)
        self.form.regis_enter_button.clicked.connect(self.open_reg)
        self.form.forgot_button.clicked.connect(self.forgot)


    def open_enter_wind(self):
        login = self.form.login_edit.text()
        password = self.form.password_edit.text()
        result = self.db.enter_account(login, password)
        if result is True:
            self.close_wind()
            Window.reg['entered_window'].open_wind(login)
            self.form.login_edit.clear()
            self.form.password_edit.clear()



        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setText("Неверный логин или пароль")
            msg.exec()

    def open_reg(self):
        self.close_wind()
        Window.reg['registration'].open_wind()


    def forgot(self):
        self.close_wind()
        Window.reg['forgot_window'].open_wind()


