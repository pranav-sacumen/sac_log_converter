"""Converter code from leef to json."""
from getConfig import parse_headers


def convert_leef_to_json(raw_config, events_list):
    """Convert the leef format into json."""
    # json_events = []
    if raw_config[0]['leef_to_json']['syslog_headers_present']:
        for event in events_list:
            header = event.split('|')[0]
            syslog_headers = parse_headers(header, raw_config[0]['leef_to_json']['syslog_headers_fields'])
            print(syslog_headers)
