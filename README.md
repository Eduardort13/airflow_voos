# ✈️ Pipeline de Dados: Monitoramento de Tráfego Aéreo (OpenSky API)

## 📌 Sobre o Projeto
Este projeto desenvolve um pipeline de dados ponta a ponta (ETL) para monitorar informações de voos em tempo real utilizando a API pública do OpenSky Network. O objetivo é extrair, transformar e carregar (ETL) dados de aeronaves para análise de volume de voos e velocidades médias por país de origem.

O projeto foi construído utilizando a **Arquitetura de Medalhão**, garantindo a rastreabilidade e a qualidade dos dados em cada etapa do processo.

---

## 🏗️ Arquitetura do Pipeline (Medalhão)

O fluxo de dados é organizado em três camadas principais:

1.  **Camada Bronze (Raw):** Ingestão dos dados brutos diretamente da API OpenSky em formato JSON.
2.  **Camada Silver (Trusted):** Limpeza e padronização dos dados, convertendo-os para CSV e tratando valores nulos ou inconsistentes.
3.  **Camada Gold (Refined):** Agregação dos dados para calcular KPIs, como a velocidade média e a contagem de voos por país.



---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.13
* **Orquestração:** Apache Airflow (via Astro CLI)
* **Processamento de Dados:** Pandas
* **Banco de Dados:** PostgreSQL (Containerizado via Docker)
* **Infraestrutura:** Docker e WSL2 (Ubuntu)
* **Visualização de Dados:** DBeaver

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
* Docker Desktop instalado.
* Astro CLI instalado.

### Passo a Passo
1.  Clone o repositório:
    ```bash
    git clone [https://github.com/Eduardort13/projeto_airflow_voos.git](https://github.com/Eduardort13/projeto_airflow_voos.git)
    ```
2.  Inicie o ambiente do Airflow:
    ```bash
    astro dev start
    ```
3.  Acesse a interface do Airflow em `localhost:8080`.
4.  Configure a conexão `postgres_default` no menu **Admin > Connections**.
5.  Ative e execute a DAG `voos_pipeline`.

---

## 💡 Aprendizados e Desafios
Este projeto demonstrou a importância da orquestração de containers e do gerenciamento de conexões em ambientes de engenharia de dados. Um dos principais desafios superados foi a configuração da persistência de dados em um banco de dados PostgreSQL local integrado ao ecossistema do Airflow, garantindo que o pipeline seja modular e escalável para outros *Data Warehouses* (como Snowflake).

---
