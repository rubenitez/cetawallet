import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget, QWidget
import sqlite3


class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("welcomescreen.ui", self)
        self.login.clicked.connect(self.gotologin)

    def gotologin(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)


class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("login.ui", self)
        # Put bullets to passwordfield
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login.clicked.connect(self.loginfunction)

    def loginfunction(self):
        user = self.emailfield.text()
        password = self.passwordfield.text()

        if len(user) == 0 or len(password) == 0:
            self.error.setText("Please input all fields.")
        else:
            conn = sqlite3.connect("shop_data.db")
            cur = conn.cursor()

            # query1 = 'SELECT username FROM login_info WHERE username = \'' + user + "\'"
            # cur.execute(query1)
            # result_user = cur.fetchone()[0]
            # if result_user == user:
            #     print("Successfully logged in.")
            #     self.error.setText("")
            # else:
            #     self.error.setText("Invalid username or password.")

            query1 = 'SELECT username FROM login_info WHERE username = \'' + user + "\'"
            cur.execute(query1)
            result_user = cur.fetchone()
            print (result_user)
            query2 = 'SELECT password FROM login_info WHERE username = \'' + user + "\'"
            cur.execute(query2)
            result_pass = cur.fetchone()
            print (result_pass)
            # if result_user == user and result_pass == password:
            #     print("Successfully logged in.")
            #     self.error.setText("")
            # elif result_user != user and result_pass == password:
            #     self.error.setText("Invalid username")
            # else:
            #     self.error.setText("Invalid password.")


# main
app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
try:
    sys.exit(app.exec())
except:
    print("Exiting")
