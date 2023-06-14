from PyQt6.QtWidgets import QMessageBox

from reg.windows import Window


class Registration(Window):
    def __init__(self, path, wind_name, db):
        super().__init__(path, wind_name, db)
        self.form.regis_button.clicked.connect(self.reg_all)

    def reg_all(self):

        login = self.form.regis_login_edit.text()
        password = self.form.regis_pw_edit.text()
        rep_password = self.form.regis_pwr_edit.text()
        name = self.form.regis_name_edit.text()
        phone_num = self.form.regis_pn_edit.text()
        try:
            self.db.registration(login = login, password = password, repeat_password = rep_password, name = name, phone_number=phone_num)
            self.close_wind()
            Window.reg['entered_window'].open_wind(login)
            self.form.regis_login_edit.clear()
            self.form.regis_pw_edit.clear()
            self.form.regis_pwr_edit.clear()
            self.form.regis_name_edit.clear()
            self.form.regis_pn_edit.clear()

        except TypeError as te:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setText(str(te))
            msg.exec()




