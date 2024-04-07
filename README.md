# Dados de Dengue em Belo Horizonte por Semana Epidemiológica - v.01

## Conteúdo
1. [Descrição do Projeto](#descricao-do-projeto)
2. [Descrição dos Arquivos](#descricao-dos-arquivos)
3. [Benefícios do Projeto](#beneficios-do-projeto)
4. [Licenças e Autores](#licencas-e-autores)

## Descrição do Projeto
Em 2024, a dengue continua a ser uma preocupação de saúde pública em várias regiões do mundo, especialmente em países tropicais e subtropicais. A doença é causada pelo vírus da dengue, transmitido pela picada do mosquito Aedes aegypti. Apesar dos esforços de controle e prevenção, a dengue persiste como um desafio devido à sua natureza sazonal e à dificuldade de controlar a população de mosquitos vetores. Estratégias de combate incluem o uso de inseticidas, eliminação de criadouros de mosquitos e campanhas de conscientização pública sobre medidas de prevenção, como o uso de repelentes e a eliminação de recipientes que acumulem água parada. Esse projeto visa coletar os dados os casos de dengue em Belo Horizonte/MG em 2024, por semana epidemiológica. O projeto tem as seguintes etapas:
- Coleta dos Dados: Coleta dos dados usando a API do INFODengue.
- Armazenamento dos Dados: Armazenamento dos dados particionados por dia no S3 bucket.
- Automatização Semanal: Automação semanal da coleta dos dados via Amazon CloudWatch.

A orquestração deste projeto envolve o agendamento semanal das funções lambda usando o CloudWatch Events, que permite processar e armazenar os dados epidemiológicos sobre a dengue no Amazon S3. Este fluxo cria uma automação eficiente para coletar, processar e armazenar dados epidemiológicos de dengue de forma programada e sem intervenção manual.

![image](https://github.com/iararosso/dengue_bh/assets/101842238/09cfd1d2-9e17-4ca8-b61f-7a9acdbcca0e)


## Descrição dos Arquivos
- **get_API_data.py:** Esta função Lambda é responsável por obter dados epidemiológicos de dengue de uma API externa. Ela faz uma solicitação para a API, processa os dados recebidos e os envia para outra função Lambda chamada "create_s3_raw.py".
- **create_s3_raw.py:** Esta função Lambda recebe os dados processados da primeira função e os armazena em um bucket do Amazon S3.

## Benefícios do Projeto
A coleta dos dados epidemiológicos permite criar a base para futuras análises, como a criação de painéis para acompanhamento da efetividade das campanhas de combate ao mosquito ou cálculo da taxa de incidência para determinação das semanas de surto.

## Licenças e Autores
- Iara Rosso
  - E-mail: iara.rosso.ir@googlemail.com
  - LinkedIn: [iara-rosso-ir](https://www.linkedin.com/in/iara-rosso-ir/)
