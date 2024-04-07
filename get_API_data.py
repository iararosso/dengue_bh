import pandas as pd
import numpy as np
import logging
import requests

# Configurando o sistema de logs
logging.basicConfig(filename='error_logs.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def getDataFromAPI(event, context):
    try:
        url = "https://info.dengue.mat.br/api/alertcity"
        geocode = 3106200
        disease = "dengue"
        format = "csv"
        ew_start = 1
        ew_end = 53
        ey_start = 2024
        ey_end = 2024

        params =(
            "&disease="
            + f"{disease}"
            + "&geocode="
            + f"{geocode}"
            + "&disease="
            + f"{disease}"
            + "&format="
            + f"{format}"
            + "&ew_start="
            + f"{ew_start}"
            + "&ew_end="
            + f"{ew_end}"
            + "&ey_start=" 
            + f"{ey_start}"
            + "&ey_end="
            + f"{ey_end}"    
        )

        url_resp = "?".join([url, params])

        logging.info("Trying to read data from URL...")
        response = requests.get(url_resp)
        response.raise_for_status()  # Check for request errors

        # Assuming the data is in CSV format
        data = pd.read_csv(response.content, index_col='SE').T.to_dict(orient='split')
        logging.info("Data read successfully.")
        return data
    except Exception as e:
        logging.error(f"Error getting data from API: {e}")
        raise e
