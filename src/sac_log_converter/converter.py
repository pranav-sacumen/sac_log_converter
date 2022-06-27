"""Converter code from leef to json."""
from typing import Any
from typing import Dict
from typing import List

from utils import check_date_time_present


def convert_leef_to_json(raw_config, events_list) -> Dict[str, Any]:
    """Convert the leef format into json."""
    json_events = []
    if raw_config[0]['leef_to_json']['syslog_headers_present']:
        for event in events_list:
            header = event.split('|')[0]
            # pass the header and header fields which we got from config
            syslog_headers = parse_syslog_headers(header, raw_config[0]['leef_to_json']['syslog_headers_fields'])
            # Split the event by |
            event_split = event.split('|')
            # pass the field names from config and event split list
            leef_headers = parse_leef_headers(raw_config[0]['leef_to_json']['leef_headers_fields'], event_split)
            # TODO: Add syslog headers and leef_headers in a dictioanry
            data = event_split[-1]
            # split the data using the delimeter provided in configuration
            if raw_config[0]['leef_to_json']['delimiter']:
                datalist = data.split(raw_config[0]['leef_to_json']['delimiter'])
                parse_data(datalist)
        # TODO: modularise into different functions

    return json_events


def parse_syslog_headers(header: str, header_fields: str) -> Dict[str, Any]:
    """Map headers with the header fields.

    :params header: Syslog Header
    :type header: str
    :params header_fields: header_fields for mapping
    :type header_fields: str
    :return: Dictionary where syslog headers will be present
    :rtype: str
    """
    syslog_header_dict = {}
    # mapping of timestamp, hostname and version
    # try except block to not print the error and continue
    status = False
    try:
        # if timestamp is present in event, prepare a syslog header dict
        if check_date_time_present(header.split(':')[0]):
            for index in range(len(header_fields.split(','))):
                syslog_header_dict[header_fields.split(',')[index]] = header.split(':')[index]
            status = True
    except ValueError:
        pass
        # if timestamp is not present in event, prepare a syslog header dict
        if not status:
            for index in range(len(header_fields.split(',')) - 1):
                syslog_header_dict[header_fields.split(',')[index + 1]] = header.split(':')[index]

    return syslog_header_dict


def parse_leef_headers(leef_header: str, data_list: List[str]) -> Dict[str, Any]:
    """Map the leef headers with fields.

    :param leef_header: leef_header field names
    :type leef_header: str
    :param event_list: List of the data in events
    :type event_list: List[str]
    :return: Dictionary where leef headers will be present
    :rtype: Dict[str, Any]
    """
    leef_header_dict = {}
    leef_header_list = leef_header.split(',')
    # read the leef_header_field names and create a dictionary
    for element, index in zip(leef_header_list, range(1, len(data_list))):
        leef_header_dict[element] = data_list[index]

    return leef_header_dict


def parse_data(datalist: List[str]) -> Dict[str, Any]:
    """Map data and add it as a dictionary."""
    data_dict = {}
    for data in datalist:
        key = data.split('=')[0]
        value = data.split('=')[1]
        print(key, value)
        # value = [item[1] for item in data.split('=')]
        # print(key)
        # print(value)

        # if key_value[0] in data_dict:
        #     # check if the value is list
        #     if isinstance(key_value[1],list):

    return data_dict


# a = convert_leef_to_json([{'leef_to_json': {'syslog_headers_present': 1,
# 'syslog_headers_fields': 'EventReceivedTime,Hostname,LEEF Version',
# 'time_format': 'yyyy-MM-ddTHH:mm:ss.SSSZ',
# 'leef_headers_fields': 'Vendor,Product,Minor_version,cvss_score,maliciousness,severity',
# 'delimiter': ' '}}, {'json_to_leef': {'add_sys_log_header': 1, 'sys_log_header_values':
# 'event_time,hostname, leef_version', 'current_time_add': 0, 'time_format': 'utc',
# 'leef_headers': 'vendor, source_name,version, event_id, data',
# 'leef_headers_mapping': 'a, b, c, d', 'payload_mapping_fields': 'src, dst, spt',
# 'delimeter': '|'}}],
# ['SAC:0|Sacumen|CAAS|2021.2.0|3|MALICIOUS|High|cat=C2 cs1Label=subcat
# cs1=DNS_TUNNELING cs2Label=vueUrls
# cs2=https://aws-dev.sacdev.io/alerts?filter=alertId%3D%3D81650 cs3Label=Tags cs3=USA,Finance
# cs4Label=Url
# cs4=https://aws-dev.sacdev.io/settings/tir?rules.sort=4%3A1&filter=state%3D%3D2&selected=9739323
# cn1Label=severityScore cn1=900
# msg=Malicious activity was reported in CAAS\= A threat intelligence rule has been automatically
# created in DAAS. dhost=bad.com dst=1.1.1.1'])
