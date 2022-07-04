"""Driver function for leef to json conversion."""
from typing import Any, Dict, List

from converter import convert_leef_to_json
from get_config import check_config_leef_to_json, get_config


def leef_to_json(events_list: list, is_config: bool = True, config_path: str = "", config_json: Dict[Any, Any] = {}) -> List[dict]:
    """Convert leef event to a json event by reading configs.

    :params config_path: Path of configuration file
    :type config_path: str
    :params events_list: Leef events as a list
    :type events_list: List[str]
    :return: json event after conversion
    :rtype: Dict[str, Any]
    """
    if is_config:
        if config_path:
            try:
                config_json = get_config(config_path)
            except ValueError as val_err:
                raise ValueError("Configuration is not in correct format.") from val_err
        else:
            raise ValueError("Config path is not provided please provide path to yaml configuration.")
    elif not config_json:
        raise KeyError("Configuration is not provided.")

    check_config_leef_to_json(config_json[0]['leef_to_json'])
    json_list = convert_leef_to_json(config_json, events_list)
    return json_list
