import os
import sys
import unittest
from unittest.mock import patch, MagicMock
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from ingest_data.ingest_data import ZipDataIngester
from constants import (
    EXTENSION_MISMATCH_ERROR,
    EXTENSION_NOT_FOUND_ERROR,
    EXTENSION_MULTIPLE_FILES_ERROR,
)

class TestZipDataIngester(unittest.TestCase):

    @patch('zipfile.ZipFile')
    @patch('os.listdir')
    @patch('pandas.read_csv')
    def test_ingest_valid_zip(self, mock_read_csv, mock_listdir, mock_zipfile):
        mock_zipfile.return_value.__enter__.return_value.extractall = MagicMock()
        mock_listdir.return_value = ['data.csv']
        mock_read_csv.return_value = pd.DataFrame({'column1': [1, 2], 'column2': [3, 4]})

        ingester = ZipDataIngester()
        df = ingester.ingest('fake_path/archive.zip')
        
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (2, 2))
        mock_zipfile.assert_called_once_with('fake_path/archive.zip', 'r')
        mock_listdir.assert_called_once_with('extracted_data')

    @patch('zipfile.ZipFile')
    def test_ingest_non_zip_file(self, mock_zipfile):
        ingester = ZipDataIngester()
        with self.assertRaises(ValueError) as context:
            ingester.ingest('fake_path/data.txt')
        self.assertEqual(str(context.exception), EXTENSION_MISMATCH_ERROR)

    @patch('zipfile.ZipFile')
    @patch('os.listdir')
    def test_ingest_no_csv_files(self, mock_listdir, mock_zipfile):
        mock_zipfile.return_value.__enter__.return_value.extractall = MagicMock()
        mock_listdir.return_value = [] 

        ingester = ZipDataIngester()
        with self.assertRaises(FileNotFoundError) as context:
            ingester.ingest('fake_path/archive.zip')
        self.assertEqual(str(context.exception), EXTENSION_NOT_FOUND_ERROR)

    @patch('zipfile.ZipFile')
    @patch('os.listdir')
    def test_ingest_multiple_csv_files(self, mock_listdir, mock_zipfile):
        mock_zipfile.return_value.__enter__.return_value.extractall = MagicMock()
        mock_listdir.return_value = ['data1.csv', 'data2.csv'] 

        ingester = ZipDataIngester()
        with self.assertRaises(ValueError) as context:
            ingester.ingest('fake_path/archive.zip')
        self.assertEqual(str(context.exception), EXTENSION_MULTIPLE_FILES_ERROR)

if __name__ == '__main__':
    unittest.main()
