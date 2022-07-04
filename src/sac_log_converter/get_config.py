"""Get and Parse the configurations."""
from typing import Any, Dict

import yaml


def check_config_leef_to_json(data: dict) -> dict:
    """Check the configuration."""
    if data.get('syslog_headers_present') is None:
        raise ValueError(
            "syslog_headers_present Field is missing in configuration.")

    if (data.get('syslog_headers_present')) and (data.get('syslog_headers_fields') is None):
        raise ValueError(
            "syslog_headers_fields should be not empty if syslog_headers_present field is set to True/1")

    if data.get('leef_headers_fields') is None:
        raise ValueError(
            "leef_headers_fields Field is missing in configuration.")

    if data.get('delimiter') is None:
        raise ValueError("delimiter Field is missing in configuration.")

    if data.get('payload_delimiter') is None:
        raise ValueError(
            "payload_delimiter Field is missing in configuration.")
    return data


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
