/*
Created on Thurs. Jul 14 2022

@author: Pedro Antonio Calorio Gutierres
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <netdb.h>

using namespace std;

int main(int argc, char *argv[])
{
    int port = 5560; // Porta que o usuário deve digitar para realizar a conexão
    char msg[1500]; // Buffer para receber e enviar mensagens
     
    // Criação do socket server
    sockaddr_in servAddr;
    bzero((char*)&servAddr, sizeof(servAddr)); // Zera a região de memória
    servAddr.sin_family = AF_INET; // AF_INET = Adress family IPv4, que designa o tipo de endereço com o qual o socket poderá se comunicar
    servAddr.sin_addr.s_addr = htonl(INADDR_ANY); // Converte a ordem de byte do host para a ordem de byte do network, com comprimento do dado sendo long
    servAddr.sin_port = htons(port); // Converte a ordem de byte do host para a ordem de byte do network, com comprimento do dado sendo short
    int serverSd = socket(AF_INET, SOCK_STREAM, 0); // SOCK_STREAM = tipo de protocolo TCP/IP
    if(serverSd < 0)
    {
        printf("\n Erro em inicializar o socket server. \n");
        exit(0);
    }

    int bindStatus = bind(serverSd, (struct sockaddr*) &servAddr, sizeof(servAddr)); // Associa a porta (local adress) com o socket server
    if(bindStatus < 0)
    {
        printf("\n Erro no building do socket no endereço local. \n");
        exit(0);
    }

    printf("\n Esperando o client para conectar. \n");
    listen(serverSd, 5); // Anuncia que o server está disposto a aceitar conexões

    // Criação de um socket para receber as mensagens do client
    sockaddr_in newSockAddr;
    socklen_t newSockAddrSize = sizeof(newSockAddr);
    int newSd = accept(serverSd, (sockaddr *)&newSockAddr, &newSockAddrSize); // Estabelece uma conexão de entrada
    if(newSd < 0)
    {
        printf("\n Erro no client aceitar o convite. \n" );
        exit(1);
    }

    printf( "\n Conexão estabelecida com o client! \n");
   
    int bytesLeitura, bytesEscrita = 0;

    // Loop para receber mensagens do client
    while(1)
    {
        printf("\n Esperando mensagem do client... \n");
        memset(&msg, 0, sizeof(msg)); // Lê a mensagem do client
        bytesLeitura += recv(newSd, (char*)&msg, sizeof(msg), 0);
        if(!strcmp(msg, "exit")) // Confere se a comunicação foi encerrada pelo client
        {
            printf("\n Client saiu da sessão...\n" );
            break;
        }
        printf("\n Posição, velocidade, torque: %s \n", msg); // Printa os dados lidos
        bytesEscrita += send(newSd, (char*)&msg, strlen(msg), 0);
    }

    // Encerra sockets
    close(newSd);
    close(serverSd);
    printf("\n Conexão interrompida... \n");
    return 0;   
}
