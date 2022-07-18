from PyQt5 import QtWidgets, uic
import sys
import socket  
import numpy as np
from asyncio import open_connection
from codecs import charmap_build

# Instância de Socket
s = socket.socket()  

message =np.uint8([1,2,3])


class Ui(QtWidgets.QMainWindow):
    def __init__(self):

        # ---------------- Front-End ---------------- #

        super(Ui, self).__init__()
        uic.loadUi('interface_front-end.ui', self)


        # ---------------- Back-End ----------------- #

        # Inputs - seção "Conexão"
        self.input1 = self.findChild(QtWidgets.QLineEdit, 'line_IP')
        self.input2 = self.findChild(QtWidgets.QLineEdit, 'line_Entrada')
        self.input3 = self.findChild(QtWidgets.QLineEdit, 'line_Envio')

        # Botão Conectar
        self.botao1 = self.findChild(QtWidgets.QPushButton, 'botao_Conectar') 
        self.botao1.clicked.connect(self.botaoConectarPressionado)
        

        # Inputs - seção "Entrada"
        self.input4 = self.findChild(QtWidgets.QLineEdit, 'line_Posicao')
        self.input5 = self.findChild(QtWidgets.QLineEdit, 'line_Vel')
        self.input6 = self.findChild(QtWidgets.QLineEdit, 'line_Torque')

        # Botão Enviar
        self.botao2 = self.findChild(QtWidgets.QPushButton, 'botao_Enviar')
        self.botao2.clicked.connect(self.botaoEnviarPressionado)


        # Outputs - seção "Estado Atual"
        self.output1 = self.findChild(QtWidgets.QLabel, 'label_Posicao')
        self.output2 = self.findChild(QtWidgets.QLabel, 'label_Vel')
        self.output3 = self.findChild(QtWidgets.QLabel, 'label_Torque')

        self.show()


    def botaoConectarPressionado(self):
        ip_text = self.input1.text()
        print('IP:', ip_text)
        port_send= int(self.input2.text())
        print('Porta de envio:', port_send)
        port_receive= int(self.input3.text())
        print('Porta de entrada:', port_receive)
        port = port_send   
        s.connect((ip_text, port))


    def botaoEnviarPressionado(self):
        posicao = float(self.input4.text())
        print('Posicao:', posicao)
        vel = float(self.input5.text())
        print('Velocidade:', vel)
        torque = float(self.input6.text())
        print('Torque:', torque)
 
        posicao_send = str(posicao)
        vel_send = str(vel)
        torque_send= str(torque)

        string = "{} {} {}".format(posicao_send, vel_send, torque_send)
        s.send(string.encode())

        # Exibição do Estado Atual
        msg = s.recv(1024)
        received_msg = msg.decode()
        split_msg= received_msg.split(" ", 2)
        self.output1.setText(split_msg[0])
        self.output1.setText(split_msg[1])
        self.output1.setText(split_msg[2])
   
   
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()