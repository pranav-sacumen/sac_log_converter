"""Driver function for leef to json conversion."""
from typing import Any
from typing import Dict
from typing import List

from converter import convert_leef_to_json
from getConfig import get_config

def leef_to_json(config_path: str, events_list: List[str]) -> Dict[str, Any]:
    """Convert leef event to a json event by reading configs.

    :params config_path: Path of configuration file
    :type config_path: str
    :params events_list: Leef events as a list
    :type events_list: List[str]
    :return: json event after conversion
    :rtype: Dict[str, Any]
    """
    # json_data = {}
    raw_config = get_config(config_path)
    json_list = convert_leef_to_json(raw_config, events_list)

    return json_list

# c = leef_to_json('C:/Users/DIVYA/Documents/Log Convertor Resuable Library/sac_log_converter/config/config.yaml',
# ['SAC:0|Sacumen|CAAS|2021.2.0|3|MALICIOUS|High|cat=C2 cs1Label=subcat cs1=DNS_TUNNELING cs2Label=vueUrls cs2=https://aws-dev.sacdev.io/alerts?filter=alertId%3D%3D81650 cs3Label=Tags cs3=USA,Finance cs4Label=Url cs4=https://aws-dev.sacdev.io/settings/tir?rules.sort=4%3A1&filter=state%3D%3D2&selected=9739323 cn1Label=severityScore cn1=900 msg=Malicious activity was reported in CAAS\= A threat intelligence rule has been automatically created in DAAS. dhost=bad.com dst=1.1.1.1'])
# print(c)
