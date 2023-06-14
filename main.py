from PyQt6.QtWidgets import QApplication

from reg.change_pw import Change_pw
from reg.databse import Reg_ent_func
from reg.enter import Enter
from reg.entered_window import Entered_window
from reg.forgot import Forgot
from reg.registration import Registration

win = QApplication([])
regis = Reg_ent_func()
enter_window_open = Enter('enter.ui', 'enter', regis)
enter_window_open.open_wind()
entered_window_open = Entered_window('ent.ui', 'entered_window', regis)
regis_window_open = Registration('regis.ui', 'registration', regis)
forgot_window_open = Forgot('forgot.ui', 'forgot_window', regis)
change_pw_open = Change_pw('new_pw.ui', 'change_password_window', regis)

win.exec()
