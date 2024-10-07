from abc import ABC, abstractmethod
import pandas as pd

class DataInspectionStrategy(ABC):
    @abstractmethod
    def inspect(self,dataFrame:pd.DataFrame):
        pass

class DataTypesInspectionStrategy(DataInspectionStrategy):
    def inspect(self,dataFrame:pd.DataFrame):
        print("\nData Types and Non-null Counts:")
        print(dataFrame.info())

class SummaryStatisticsInspectionStrategy(DataInspectionStrategy):
    def inspect(self, dataFrame: pd.DataFrame):
        print("\nSummary Statistics (Numerical Features):")
        print(dataFrame.describe())
        print("\nSummary Statistics (Categorical Features):")
        print(dataFrame.describe(include=["O"]))

class DataInspector:
    def __init__(self, strategy: DataInspectionStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: DataInspectionStrategy):
        self._strategy = strategy

    def execute_inspection(self, dataFrame: pd.DataFrame):
        self._strategy.inspect(dataFrame)