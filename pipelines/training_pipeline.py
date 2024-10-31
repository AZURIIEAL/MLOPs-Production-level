from zenml import Model, pipeline, step
from steps.data_ingestion_step.data_ingestion_step import data_ingestion_step
@pipeline(
    model=Model(
        name="prices_predictor"
    ),
)
def ml_pipeline():
    raw_data = data_ingestion_step(
        file_path="data/archive.zip"
    )
    