from sac_log_converter.utils import convert_time_to_format


def convert_leef_to_json(config, events):
    json_events = [] 
    for event in events:
        result = {}
        event = event.split(config["delimeter"])
        if config["syslog_header_is_present"]:
            syslog_headers = event[0].split(" ")
            for index in range(len(syslog_headers)-1):
                if result[config["syslog_headers"][index]] == "timestamp":
                    result[config["syslog_headers"][index]] = convert_time_to_format(syslog_headers[index])
                else:
                    result[config["syslog_headers"][index]] = syslog_headers[index]
            
                
        if not len(config["leef_headers"]) == len(event[0:-1]):
            raise Exception("Leef headers does not match to events")
        else:
            result[config]["LEEF_headers"][index] = LEEF_headers[index]