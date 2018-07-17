# python
Assignment programs

import sys
import socket
import paramiko
import time
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize,QRegExp
from PyQt5.QtGui import QRegExpValidator

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # creating main window sige
        self.setMinimumSize(QSize(300, 300))    
        self.setWindowTitle("$ Putty $") 
        # creating label with text box
        self.IPLabel = QLabel(self)
        self.IPLabel.setText('IP ADRESS:')
        self.IPAdress = QLineEdit(self)
        self.IPAdress.move(80, 20)
        self.IPAdress.resize(200, 32)
        self.IPLabel.move(15, 20)        
        # creating label with text box
        self.UserLabel = QLabel(self)
        self.UserLabel.setText('USER NMAE:')
        self.UserNmae = QLineEdit(self)
        self.UserNmae.move(80, 60)
        self.UserNmae.resize(200, 32)
        self.UserLabel.move(15, 60)
        # creating label with text box  
        self.PasswordLabel = QLabel(self)
        self.PasswordLabel.setText('PASSWORD:')
        self.Password = QLineEdit(self)
        self.Password.move(80, 100)
        self.Password.resize(200, 32)
        self.PasswordLabel.move(15, 100)
        # creating button with login name
        self.button = QPushButton('Login', self)
        self.button.move(80,250)
        self.button.resize(100,32)
        # connect button to function on_click
        self.button.clicked.connect(self.clickMethod)
        self.show()
    
    def connect_linux_system(self,ip_adress,user_name,password):
        #usd to connect to linux system
        try:
            ssh_pre = paramiko.SSHClient()
            ssh_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_pre.connect(ip_adress, username=user_name, password=password)
            time.sleep(10)
            (stdin, stdout, stderr) = ssh_pre.exec_command('free -m')
            print(stdout.read())
        except Exception as e:
            print ('entered input details wrong or check network connection')
        except Exception as e:
            print ('Error'+str(e))
                
    def clickMethod(self):
        ip_adress = self.IPAdress.text()
        
        #Checking the ip adress is valid or not
        try: 
            socket.inet_aton(ip_adress)
            print('IP ADRESS =',ip_adress)
            #connecting to the linux system
            #self.connect_linux_system(ip_adress,user_name,password)
            
        except:
            print('IP Adress Wrong')
        
        user_name=self.UserNmae.text()
        password=self.Password.text()
        print('USER NAME =',user_name)
        print('PASSWORD =',password)
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
