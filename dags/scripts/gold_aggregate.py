import pandas as pd
from pathlib import Path

def run_gold_aggregate(**context):
    silver_file = context["ti"].xcom_pull(
        key="silver_file", task_ids="silver_transform"
    )

    if not silver_file:
        raise ValueError("Caminho do arquivo Silver não encontrado no XCom.")

    df = pd.read_csv(silver_file)

    if not df.empty:
        agg = (
            df.groupby("origin_country")
            .agg(
                total_flights=("icao24", "count"),
                avg_velocity=("velocity", "mean"),
                on_ground=("on_ground", "sum")
            )
            .reset_index()
            .sort_values(by="total_flights", ascending=False)
        )
        agg["avg_velocity"] = agg["avg_velocity"].round(2)
    else:
        agg = pd.DataFrame(columns=["origin_country", "total_flights", "avg_velocity", "on_ground"])

    gold_path = Path(str(silver_file).replace("silver", "gold"))
    
    gold_path.parent.mkdir(parents=True, exist_ok=True)

    agg.to_csv(gold_path, index=False)
    context["ti"].xcom_push(key="gold_file", value=str(gold_path))
    
    print(f"Camada Gold concluída com sucesso! Salvo em: {gold_path}")