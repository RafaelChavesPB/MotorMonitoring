# Motor Monitoring

MotorMonitoring é uma aplicação de monitoramento de motores que lê, transmite e exibe em tempo real dados como corrente e tensão do motor em um dashboard web. O objetivo da ferramenta é permitir que gestores e responsáveis pela manutenção possam identificar rapidamente falhas e problemas no motor, facilitando a tomada de decisões e garantindo a disponibilidade e eficiência do equipamento. 


## Arquitetura

O projeto é dividido em três subsistemas:

- **[Dashboard](https://github.com/RafaelChavesPB/MotorMonitoring/tree/master/dashboard)**: responsável por exibir os dados em tempo real.
- **[Server](https://github.com/RafaelChavesPB/MotorMonitoring/tree/master/server)**: Fica responsável por receber os dados do sistema embarcado e envia-los em tempo real ao dashboard. Também é responsável por armazenar os dados recebidos em um banco de dados.
- **[Embedded](https://github.com/RafaelChavesPB/MotorMonitoring/tree/master/embedded)**: Sitema embarcado responsável por fazer as medições nos motores e enviar os valores ao server.

Dessa forma, o MotorMonitoring funciona como um sistema integrado que coleta, armazena e apresenta informações em tempo real sobre o desempenho dos motores monitorados.