# Class Overview
The provided code implements a framework for **univariate analysis** of features in a pandas DataFrame. It allows users to analyze and visualize the distribution of both numerical and categorical features using different strategies, making it easier to understand individual variables in a dataset.

**Problem Solved:**  
The code offers a structured approach to perform univariate analysis, enabling users to choose the appropriate method for analyzing different types of data. This is essential for exploratory data analysis (EDA), helping to identify trends, distributions, and patterns within individual features.

**Functionality Provided:**  
The code provides functionalities to:
- Analyze and visualize the distribution of numerical features using histograms.
- Analyze and visualize the distribution of categorical features using count plots.

# Key Components

## 1. `UnivariateAnalysisStrategy (ABC)`
- **Purpose:**  
  This is an **abstract base class (ABC)** that defines a strategy for univariate analysis. It outlines a method that must be implemented by concrete strategies.

- **Key Methods:**
  - `analyze(self, df: pd.DataFrame, feature: str)`  
    Abstract method to be implemented by subclasses to perform the analysis on a specified feature of the DataFrame.

## 2. `NumericalUnivariateAnalysis`
- **Purpose:**  
  This class implements the `UnivariateAnalysisStrategy` for analyzing numerical features. It provides a specific method to visualize the distribution of numerical data.

- **Key Methods:**
  - `analyze(self, df: pd.DataFrame, feature: str)`  
    Uses a histogram to visualize the distribution of the specified numerical feature along with a Kernel Density Estimate (KDE) for better interpretation.

## 3. `CategoricalUnivariateAnalysis`
- **Purpose:**  
  This class implements the `UnivariateAnalysisStrategy` for analyzing categorical features. It provides a specific method to visualize the distribution of categorical data.

- **Key Methods:**
  - `analyze(self, df: pd.DataFrame, feature: str)`  
    Uses a count plot to visualize the distribution of the specified categorical feature.

## 4. `UnivariateAnalyzer`
- **Purpose:**  
  This class orchestrates the univariate analysis by using a chosen strategy to analyze a specified feature of the DataFrame.

- **Key Methods:**
  - `__init__(self, strategy: UnivariateAnalysisStrategy)`  
    Initializes the analyzer with a specific analysis strategy.
  - `set_strategy(self, strategy: UnivariateAnalysisStrategy)`  
    Allows changing the analysis strategy dynamically.
  - `execute_analysis(self, df: pd.DataFrame, feature: str)`  
    Executes the analysis by invoking the strategy's `analyze` method.

# Visualization Component

## Why Use a Heatmap?

A heatmap is used because it provides a visually intuitive way to see the distribution of missing data across the DataFrame. The heatmap shows:
- Missing values in a simple, color-coded format.
- Clear patterns or trends in the missing data that may not be obvious from raw numbers alone.

Seaborn is a powerful visualization library that makes it easy to generate attractive and informative plots. The heatmap in this case highlights where missing values exist in the DataFrame.

## Why Use a Count Plot?
A count plot is effective because it visually represents the frequency of each category in a categorical feature. It allows for:
- Quick identification of the most and least common categories.
- Insight into the distribution of categories, helping to uncover patterns or imbalances in the dataset.
- Easy comparison between different categories, which can inform further analysis or model development.

# Design Patterns

### Strategy Pattern  
The code implements the **Strategy Pattern**, which allows selecting different algorithms (or strategies) for univariate analysis at runtime.

**Contribution to the Architecture:**  
This pattern enhances flexibility by enabling the addition of new analysis methods without modifying existing code. Users can easily switch between different analysis strategies for numerical and categorical data.

# Logical Aspects

### 1. Modularity:  
The code is modular, with separate classes for each analysis strategy. Each class has a single responsibility, making it easier to manage and extend.

### 2. Extensibility:  
New strategies for univariate analysis can be added by creating additional subclasses of `UnivariateAnalysisStrategy`, thus allowing for more analytical methods (e.g., box plots, violin plots) without altering the existing structure.

### 3. Error Handling:  
Error handling is not explicitly included. Future extensions could benefit from adding checks to ensure that the feature exists in the DataFrame and that the data type is appropriate for the chosen analysis method.

### 4. Encapsulation:  
Responsibilities are well-encapsulated:
- Each analysis strategy class encapsulates the logic for analyzing either numerical or categorical data.
- The `UnivariateAnalyzer` class manages the analysis execution based on the selected strategy.

# Usage Example

```python
import pandas as pd

# Example DataFrame
data = {
    'NumericalFeature': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'CategoricalFeature': ['A', 'B', 'A', 'B', 'A', 'C', 'C', 'C', 'B', 'A']
}
df = pd.DataFrame(data)

# Analyze numerical feature
numerical_analyzer = UnivariateAnalyzer(NumericalUnivariateAnalysis())
numerical_analyzer.execute_analysis(df, 'NumericalFeature')

# Analyze categorical feature
categorical_analyzer = UnivariateAnalyzer(CategoricalUnivariateAnalysis())
categorical_analyzer.execute_analysis(df, 'CategoricalFeature')


