import sys
import json
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QMainWindow


class MyWindow(QMainWindow): 
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()

    

    def initUI(self):
        self.setGeometry(200,200,500,300) 
        self.setWindowTitle("Login") 
        
        #username 
        self.username_label = QLabel(self)
        self.username_label.setText("Username")
        self.username_label.move(50, 50) 

        self.username_text = QLineEdit('', self)
        #username_text.dragEnabled(True)
        self.username_text.move(100, 50)


        #Password 
        self.pass_label = QLabel(self)
        self.pass_label.setText("Password")
        self.pass_label.move(50, 100)

        self.pass_text = QLineEdit('', self)
        #pass_text.dragEnabled(False)
        self.pass_text.move(100, 100)

        #login button 
        
        self.login_button = QtWidgets.QPushButton(self)
        self.login_button.setText("login") 
        self.login_button.move(200, 200)
        self.login_button.clicked.connect(self.button_clicked)

        '''
        login_button = Button('&login', self)
        login_button.move(200, 200)
        login_button.
        login_button.clicked.connect(self.button_clicked)
        '''
    def button_clicked(self):
        '''
        next task: put them in a json file not in .txt 
        '''
        print("clicked")
        username = self.username_text.text()
        password = self.pass_text.text()
        dictionary = {'username': username, 'password': [password]}
        json_object = json.dumps(dictionary, indent=4)
        with open("pass.json", "w") as outfile:
            outfile.write(json_object)

        '''
        f = open("Password.txt", "w")
        f.write(str({'username', username}))
        f.write(str({'password', password}))
        f .close()
        '''


def main():
    app = QApplication(sys.argv)
    window = MyWindow() #object of the class
    window.show()
    sys.exit(app.exec_())

main()