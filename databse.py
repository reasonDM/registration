import base64

import psycopg2
from dotenv import dotenv_values

class Reg_ent_func:
    def __init__(self):
        config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}
        self.connection = psycopg2.connect(
            host=config['HOST'],
            database=config['DATABASE'],
            user=config['USER'],
            password=config['PASSWORD'])
        self.regis_cursor = self.connection.cursor()


    # regis_cursor.execute("SELECT * FROM regis_information")
    # print(regis_cursor.fetchall())

    def registration(self, name, phone_number, login, password, repeat_password):
        # Такого логина не существует, что пароли совпадают, зарегистрировать пользователя (добавить в бд), с кодированием пароль
        if not login or not password or not repeat_password or not name or not phone_number:
            raise TypeError("Пустые поля")

        self.regis_cursor.execute(f"SELECT login FROM regis_information WHERE login='{login}'")


        login_res = self.regis_cursor.fetchone()

        if login_res is None and password == repeat_password:
            self.regis_cursor.execute(f"INSERT INTO regis_information(login, password) VALUES('{login}', '{self.encode_password(password)}') RETURNING id")
            regis_id = self.regis_cursor.fetchone()[0]
            self.regis_cursor.execute(f"INSERT INTO personal_information(name, phone_number, regis_id) VALUES('{name}', '{phone_number}', '{regis_id}')")
            self.connection.commit()
        elif login_res is not None:
            raise TypeError("Такой логин уже существует")
        elif password != repeat_password:
            raise TypeError("Пароли не совпадают")


    def enter_account(self, login, password):# если пользователь с такими данными существует, вернуть True, в противном случае False
        self.regis_cursor.execute(f"SELECT login, password FROM regis_information WHERE login='{login}' AND password = '{self.encode_password(password)}'")
        res = self.regis_cursor.fetchone()
        if res is None:
            return False
        else:
            return True

    def check_login_confirm(self, login):
        self.regis_cursor.execute(f"SELECT login FROM regis_information WHERE login='{login}'")
        res = self.regis_cursor.fetchone()
        if res is None:
            return False
        else:
            return True


    def name_login(self, login):
        self.regis_cursor.execute(f"SELECT name FROM personal_information INNER JOIN regis_information ON regis_information.id=personal_information.regis_id WHERE login='{login}'")
        return self.regis_cursor.fetchone()[0]

    def update_pw(self, code, email):
        self.regis_cursor.execute(f"UPDATE regis_information SET password='{self.encode_password(code)}' WHERE login='{email}'")
        self.connection.commit()

    def encode_password(self, password):
        encoded_bytes = base64.b64encode(password.encode('utf-8'))
        encoded_password = encoded_bytes.decode('utf-8')
        return encoded_password
