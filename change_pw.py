import random
import smtplib

from PyQt6.QtWidgets import QMessageBox

from reg.windows import Window


class Change_pw(Window):

    def __init__(self, path, wind_name, db):
        super().__init__(path, wind_name, db)
        self.form.commit_button.clicked.connect(self.check_code)

    def open_wind(self, code, email):
        self.code = code
        self.email = email
        self.windows.show()

    def check_code(self):
        code = self.form.code_edit.text()
        new_pw = self.form.new_pw_edit.text()
        if int(code) == self.code and new_pw is not None:
            self.db.update_pw(new_pw, self.email)
            self.close_wind()
            Window.reg['enter'].open_wind()
        elif code != self.code:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setText("Неверный код")
            msg.exec()
        elif new_pw is None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setText("Введите пароль")
            msg.exec()







