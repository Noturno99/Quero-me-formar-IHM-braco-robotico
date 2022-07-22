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
    int port = 5560;
    // Buffer para receber e enviar mensagens
    char msg[1500];
     
    // Criação do socket server
    sockaddr_in servAddr;
    bzero((char*)&servAddr, sizeof(servAddr));
    servAddr.sin_family = AF_INET;
    servAddr.sin_addr.s_addr = htonl(INADDR_ANY);
    servAddr.sin_port = htons(port);
 
    int serverSd = socket(AF_INET, SOCK_STREAM, 0);
    if(serverSd < 0)
    {
        printf("\n Erro em inicializar o socket server. \n");
        exit(0);
    }

    int bindStatus = bind(serverSd, (struct sockaddr*) &servAddr, sizeof(servAddr));
    if(bindStatus < 0)
    {
        printf("\n Erro no building do socket no endereço local. \n");
        exit(0);
    }

    printf("\n Esperando o client para conectar. \n");
    listen(serverSd, 5);

    sockaddr_in newSockAddr;
    socklen_t newSockAddrSize = sizeof(newSockAddr);

    int newSd = accept(serverSd, (sockaddr *)&newSockAddr, &newSockAddrSize);
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
        memset(&msg, 0, sizeof(msg));
        bytesLeitura += recv(newSd, (char*)&msg, sizeof(msg), 0);
        if(!strcmp(msg, "exit"))
        {
            printf("\n Client saiu da sessão...\n" );
            break;
        }
        printf("\n Posição, velocidade, torque: %s \n", msg);
        bytesEscrita += send(newSd, (char*)&msg, strlen(msg), 0);
    }

    // Fechar sockets
    close(newSd);
    close(serverSd);
    printf("\n Conexão interrompida... \n");
    return 0;   
}