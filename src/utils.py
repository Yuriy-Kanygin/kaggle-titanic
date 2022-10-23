from typing import Tuple

import pandas as pd


def read_data(
    path_to_train: str, path_to_test: str
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """This is a raw data reader function

    Args:
        path_to_train (str): path to the train dataset
        path_to_train (str): path to the test dataset

    Returns:
        tuple: train and test dataframe
    """
    train_data = pd.read_csv(path_to_train)
    print("Train data imported successfully!!")
    print("=" * 50)
    test_data = pd.read_csv(path_to_test)
    print("Test data imported successfully!!")
    return train_data, test_data
