# Motor Monitoring

MotorMonitoring é uma aplicação de monitoramento de motores que lê, transmite e exibe em tempo real dados como corrente e tensão do motor em um dashboard web. O objetivo da ferramenta é permitir que gestores e responsáveis pela manutenção possam identificar rapidamente falhas e problemas no motor, facilitando a tomada de decisões e garantindo a disponibilidade e eficiência do equipamento. 


## Arquitetura

O projeto é dividido em três subsistemas:

- **[Dashboard](https://github.com/RafaelChavesPB/MotorMonitoring/tree/master/dashboard)**: responsável por exibir os dados em tempo real.
- **[Server](https://github.com/RafaelChavesPB/MotorMonitoring/tree/master/server)**: Fica responsável por receber os dados do sistema embarcado e envia-los em tempo real ao dashboard. Também é responsável por armazenar os dados recebidos em um banco de dados.
- **[Embedded](#)**: Sitema embarcado responsável por fazer as medições nos motores e enviar os valores ao server.

Dessa forma, o MotorMonitoring funciona como um sistema integrado que coleta, armazena e apresenta informações em tempo real sobre o desempenho dos motores monitorados.

## Inicializando

Para inicializar o MotorMonitoring você pode iniciar cada subsistema individualmente, as instruções estão descritas nos respctivos diretorios. Ou utilizar Docker e Docker-compose para subir uma stack contendo o Dashboard e o Server.

Para isso é necessário instalar o [docker](https://docs.docker.com/engine/install/ubuntu/) e o plugin para o [docker-compose](https://docs.docker.com/compose/install/linux/). Para executar o docker sem a necessidade de utilizar **sudo** ou acessar como usuário raiz, siga os seguintes passos do [Docker postinstall](https://docs.docker.com/engine/install/linux-postinstall/).

Agora que você já está com todas as ferramentas em mãos, basta entrar no diretorio raiz do projeto e executar o seguinte comando:

```bash
docker compose up --build
```

Caso nenhuma mensagem de erro apareça o server já está conectado ao dashboard e aguarda os dados que devem ser enviados pelos o sistema embarcado.


<div align="center">

| Serviço | Host | Porta |
|:--------:|:--------:|:--------:|
| Dashboard | Ip, Localhost, 127.0.0.1, 0.0.0.0 | 8080 |
| Server | Ip, Localhost, 127.0.0.1, 0.0.0.0 | 5000 |

</div>