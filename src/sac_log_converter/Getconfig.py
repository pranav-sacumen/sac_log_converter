from unittest import result
import yaml
from yaml.loader import SafeLoader

# Open the file and load the file
with open('/home/dell/sac_log_converter/config/config.yaml') as f:
    data = yaml.load(f, Loader=SafeLoader)
    # print(data)
    subs='present'
    # res = [i for i in data if subs in i]
    r = data[0]
    print (data[0]['syslog headers']['present'])
    if data[0]['syslog headers']['present'] == 1:
        print("value exist for present")
    else:
        raise ValueError("value not found")
    
    if data[0]['syslog headers']['fields'] == 'timestamp,hostname':
        print("value exist for fields")
    else:
        raise ValueError("value not found")  
    print (data[1]['time format'])
    if data[1]['time format'] == 'yyyy-MM-ddTHH:mm:ss.SSSZ.':
        print("value exist for time format")
    else:
        raise ValueError("value not found")
          
    if data[2]['LEEF headers']['fields'] == 'Version,Vendor,Product,Version,EventID':
        print("value exist for leef header fields")
    else:
        raise ValueError("value not found")
    
    if data[3]['delimiter'] == '|':
        print("value exist for delimiters")
    else:
        raise ValueError("value not found")
          


class LEEF_Logger:
    """LEEF LOGGER"""
    

    # LEEF Headers
    version_major = None
    version_minor = None
    product_vendor = None
    product_name = None
    product_version = None

    def __init__(self, product_vendor, product_name, product_version,
                 version_major=1, version_minor=0, delimiter="\t"):
        """ Define the LEEF Headers """

        self.version_major = version_major
        self.version_minor = version_minor
        self.product_vendor = product_vendor
        self.product_name = product_name
        self.product_version = product_version

        if delimiter not in ['\t', '|', '^']:
            raise ValueError("Delimeter must be '\\t', '|' or '^'")
        self.delimiter = delimiter

    def logEvent(self, event_id, keys):
        """
        Log an event
        """
        return self._createEventString(event_id, keys)

    def _createEventString(self, event_id, keys):
        header = self._createHeader(event_id)
        values = sorted([(str(k) + "=" + str(v))
                         for k, v in iter(keys.items())])

        payload = '\t'.join(values)

    def _createHeader(self, event_id):
        return "LEEF:{0}.{1}|{2}|{3}|{4}|{5}|". \
               format(self.version_major,
                      self.version_minor,
                      self.product_vendor,
                      self.product_name,
                      self.product_version,
                      event_id
                      )

    