import json
import pandas as pd
from pathlib import Path

def run_silver_transform(**context):
    execution_date = context["ds_nodash"]

    bronze_file = context["ti"].xcom_pull(
        key="bronze_file",
        task_ids="bronze_ingestion" 
    )

    if not bronze_file:
        raise ValueError("Caminho do arquivo Bronze não encontrado no XCom.")

    silver_path = Path("/usr/local/airflow/include/silver")
    silver_path.mkdir(parents=True, exist_ok=True)

    with open(bronze_file, "r") as f:
        raw = json.load(f)
    
    states_data = raw.get("states")
    if not states_data:
        states_data = []

    df_raw = pd.DataFrame(states_data)

    if not df_raw.empty:
        df_raw.columns = [
            "icao24", "callsign", "origin_country", "time_position", "last_contact", "longitude",
            "latitude", "baro_altitude", "on_ground", 
            "velocity", "true_track", "vertical_rate",
            "sensors", "geo_altitude", "squawk",
            "spi", "position_source"
        ]

        df = df_raw[
            [
                "icao24",
                "origin_country",
                "velocity",
                "on_ground"
            ]
        ]
    else:
        df = pd.DataFrame(columns=["icao24", "origin_country", "velocity", "on_ground"])

    output_file = silver_path / f"flights_silver_{execution_date}.csv"
    df.to_csv(output_file, index=False)

    context["ti"].xcom_push(
        key="silver_file",
        value=str(output_file)
    )