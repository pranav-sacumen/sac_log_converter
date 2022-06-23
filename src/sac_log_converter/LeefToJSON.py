"""Driver function for leef to json conversion."""
from asyncio.log import logger

from sac_log.logger import get_logger
from sac_log_converter.converter import convert_leef_to_json
from sac_log_converter.Getconfig import check_config
from sac_log_converter.Getconfig import parse_configurations


def leef_to_json(is_config=True, config_path=None, config_json=None, events=[]):
    """Driver function."""
    if is_config==True:
        if config_path is not None:
            try:
                raw_config = check_config(config_path)
            except ValueError as e:
                logger.error("Yaml file is not in correct format")

        else:
            logger.error('Config path is not provided please provide path to yaml configuration.')
    else:
        raw_config = check_config(config_json)

    config = parse_configurations(raw_config)
    json_data = convert_leef_to_json(config, events)
    return json_data
