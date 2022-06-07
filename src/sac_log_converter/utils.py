from datetime import datetime
def convert_time_to_format(str_time, format):
    return datetime.strftime(str_time, format)