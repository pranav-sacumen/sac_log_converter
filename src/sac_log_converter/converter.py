from operator import length_hint
from utils import convert_time_to_format


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
             result[config]["LEEF_headers"][index] = leef_headers[index]

test = "cat=C2 cs1Label=subcat cs1=DNS_TUNNELING cs2Label=vueUrls cs2=https://aws-dev.sacdev.io/alerts?filter=alertId%3D%3D81650 cs3Label=Tags cs3=USA,Finance cs4Label=Url cs4=https://aws-dev.sacdev.io/settings/tir?rules.sort=4%3A1&filter=state%3D%3D2&selected=9739323 cn1Label=severityScore cn1=900 msg=Malicious activity was reported in CAAS\= A threat intelligence rule has been automatically created in DAAS. dhost=bad.com dst=1.1.1.1"


json_event= {}
test = test.split(" ")
print(test)
index=0
while index < len(test):
    if "=" in test[index]:
        item = test[index].split("=")
        json_event[item[0]] = "=".join(item[1:])
    else:
        test1 = test[index-1]
        count = 0
        for inner_index in range(index, len(test)):
            count +=1
            if "\=" in test[inner_index] or "=" not in test[inner_index]:
                test1 = test1 + " "+ test[inner_index]
            else:
                break
        json_event[test[index-1].split("=")[0]] = "=".join(test1.split("=")[1:])
        index += count-2
    index+=1
print(json_event)


    

