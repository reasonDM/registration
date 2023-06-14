import random
import smtplib

from reg.windows import Window
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from PyQt6.QtWidgets import QMessageBox

class Forgot(Window):

    def __init__(self, path, wind_name, db):
        super().__init__(path, wind_name, db)
        self.form.forgot_enter_button.clicked.connect(self.comfirm)

    def comfirm(self):
        '''

        :return: entering the login or mail for confirm
        '''

        corfirm_res = self.form.forgot_edit.text()
        result_confirm = self.db.check_login_confirm(corfirm_res)
        if result_confirm is True:
            # Параметры подключения к SMTP-серверу
            smtp_server = 'smtp.bk.ru'  # Укажите адрес SMTP-сервера
            smtp_port = 587  # Укажите порт SMTP-сервера
            smtp_username = 'dorjkhuu@bk.ru'  # Укажите вашу почту
            smtp_password = 'Umk0pYykGspEaYszXyuj'  # Укажите ваш пароль

            # Создание MIME-сообщения
            msg = MIMEMultipart()
            msg['From'] = 'dorjkhuu@bk.ru'  # Укажите адрес отправителя
            msg['To'] = f'{corfirm_res}'  # Укажите адрес получателя
            msg['Subject'] = 'Код для обновления пароля'  # Укажите тему сообщения

            # Добавление текстовой части сообщения
            rand_code = random.randint(100000, 999999)
            text = f'Введите этот код {rand_code} для сброса старого пароля и создания нового.'

            msg.attach(MIMEText(text, 'plain'))

            # Отправка сообщения через SMTP-сервер
            try:
                with smtplib.SMTP(smtp_server, smtp_port) as server:
                    server.starttls()
                    server.login(smtp_username, smtp_password)
                    server.send_message(msg)
                print('Сообщение успешно отправлено!')
                self.close_wind()
                Window.reg['change_password_window'].open_wind(rand_code, corfirm_res)
            except Exception as e:
                print('Ошибка при отправке сообщения:', str(e))

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setText("Такой почты нет")
            msg.exec()