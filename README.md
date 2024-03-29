# Quero-me-formar-IHM-braco-robotico
Trabalho final da disciplina de Sistemas Embarcados (SEM0544) - 2022.1.

Projeto 5: Interface Humano-Máquina para braço robótico de reabilitação.

Grupo: Quero Me Formar

Membros:
- Gabriel Corrêa de Oliveira - nº 10747270
- Yuri Campagnari Ramos - nº 10788568
- Pedro Antonio Calorio Gutierres - nº 10746856

## Objetivo
O intuito desse projeto é desenvolver uma interface capaz de enviar e exibir sinais de posição, torque e velocidade para um microcontrolador Toradex que, por sua vez, estará controlando os motores de um braço robótico de reabilitação. A ideia é a interface assim como a recepção e o envio de dados de entrada rodarem em um computador (host) com sistema operacional Linux.

Dito isso, podemos dividir o projeto em três etapas: Front-End, Back-End e Comunicação Host-Toradex.

## Desenvolvimento

### Front-End
Essa etapa envolve a criação de uma interface por meio da qual o usuário digitará dados de comunicação e de controle dos motores do braço robótico, para que sejam enviados ao microcontrolador. Ademais, o estado atual do robô deve ser exibido na janela. Sendo assim, dividiu-se a interface em três seções - Conexão, Entrada e Estado Atual -, conforme a imagem abaixo mostra.

![image](https://user-images.githubusercontent.com/70723135/179436185-bd050a5f-a298-4779-9335-bf4dbbe70f47.png)

No que diz respeito às ferramentas para o desenvolvimento da interface, utilizou-se o Qt Designer, um software que facilita a utilização do framework Qt. O arquivo resultante, que corresponde ao Front-End, possui a extensão .ui.

### Back-End
Feito o Front-End, é necessário implementar recepção, interpretação e envio dos dados fornecidos pelo usuário, isto é, executar as ações necessárias quando são digitados os valores desejados nos campos em branco e os botões são pressionados.

Para elaboração da lógica de Back-End, também foi utilizado o framework Qt, no entanto a versão para linguagem Python, a PyQt. O arquivo .py presente no diretório IHM realiza a leitura do arquivo .ui da etapa anterior e promove a interação do usuário com os componentes da interface. Abaixo está uma parte do código que exemplifica como isso é feito:

```python
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
```

### Comunicação do Host com a Toradex
Por fim, para estabelecer a comunicação entre o host e a Toradex, utilizou-se protocolo TCP-IP e Sockets nos quais o client foi implementado em Python no computador e o server, em C++ no microcontrolador. Em Python, o módulos utilizado foi *socket*, que fornece uma interface para conexões de baixo nível. Fez-se necessário, por outro lado, usar os headers *sys/socket.h*, *netinet/in.h* e *netdb.h* em C++. 

Para tanto, inicialmente a Toolchain da Toradex Colibri VF50 foi configurada e o arquivo .cpp do server compilado e enviado para o microcontrolador pelo terminal, conforme as práticas realizadas na disciplina:

<img src="https://user-images.githubusercontent.com/70723135/180578877-00d2f8aa-ac33-4e4d-a3ca-0de27b20c5a2.png" width="525">

Em seguida, navegou-se pelos arquivos da Toradex em outro terminal e executou-se o arquivo compilado:

<img src="https://user-images.githubusercontent.com/70723135/180579743-4f9d436f-fd68-4498-b3ff-eee5353bc941.png" width="525">

O arquivo .py da interface e do client, então, é executado no host, faltando apenas enviar os dados necessários para estabelecer a comunicação:

<img src="https://user-images.githubusercontent.com/70723135/180579878-b2cfe99f-adc8-4b7c-b42f-2556e1ed39a6.png" width="">

## Resultados

Portanto, com todo esse procedimento realizado, os dados de posição, velocidade e torque dos motores são enviados na seção de Entrada da IHM, sendo mostrados na seção Estado Atual. Segue um exemplo dos campos da interface preenchidos e outro da confirmação da conexão estabelecida e do recebimento desses dados no terminal que está navegando na Toradex, respectivamente:

<img src="https://user-images.githubusercontent.com/70723135/180580492-b5848b8e-d888-4ca1-9ef0-28a392446b1d.png" width="700">

<img src="https://user-images.githubusercontent.com/70723135/180580526-c891928b-feaf-479b-8b64-25ada602a731.png" width="525">

