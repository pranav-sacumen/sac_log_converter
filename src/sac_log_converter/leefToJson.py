"""Driver function for leef to json conversion."""
from logging import Logger as logger
from typing import Any, Dict
#from converter import convert_leef_to_json
from getConfig import get_config
# from sac_log_converter.Getconfig import parse_configurations


def leef_to_json(config_path:str) -> Dict[str, Any]:
#events:Dict[str, Any]):
    """Convert leef event to a json event by reading configs."""
    raw_config = get_config(config_path)
    logger.debug('configurations: {raw_config}'.format(raw_config=raw_config))


    #     else:
    #         logger.error('Config path is not provided please provide path to yaml configuration.')
    # else:
    #     raw_config = check_config(config_json)

    # config = parse_configurations(raw_config)
    # json_data = convert_leef_to_json(config, events)
    return raw_config
