# Bivariate Analysis 

## Code Overview

### Purpose
The code aims to provide a flexible and modular framework for performing bivariate analysis on datasets. It allows users to visualize relationships between pairs of features in a dataset, specifically focusing on two types of analyses: numerical vs. numerical and categorical vs. numerical.

### Problem Solved
The code solves the problem of visualizing relationships between two variables in a dataset, enabling users to better understand correlations, distributions, and potential trends. The functionality provided includes scatter plots for numerical vs. numerical analysis and box plots for categorical vs. numerical analysis.

## Key Components

### Classes

1. **BivariateAnalysisStrategy (Abstract Base Class)**
   - **Purpose**: Serves as the interface for different bivariate analysis strategies.
   - **Key Methods**:
     - `analyze(self, df: pd.DataFrame, feature1: str, feature2: str)`: Abstract method that must be implemented by derived classes to perform analysis.

2. **NumericalVsNumericalAnalysis (Concrete Class)**
   - **Purpose**: Implements the analysis strategy for visualizing relationships between two numerical features using a scatter plot.
   - **Key Methods**:
     - `analyze(self, df: pd.DataFrame, feature1: str, feature2: str)`: Uses `seaborn.scatterplot` to create a scatter plot of the two specified features.

3. **CategoricalVsNumericalAnalysis (Concrete Class)**
   - **Purpose**: Implements the analysis strategy for visualizing relationships between a categorical feature and a numerical feature using a box plot.
   - **Key Methods**:
     - `analyze(self, df: pd.DataFrame, feature1: str, feature2: str)`: Uses `seaborn.boxplot` to create a box plot of the numerical feature against the categorical feature.

4. **BivariateAnalyzer**
   - **Purpose**: Context class that utilizes a specific analysis strategy to perform the analysis.
   - **Key Methods**:
     - `__init__(self, strategy: BivariateAnalysisStrategy)`: Initializes the analyzer with a specific analysis strategy.
     - `set_strategy(self, strategy: BivariateAnalysisStrategy)`: Allows changing the analysis strategy at runtime.
     - `execute_analysis(self, df: pd.DataFrame, feature1: str, feature2: str)`: Executes the analysis using the current strategy.

## Design Patterns

### Strategy Pattern
- **Description**: The code utilizes the Strategy design pattern by defining a family of algorithms (bivariate analysis strategies) and making them interchangeable.
- **Contribution to Architecture**: This pattern promotes flexibility and allows the user to switch between different analysis types (e.g., numerical vs. numerical or categorical vs. numerical) without modifying the `BivariateAnalyzer` class.

## Logical Aspects

### Design Principles

1. **Modularity**
   - The code is structured into distinct classes, each responsible for specific functionalities related to bivariate analysis, promoting a clear separation of concerns.

2. **Extensibility**
   - New analysis strategies can easily be added by creating additional classes that extend `BivariateAnalysisStrategy`, allowing for the inclusion of other analysis types without modifying existing code.

3. **Error Handling**
   - The current code does not explicitly handle errors. Implementing error checks (e.g., verifying the existence of specified features in the DataFrame) would improve robustness.

4. **Encapsulation**
   - Each class encapsulates its behavior and responsibilities. The `BivariateAnalyzer` class delegates analysis execution to the strategy classes, maintaining a clean separation between analysis logic and execution control.

## Visualizations

### Scatter Plot
- **Purpose**: Used to visualize the relationship between two numerical features. It helps in identifying trends, clusters, or correlations between the variables.
- **Parameters**:
  - `x`: Name of the numerical feature to be plotted on the x-axis.
  - `y`: Name of the numerical feature to be plotted on the y-axis.
  - `data`: The DataFrame containing the data to be visualized.

### Box Plot
- **Purpose**: Used to visualize the distribution of a numerical feature across different categories. It provides insights into the median, quartiles, and potential outliers within each category.
- **Parameters**:
  - `x`: Name of the categorical feature to be plotted on the x-axis.
  - `y`: Name of the numerical feature to be plotted on the y-axis.
  - `data`: The DataFrame containing the data to be visualized.
  - Additional parameters (e.g., `palette`, `orient`) can customize the appearance.

## Usage Example

Here’s a simple example demonstrating how to use the main functionality of the code:

```python
import pandas as pd

# Sample DataFrame
data = {
    'numerical_feature1': [1, 2, 3, 4, 5, 6],
    'numerical_feature2': [2, 3, 4, 5, 6, 7],
    'categorical_feature': ['A', 'B', 'A', 'B', 'A', 'B']
}

df = pd.DataFrame(data)

# Creating the BivariateAnalyzer with a numerical vs. numerical strategy
analyzer = BivariateAnalyzer(NumericalVsNumericalAnalysis())
analyzer.execute_analysis(df, 'numerical_feature1', 'numerical_feature2')

# Changing strategy to categorical vs. numerical
analyzer.set_strategy(CategoricalVsNumericalAnalysis())
analyzer.execute_analysis(df, 'categorical_feature', 'numerical_feature1')
