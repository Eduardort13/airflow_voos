import pandas as pd
from airflow.providers.postgres.hooks.postgres import PostgresHook

def run_load_to_postgres(**context):
    gold_file = context["ti"].xcom_pull(
        key="gold_file",
        task_ids="gold_aggregate"
    )

    if not gold_file:
        raise ValueError("Caminho do arquivo Gold não encontrado no XCom.")

    df = pd.read_csv(gold_file)

    if df.empty:
        return

    df.columns = df.columns.str.lower()

    hook = PostgresHook(postgres_conn_id="postgres_default")
    engine = hook.get_sqlalchemy_engine()

    df.to_sql(
        name="flight_kpis",
        con=engine,
        if_exists="replace",
        index=False
    )
    
    print("Carga no Postgres local concluída com sucesso!")