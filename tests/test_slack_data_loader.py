import unittest

import pandas as pd

from src.loader import (
    SlackDataLoader,  # Import the SlackDataLoader class from your module
)


class TestSlackDataLoader(unittest.TestCase):
    def setUp(self):
        # Create an instance of the SlackDataLoader class
        self.slack_loader = SlackDataLoader(path="your_file_path")  # Replace "your_file_path" with the actual file path

    def test_data_frame_columns(self):
        # Get the data frame from the SlackDataLoader instance
        data_frame = self.slack_loader.get_users()

        # You may need to initialize or set up some data for testing here

    def test_expected_columns(self):
        # Call the method that returns the DataFrame
        data_frame = self.slack_loader.get_users()  # Replace with your method name if different from "get_data"

        # Define the expected columns
        expected_columns = ['column1', 'column2', ...]  # Replace with your expected column names

        # Check if the columns of the DataFrame match the expected columns
        self.assertEqual(list(data_frame.columns), expected_columns)
