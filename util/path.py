import os


def get_config_path():
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../config"))
    return config_path


def get_data_path():
    data_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../data/")
    )
    return data_path
