from PyQt5 import QtWidgets, uic
import sys
import socket  
import numpy as np
from asyncio import open_connection
from codecs import charmap_build

# Instância de Socket
sc = socket.socket()  

class Ui(QtWidgets.QMainWindow):
    def __init__(self):

        # ---------------- Front-End ---------------- #

        super(Ui, self).__init__()
        uic.loadUi('interface_front-end.ui', self)


        # ---------------- Back-End ----------------- #

        # As funções botaoConectarPressionado e botaoEnviarPressionado determinam
        # quais ações serão tomados quando cada botão for apertado.

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
        ip = self.input1.text()
        print('IP:', ip)
        send= int(self.input2.text())
        print('Porta de envio:', send)
        receive= int(self.input3.text())
        print('Porta de entrada:', receive)  
        sc.connect((ip, send))


    def botaoEnviarPressionado(self):
        posicao = float(self.input4.text())
        print('Posicao:', posicao)
        vel = float(self.input5.text())
        print('Velocidade:', vel)
        torque = float(self.input6.text())
        print('Torque:', torque)
 
        p_enviado = str(posicao)
        v_enviado = str(vel)
        t_enviado= str(torque)

        string = "{} {} {}".format(p_enviado, v_enviado, t_enviado)
        sc.send(string.encode())

        # Exibição do Estado Atual
        msg = sc.recv(1024)
        msg_recebida = msg.decode()
        split_msg= msg_recebida.split(" ", 2)
        self.output1.setText(split_msg[0])
        self.output1.setText(split_msg[1])
        self.output1.setText(split_msg[2])
   
   
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()