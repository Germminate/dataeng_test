import os
import csv
import math
import random


class Parser:
    """
    Takes raw data and converts it into an input array for the model.

    Raw data is in the format:
    | Buying Price | Maintenance | Doors | Persons | Lug_Boot_Size | Safety | (Acceptability) Class Value |

    """

    def __init__(self, dataset_path, validation_split=0.7):
        """
        dataset_path: Path to raw data (text file)
        validation_split: (Optional) Ratio of tfrecord files in directory to use for validation
        """
        self._dataset_path = dataset_path
        self._validation_split = validation_split

    def _read_file(self):
        # Read in the raw data file for processing
        with open(self._dataset_path, newline='') as raw_data:
            return [row for row in csv.reader(raw_data, delimiter=",")]

    def _get_variables_data(self, data):
        # Separate independent and dependent variables
        random.shuffle(data)
        x_data, y_data = [], []
        for row in data:
            y_data.append([row.pop(0)])
            x_data.append(row)

        return x_data, y_data

    def _split_data(self, x_values, y_values):
        # Split independent variables values
        x_split = math.ceil(self._validation_split * len(x_values))
        if x_split > 0:
            x_train = x_values[:x_split]
            x_test = x_values[x_split:]
        else:
            x_train = x_values
            x_test = []

        # Split dependent variable values
        y_split = math.ceil(self._validation_split * len(y_values))
        if y_split > 0:
            y_train = y_values[:y_split]
            y_test = y_values[y_split:]
        else:
            y_train = y_values
            y_test = []

        return x_train, y_train, x_test, y_test

    def parse(self):
        """
        Returns arrays of datasets: x_train, y_train, x_test, y_test
        """
        data = self._read_file()
        x_data, y_data = self._get_variables_data(data)
        return self._split_data(x_data, y_data)
