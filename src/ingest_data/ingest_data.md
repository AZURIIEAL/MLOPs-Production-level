# Data Ingestion System

## Overview

This project implements a system for ingesting data from files, specifically focusing on ZIP archives containing CSV files. The architecture is designed using the Factory design pattern, allowing for easy extensibility and maintenance.

## Components

### Abstract Base Class: `DataIngester`

- Defines the interface for all data ingesters.
- Contains the abstract method `ingest`, which must be implemented by subclasses.

### Concrete Class: `ZipDataIngester`

- Inherits from `DataIngester`.
- Implements the `ingest` method for ZIP files containing CSVs.
- Contains several helper methods:
  - `_extract_zip`: Extracts the contents of a ZIP file.
  - `_get_csv_files`: Lists CSV files in the extracted directory.
  - `_handle_csv_files`: Processes the found CSV files, ensuring that exactly one CSV file is present.
- If there are any other method to ingest data ,we can add it here and its open for expansion.

### Factory Class: `DataIngestorFactory`

- Uses the Factory design pattern to instantiate the appropriate data ingester based on the provided file extension.
- Returns a `ZipDataIngester` for ZIP files or raises an error for unrecognized extensions.

## Logical Aspects

- **Modularity**: The design is modular, separating concerns(SOC) among different classes.
- **Extensibility**: New ingester classes can be added for additional file types (e.g., JSON, XML) without modifying existing code.
- **Error Handling**: Robust error handling is included for various conditions (e.g., file type mismatches, missing or multiple CSV files).
- **Encapsulation**: Each class has a clear responsibility:
  - `DataIngester`: Interface definition.
  - `ZipDataIngester`: Logic specific to ZIP file ingestion.
  - `DataIngestorFactory`: Centralizes the creation of ingesters.

## Design Pattern: Factory

The Factory design pattern is utilized in the `DataIngestorFactory` class, encapsulating the logic required to create instances of different ingester classes based on file type. This promotes loose coupling, allowing client code to remain unaware of specific ingester implementations.

## Conclusion

This code provides a clean, extensible design for handling data ingestion, utilizing abstract classes and a factory pattern to promote flexibility and maintainability. It serves as a solid foundation for further enhancements as more data sources and formats are introduced.

## Usage

To use this system, create an instance of `DataIngestorFactory` and call `get_data_ingestor` with the desired file extension. For example:

```python
factory = DataIngestorFactory()
ingestor = factory.get_data_ingestor('.zip')
data_frame = ingestor.ingest('path/to/your/file.zip')