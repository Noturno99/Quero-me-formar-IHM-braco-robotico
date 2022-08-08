from PyQt5 import QtWidgets, uic
import sys
import socket  

# Instância de Socket
sc = socket.socket()  

class Ui(QtWidgets.QMainWindow):
    def __init__(self):

        # ---------------- Front-End ---------------- #

        super(Ui, self).__init__()
        uic.loadUi('interface_front-end.ui', self) # Carrega o arquivo de front-end .ui gerado no Qt Designer


        # ---------------- Back-End ----------------- #

        # As funções botaoConectarPressionado e botaoEnviarPressionado determinam
        # quais ações serão tomados quando cada botão for apertado.

        # Inputs - seção "Conexão"
        # Nomeia as entradas de conexão com a Toradex 
        self.input1 = self.findChild(QtWidgets.QLineEdit, 'line_IP')
        self.input2 = self.findChild(QtWidgets.QLineEdit, 'line_Entrada')
        self.input3 = self.findChild(QtWidgets.QLineEdit, 'line_Envio')

        # Botão Conectar
        self.botao1 = self.findChild(QtWidgets.QPushButton, 'botao_Conectar') 
        self.botao1.clicked.connect(self.botaoConectarPressionado) # Chama a função botaoConectarPressionado
                                                                   # assim que o botão Conectar é apertado
        

        # Inputs - seção "Entrada"
        # Nomeia as entradas de estado do robô 
        self.input4 = self.findChild(QtWidgets.QLineEdit, 'line_Posicao') 
        self.input5 = self.findChild(QtWidgets.QLineEdit, 'line_Vel')
        self.input6 = self.findChild(QtWidgets.QLineEdit, 'line_Torque')

        # Botão Enviar
        self.botao2 = self.findChild(QtWidgets.QPushButton, 'botao_Enviar')
        self.botao2.clicked.connect(self.botaoEnviarPressionado) # Chama a função botaoEnviarPressionado
                                                                 # assim que o botão Enviar é apertado


        # Outputs - seção "Estado Atual"
        # Nomeia as saídas de Estado Atual 
        self.output1 = self.findChild(QtWidgets.QLabel, 'label_Posicao')
        self.output2 = self.findChild(QtWidgets.QLabel, 'label_Vel')
        self.output3 = self.findChild(QtWidgets.QLabel, 'label_Torque')

        self.show()


    def botaoConectarPressionado(self):
        # Printa no terminal as entradas do usuário para conexão
        ip = self.input1.text()
        print('IP:', ip)
        send = int(self.input2.text())
        print('Porta de envio:', send)
        receive = int(self.input3.text())
        print('Porta de entrada:', receive)  
        
        # Estabelece a conexão Socket com os dados de IP e porta de envio
        sc.connect((ip, send))


    def botaoEnviarPressionado(self):
        # Printa no terminal as entradas do usuário para estado do robô
        posicao = float(self.input4.text())
        print('Posicao:', posicao)
        vel = float(self.input5.text())
        print('Velocidade:', vel)
        torque = float(self.input6.text())
        print('Torque:', torque)
 
        p_enviado = str(posicao)
        v_enviado = str(vel)
        t_enviado= str(torque)
        
        # Gera uma string com as três informações de estado e a envia via Socket
        string = "{} {} {}".format(p_enviado, v_enviado, t_enviado)
        sc.send(string.encode())

        msg = sc.recv(1024)
        msg_recebida = msg.decode() # Lê a mensagem enviada
        split_msg = msg_recebida.split(" ", 2) # Separa as informações de estado da string
        
        # Exibe na interface o estado atual
        self.output1.setText(split_msg[0])
        self.output2.setText(split_msg[1])
        self.output3.setText(split_msg[2])
   
   
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
