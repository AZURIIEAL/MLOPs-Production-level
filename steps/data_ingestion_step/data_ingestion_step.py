import pandas as pd
from constants import EXTENSION_ZIP
from src.ingest_data.ingest_data import DataIngestorFactory
from zenml import step


@step
def data_ingestion_step(file_path: str) -> pd.DataFrame:
    file_extension = EXTENSION_ZIP 
    data_ingestor = DataIngestorFactory.get_data_ingestor(file_extension)
    df = data_ingestor.ingest(file_path)
    return df
