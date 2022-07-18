# Quero-me-formar-IHM-braco-robotico
Trabalho final da disciplina de Sistemas Embarcados (SEM0544) - 2022.1.

Projeto 5: Interface Homem-Máquina para braço robótico de reabilitação.

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
Essa etapa envolve a criação de uma interface por meio da qual o usuário digitará dados de comunicação e de controle dos motores, para que sejam enviados ao microcontrolador. Ademais, o estado atual do braço robótico deve ser exibido na janela. Sendo assim, dividiu-se a interface em três seções - Conexão, Entrada e Estado Atual -, conforme a imagem abaixo mostra.

![image](https://user-images.githubusercontent.com/70723135/179436185-bd050a5f-a298-4779-9335-bf4dbbe70f47.png)


### Back-End


### Comunicação do Host com a Toradex
