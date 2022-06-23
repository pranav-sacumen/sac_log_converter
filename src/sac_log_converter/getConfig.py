"""Get the configuration."""
# import sys
from logging import Logger as logger
from typing import Dict, Any
# from time import strftime

import yaml

# from pyparsing import alphas
# from pyparsing import Combine
# from pyparsing import nums
# from pyparsing import Optional
# from pyparsing import Regex
# from pyparsing import string
# from pyparsing import Suppress
# from pyparsing import Word
# from yaml.loader import SafeLoader


def get_config(config_path: str) -> Dict[str, Any]:
    """Read the configurations from the yaml file.
    
    :param config_path: configuration file path
    :type config_path: str
    :return: configurations in form of json
    :rtype: Dict[str, Any]"""
    with open(config_path) as yamlfile:
        config = yaml.safe_load(yamlfile)
        #logger.debug(config)
        # print (data[0]['syslog headers']['present'])
        # if not data[1]['time format']:
        #     raise ValueError("value not found")

        # if not data[2]['LEEF headers']['fields']:
        #     raise ValueError("value not found")

        # if not data[3]['delimiter']:
        #     raise ValueError("value not found")
        return config

# c = get_config('C:/Users/DIVYA/Documents/Log Convertor Resuable Library/sac_log_converter-leef-json/config/config.yaml')
# print('c:',c)

    # class Parser:
    #     """Parse the configuration."""
    #     def __init__(self):
    #         ints = Word(nums)

    #         # priority
    #         priority = Suppress("<") + ints + Suppress(">")

    #         # timestamp
    #         month = Word(string.ascii_uppercase , string.ascii_lowercase, exact=3)
    #         day   = ints
    #         hour  = Combine(ints + ":" + ints + ":" + ints)

    #         timestamp = month + day + hour

    #         # hostname
    #         hostname = Word(alphas + nums + "_" + "-" + ".")


    # def parse(self, line):
    #     """Parse the syslog."""
    #     parsed = self.__pattern.parseString(line)

    #     payload = {}
    #     payload["priority"]  = parsed[0]
    #     payload["timestamp"] = strftime("%Y-%m-%d %H:%M:%S")
    #     payload["hostname"]  = parsed[4]


    #     return payload

    # """ --------------------------------- """

# def main():
#     """Main function."""
# parser = Parser()

# if len(sys.argv) == 1:
#     print("Usage:\n  $ python xlog.py ./sample.log")
#     exit(666)

# syslogPath = sys.argv[1]

# with open(syslogPath) as syslogFile:
#     for line in syslogFile:
#       fields = parser.parse(line)
#       print(fields)

# if __name__ == "__main__":
#   main()
