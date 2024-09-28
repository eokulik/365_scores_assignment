import csv
import logging
from typing import List

import pytest
from _pytest.mark.structures import ParameterSet

logging.getLogger(__name__)


def read_test_data(filepath: str, data_name: str) -> List[ParameterSet]:
    try:
        with open(filepath, 'r', encoding='utf-8', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            test_data = []
            for row in reader:
                if data_name == row['name']:
                    del row['name']
                    param_id = row.pop('id')
                    test_data.append(pytest.param(*row.values(), id=param_id))
            if test_data:
                logging.info(
                    'Test parameters prepared from file %s with data name "%s": %s',
                    filepath, data_name, test_data
                )
            else:
                logging.warning('No test data for data name %s in file %s', data_name, filepath)
            return test_data
    except FileNotFoundError as err:
        logging.exception('File %s not found', filepath)
        raise err
