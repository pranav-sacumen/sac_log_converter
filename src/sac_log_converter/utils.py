from datetime import datetime


def convert_time_to_format(str_time, format):
    """Convert the timestamp into specified format."""
    return datetime.strftime(str_time, format)


def check_date_time_present(time) -> datetime:
    """Check if the timestamp is present."""
    return datetime.strptime(time, '%Y') or datetime.strptime(time, '%b %d %y') or datetime.strptime(time, '%b %d %Y') or datetime.strptime(time, '%B %d %y') or datetime.strptime(time, '%B %d %Y')
