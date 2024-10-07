# Project Summary

## Project Overview

**Overall Purpose**:  
The code implements a framework for data inspection, allowing users to analyze DataFrames (specifically from the Pandas library) using different strategies. The primary goal is to provide insights into data types and summary statistics of the DataFrame.

**Problem Solved**:  
Data scientists and analysts often need to quickly assess the structure and contents of their data before performing further analysis or modeling. This code simplifies that process by providing a clear and modular way to inspect data through different strategies.

## Key Components

1. **DataInspectionStrategy (Abstract Base Class)**:
   - **Purpose**: This is an abstract base class that defines a blueprint for various data inspection strategies. It enforces the implementation of the `inspect` method in derived classes.
   - **Key Methods**:
     - `inspect(dataFrame: pd.DataFrame)`: An abstract method that derived classes must implement to provide specific inspection functionality.

2. **DataTypesInspectionStrategy**:
   - **Purpose**: This class extends `DataInspectionStrategy` and provides a concrete implementation for inspecting the data types and non-null counts of each column in a DataFrame.
   - **Key Methods**:
     - `inspect(dataFrame: pd.DataFrame)`: This method uses the `info()` function of the DataFrame to print data type information and non-null counts.

3. **SummaryStatisticsInspectionStrategy**:
   - **Purpose**: This class also extends `DataInspectionStrategy` and is responsible for providing summary statistics for both numerical and categorical features in the DataFrame.
   - **Key Methods**:
     - `inspect(dataFrame: pd.DataFrame)`: This method uses the `describe()` function to print statistical summaries for numerical features and categorical features.

4. **DataInspector**:
   - **Purpose**: This class serves as a context for executing a chosen inspection strategy on a DataFrame.
   - **Key Methods**:
     - `__init__(self, strategy: DataInspectionStrategy)`: Initializes the inspector with a specific strategy.
     - `set_strategy(self, strategy: DataInspectionStrategy)`: Allows changing the inspection strategy at runtime.
     - `execute_inspection(self, dataFrame: pd.DataFrame)`: Calls the `inspect` method of the current strategy, performing the data inspection.

## Design Patterns

- **Strategy Pattern**:  
  The code implements the Strategy Pattern, which allows defining a family of algorithms (data inspection strategies) and making them interchangeable. The `DataInspector` class acts as a context that uses different inspection strategies, which enhances flexibility and maintainability.

### Contribution to Architecture:
This design pattern allows users to easily switch between different data inspection methods without modifying the `DataInspector` class itself, promoting loose coupling and higher cohesion.

## Logical Aspects

- **Modularity**:  
  The code is structured in a modular way, with separate classes handling different aspects of the data inspection process. Each strategy is encapsulated in its own class, making it easier to manage and understand.

- **Extensibility**:  
  New inspection strategies can be added easily by creating new classes that inherit from `DataInspectionStrategy` and implementing the `inspect` method. This makes the framework highly extensible.

- **Error Handling**:  
  The code does not currently include explicit error handling. Adding try-except blocks in the `inspect` methods could enhance robustness by catching potential errors related to data types or missing values.

- **Encapsulation**:  
  Each class has distinct responsibilities: `DataInspector` manages the inspection process, while individual strategies handle specific inspection tasks. This separation of concerns promotes clearer and more maintainable code.

## Usage Example

Here’s a simple example demonstrating how to use the main functionality of the code:

```python
import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': ['foo', 'bar', 'baz'],
    'C': [1.1, 2.2, None]
}
df = pd.DataFrame(data)

# Initialize the DataInspector with the DataTypesInspectionStrategy
data_inspector = DataInspector(DataTypesInspectionStrategy())

# Execute inspection
data_inspector.execute_inspection(df)

# Change strategy to SummaryStatisticsInspectionStrategy
data_inspector.set_strategy(SummaryStatisticsInspectionStrategy())

# Execute summary statistics inspection
data_inspector.execute_inspection(df)
