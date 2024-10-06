from abc import ABC, abstractmethod
import pandas as pd
import zipfile
import os
from constants import (
    EXTENSION_ZIP,
    EXTENSION_CSV,
    EXTENSION_MISMATCH_ERROR,
    EXTENSION_NOT_FOUND_ERROR,
    EXTENSION_MULTIPLE_FILES_ERROR,
    EXTRACTED_DATA_FILE_NAME,
    NO_INGESTOR_AVAILABLE,
)

class DataIngester(ABC):
    @abstractmethod
    def ingest(self, file_path: str) -> pd.DataFrame:
        """Ingest data from the given file path and return a DataFrame."""
        pass

class ZipDataIngester(DataIngester):
    def ingest(self, file_path: str) -> pd.DataFrame:
        """Ingest data from a zip file containing CSV files."""
        if not file_path.endswith(EXTENSION_ZIP):
            raise ValueError(EXTENSION_MISMATCH_ERROR)
        
        self._extract_zip(file_path)
        csv_files = self._get_csv_files()
        return self._handle_csv_files(csv_files)

    def _extract_zip(self, file_path: str) -> None:
        """Extract the zip file to the specified directory."""
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall(EXTRACTED_DATA_FILE_NAME)

    def _get_csv_files(self) -> list:
        """Retrieve a list of CSV files from the extracted data directory."""
        extracted_files = os.listdir(EXTRACTED_DATA_FILE_NAME)
        return [file for file in extracted_files if file.endswith(EXTENSION_CSV)]

    def _handle_csv_files(self, csv_files: list) -> pd.DataFrame:
        """Handle the CSV files based on how many were found."""
        if len(csv_files) == 0:
            raise FileNotFoundError(EXTENSION_NOT_FOUND_ERROR)
        if len(csv_files) > 1:
            raise ValueError(EXTENSION_MULTIPLE_FILES_ERROR)

        csv_file_path = os.path.join(EXTRACTED_DATA_FILE_NAME, csv_files[0])
        return pd.read_csv(csv_file_path)

class DataIngestorFactory:
    def get_data_ingestor(self, file_extension: str) -> DataIngester:
        """Return an appropriate data ingester based on the file extension."""
        if file_extension == EXTENSION_ZIP:
            return ZipDataIngester()
        else:
            raise ValueError(f"{NO_INGESTOR_AVAILABLE} : {file_extension}")
