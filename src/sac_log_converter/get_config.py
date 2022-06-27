"""Get and Parse the configurations."""
from typing import Any
from typing import Dict

import yaml


def get_config(config_path: str) -> Dict[str, Any]:
    """Read the configurations from the yaml file.

    :param config_path: configuration file path
    :type config_path: str
    :return: configurations in form of json
    :rtype: Dict[str, Any]
    """
    with open(config_path) as yamlfile:
        config = yaml.safe_load(yamlfile)
        return config

# c = get_config('C:/Users/DIVYA/Documents/Log Convertor Resuable Library/sac_log_converter-leef-json/config/config.yaml')
# print('c:',c)
