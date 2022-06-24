"""Get and Parse the configurations."""
from datetime import datetime
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

def parse_headers(header:str, header_fields:str) -> Dict[str, Any]:
    """Map headers with the header fields.

    :params header: Syslog Header
    :type header: str
    :params header_fields: header_fields for mapping
    :type header_fields: str
    :return: Dictionary where syslog headers will be present
    :rtype: str
    """
    header_dict = {}
    # mapping of timestamp, hostname and version
    # try except block to not print the error and continue
    status = False
    try:
        # if timestamp is present in event, prepare a syslog header dict
        if datetime.strptime(header.split(':')[0], '%Y') or datetime.strptime(header.split(':')[0], '%b %d %y') or datetime.strptime(header.split(':')[0], '%b %d %Y')  or datetime.strptime(header.split(':')[0], '%B %d %y') or datetime.strptime(header.split(':')[0], '%B %d %Y'):
            header_dict[header_fields.split(',')[0]] = header.split(':')[0]
            header_dict[header_fields.split(',')[1]] = header.split(':')[1]
            header_dict[header_fields.split(',')[2]] = header.split(':')[2]
            status = True
    except ValueError:
        pass
        # if timestamp is not present in event, prepare a syslog header dict
        if not status:
            header_dict[header_fields.split(',')[1]] = header.split(':')[0]
            header_dict[header_fields.split(',')[2]] = header.split(':')[1]
            # logger.debug("Syslog Header Dictionary",header_dict)
    return header_dict
