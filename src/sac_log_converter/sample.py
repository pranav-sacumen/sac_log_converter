import json
import re


class Systemlog:

    def __init__(self):
        pass

    def read_log(self):
        
        f = open('input_sample.txt', 'r')
        log_data = f.read().strip('\n')
        return log_data

    def parse_log(self, log_data):
        
        data = dict()

        cat = re.search('cat=(.+?) ', log_data)
        if cat:
            data['cat'] = cat.group(1)

        cs1Label = re.search('cs1Label=(.+?) ', log_data)
        if cs1Label:
            data['cs1Label'] = cs1Label.group(1)

        cs1 = re.search('cs1=(.+?) ', log_data)
        if cs1:
            data['cs1'] = cs1.group(1)

        cs2Label = re.search('cs2Label=(.+?) ', log_data)
        if cs2Label:
            data['cs2Label'] = cs2Label.group(1)

        cs2 = re.search('cs2=(.+?) ', log_data)
        if cs2:
            data['cs2'] = cs2.group(1)

        cs3Label = re.search('cs3Label=(.+?) ', log_data)
        if cs3Label:
            data['cs3Label'] = cs3Label.group(1)

        cs3 = re.search('cs3=(.+?) ', log_data)
        if cs3:
            data['cs3'] = cs3.group(1)

        cs4Label = re.search('cs4Label=(.+?) ', log_data)
        if cs4Label:
            data['cs4Label'] = cs4Label.group(1)

        cs4 = re.search('cs4=(.+?) ', log_data)
        if cs4:
            data['cs4'] = cs4.group(1)

        cn1Label = re.search('cn1Label=(.+?) ', log_data)
        if cn1Label:
            data['cn1Label'] = cn1Label.group(1)

        cn1 = re.search('cn1=(.+?) ', log_data)
        if cn1:
            data['cn1'] = int(cn1.group(1))

        msg = re.search('msg=(.+?)[.]', log_data)
        if msg:
            data['msg'] = msg.group(1)

        dhost = re.search('dhost=(.+?) ', log_data)
        if dhost:
            data['dhost'] = dhost.group(1)

        dst = re.search('dst=(.+?$)', log_data)
        if dst:
            data['dst'] = dst.group(1)

        return data

    def display_log(self, data):
       
        f = open('output.txt', 'w')
        f.write(json.dumps(data))
        print("Data generated successfully! Please check the output file.\n")


def main():
    
    sl = Systemlog()
    log_data = sl.read_log()
    data = sl.parse_log(log_data)
    sl.display_log(data)


if __name__ == '__main__':
    main()
    