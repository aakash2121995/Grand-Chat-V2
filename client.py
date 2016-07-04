from PyQt4 import QtGui,QtCore # Import the PyQt4 module we'll need
import sys # We need sys so that we can pass argv to QApplication

import design # This file holds our MainWindow and all design related things
              # it also keeps events etc that we defined in Qt Designer
import socket
import threading
import time
import argparse


def getHostname():
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.connect(("gmail.com",80))
    myIp = s.getsockname()[0]
    s.close()
    return myIp

def getServerIp():
    parser = argparse.ArgumentParser()
    parser.add_argument("server_Ip",help="IP address of the Chat server you want to use", type = str)
    args = parser.parse_args()
    return args.server_Ip

class ExampleApp(QtGui.QMainWindow, design.Ui_MainWindow):

    def receiving(self):
        while not self.shutdown:
            try:
                while True:
                    data, addr = self.socket.recvfrom(1024)
                    #print data
                    msg = str(data)
                    self.ChatWindow.append(msg)
                    self.ChatWindow.append("")
            except :
                pass
    def end(self):
        self.socket.sendto("** " + self.name + " joined **",self.server)
        self.shutdown = True
        self.rT.join()
        self.socket.close()
    def sendMessage(self):
        userMessage = str(self.message.displayText())
        if not userMessage:
            return 
        userMessage = self.name + ": " + userMessage
        self.message.clear()
        # print (userMessage)
        self.socket.sendto(userMessage,self.server)
        self.ChatWindow.append(userMessage)
        self.ChatWindow.append("")
        #print(userMessage)
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            self.send.click()         

    def __init__(self,s,alias,server):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
                            # It sets up layout and widgets that are defined
        self.socket = s
        self.name = alias
        self.server = server
        self.send.clicked.connect(self.sendMessage)
        self.shutdown = False
        self.rT = threading.Thread(target=self.receiving,args=())
        self.rT.start()

        s.sendto("** " + alias + " joined **",self.server)

def main():

    server = (getServerIp(),5000)
    host = getHostname()
    port = 0

    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind((host,port))
    s.setblocking(0)

    alias = raw_input("Enter name: ")

    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp(s,alias,server)                 # We set the form to be our ExampleApp (design)
    form.show()                         # Show the form
    app.exec_()                         # and execute the app
    form.end()

if __name__ == '__main__':              # if we're running file directly and not importing it
    main()  