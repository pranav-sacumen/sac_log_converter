"""Get the configuration."""
import sys
from time import strftime

import yaml
from pyparsing import alphas
from pyparsing import Combine
from pyparsing import nums
from pyparsing import Optional
from pyparsing import Regex
from pyparsing import string
from pyparsing import Suppress
from pyparsing import Word
from yaml.loader import SafeLoader


def check_config(config_path):
    """check the configuration."""
# Open the file and load the file
    with open(config_path) as f:
        data = yaml.load(f, Loader=SafeLoader)
        print (data[0]['syslog headers']['present'])
        if not data[1]['time format']:
            raise ValueError("value not found")

        if not data[2]['LEEF headers']['fields']:
            raise ValueError("value not found")

        if not data[3]['delimiter']:
            raise ValueError("value not found")
        return data



    class Parser:
        """Parse the configuration."""
        def __init__(self):
            ints = Word(nums)

            # priority
            priority = Suppress("<") + ints + Suppress(">")

            # timestamp
            month = Word(string.ascii_uppercase , string.ascii_lowercase, exact=3)
            day   = ints
            hour  = Combine(ints + ":" + ints + ":" + ints)

            timestamp = month + day + hour

            # hostname
            hostname = Word(alphas + nums + "_" + "-" + ".")


    def parse(self, line):
        """Parse the syslog."""
        parsed = self.__pattern.parseString(line)

        payload = {}
        payload["priority"]  = parsed[0]
        payload["timestamp"] = strftime("%Y-%m-%d %H:%M:%S")
        payload["hostname"]  = parsed[4]


        return payload

    """ --------------------------------- """

def main():
    """Main function."""
parser = Parser()

if len(sys.argv) == 1:
    print("Usage:\n  $ python xlog.py ./sample.log")
    exit(666)

syslogPath = sys.argv[1]

with open(syslogPath) as syslogFile:
    for line in syslogFile:
      fields = parser.parse(line)
      print(fields)

if __name__ == "__main__":
  main()
