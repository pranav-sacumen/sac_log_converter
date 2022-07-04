"""Converter code from leef to json."""

from typing import Any, Dict, List

from sac_log_converter.constants.config import (DELIMITER, LEEF_HEADER_FIELDS,
                                                LEEF_TO_JSON,
                                                PAYLOAD_DELIMITER,
                                                SYSLOG_HEADER_FIELDS,
                                                SYSLOG_HEADER_PRESENT)
from sac_log_converter.constants.general import (COLON, COMMA, DOUBLE_SLASH,
                                                 EQUAL, PAY_LOAD, SLASH_EQUAL,
                                                 SPACE_CHAR)
from sac_log_converter.utils import check_date_time_present


def convert_leef_to_json(raw_config: dict, events_list: list) -> list:
    """Convert the leef format into json."""
    json_events = []

    for event in events_list:
        syslog_headers = {}
        leef_headers = {}
        # Split the event by delimiter
        event_split = event.split(raw_config[0][LEEF_TO_JSON][DELIMITER])
        if raw_config[0][LEEF_TO_JSON][SYSLOG_HEADER_PRESENT]:
            header = event_split[0]
            # pass the header and header fields which we got from config
            syslog_headers = parse_syslog_headers(header, raw_config[0][LEEF_TO_JSON][SYSLOG_HEADER_FIELDS])
        # pass the field names from config and event split list
        leef_headers = parse_leef_headers(raw_config[0][LEEF_TO_JSON][SYSLOG_HEADER_FIELDS], raw_config[0][LEEF_TO_JSON][LEEF_HEADER_FIELDS], event_split)
        data = event_split[-1]
        # split the data using the delimeter provided in configuration
        if raw_config[0][LEEF_TO_JSON][PAYLOAD_DELIMITER]:
            datalist = data.split(raw_config[0][LEEF_TO_JSON][PAYLOAD_DELIMITER])
            payload = parse_data(datalist)
        event = {}
        syslog_headers.update(leef_headers)
        event.update(syslog_headers)
        event[PAY_LOAD] = payload

        json_events.append(event)
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
        if check_date_time_present(header.split(COLON)[0]):
            for index in range(len(header_fields.split(COMMA))):
                syslog_header_dict[header_fields.split(COMMA)[index]] = header.split(COLON)[index]
            status = True
    except ValueError:
        pass
        # if timestamp is not present in event, prepare a syslog header dict
        if not status:
            for index in range(len(header_fields.split(COMMA)) - 1):
                syslog_header_dict[header_fields.split(COMMA)[index + 1]] = header.split(COLON)[index]

    return syslog_header_dict


def parse_leef_headers(syslog_h_present: str, leef_header: str, data_list: List[str]) -> Dict[str, Any]:
    """Map the leef headers with fields.

    :param leef_header: leef_header field names
    :type leef_header: str
    :param leef_header: leef_header field names
    :type leef_header: str
    :param event_list: List of the data in events
    :type event_list: List[str]
    :return: Dictionary where leef headers will be present
    :rtype: Dict[str, Any]
    """
    leef_header_dict = {}
    leef_header_list = leef_header.split(COMMA)
    if syslog_h_present:
        leef_header_dict[leef_header_list[0]] = data_list[0].split(" ")[0]
    # read the leef_header_field names and create a dictionary
        for element, index in zip(leef_header_list[1:], range(1, len(data_list))):
            leef_header_dict[element] = data_list[index]
    else:
        # read the leef_header_field names and create a dictionary
        for element, index in zip(leef_header_list, range(1, len(data_list))):
            leef_header_dict[element] = data_list[index]

    return leef_header_dict

def parse_data(datalist: List[str]) -> Dict[str, Any]:
    """Map data and add it as a dictionary."""
    json_event = {}
    index = 0
    while index < len(datalist):
        if EQUAL in datalist[index]:
            item = datalist[index].split(EQUAL)
            json_event[item[0]] = EQUAL.join(item[1:])
        else:
            datalist1 = datalist[index - 1]
            count = 0
            for inner_index in range(index, len(datalist)):
                count += 1
                if EQUAL not in datalist[inner_index]:
                    datalist1 = datalist1 + SPACE_CHAR + datalist[inner_index]
                elif SLASH_EQUAL in datalist[inner_index]:
                    datalist1 = datalist1 + SPACE_CHAR + datalist[inner_index].replace(DOUBLE_SLASH, "")
                else:
                    break
            json_event[datalist[index - 1].split(EQUAL)[0]] = SLASH_EQUAL.join(datalist1.split(EQUAL)[1:])
            index += count - 2
        index += 1
    return json_event
