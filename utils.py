import sys
from datetime import datetime
from tqdm import tqdm

def unix_to_datetime(unixtime: int):
    return datetime.fromtimestamp(unixtime).strftime('%Y-%m-%d-%H-%M-%S')

def datetime_to_unix(date: datetime):
    return int((datetime(*list(map(int, date.split('-')))) - datetime(1970, 1, 1)).total_seconds())


def get_date_range(data: list):
    assert 'created_utc' in data[0]
    min_time = sys.maxsize
    max_time = 0
    for comment in tqdm(data):
        unixtime = comment['created_utc']
        if unixtime < min_time:
            min_time = unixtime
        if unixtime > max_time:
            max_time = unixtime
    return min_time, max_time
