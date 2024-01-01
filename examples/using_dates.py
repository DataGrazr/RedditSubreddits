import urllib.request
import json
import arrow
from datetime import datetime
from pprint import pprint

url = "https://raw.githubusercontent.com/DataGrazr/RedditSubreddits/main/data/latest/core_data.json"

print(f"Retrieving data from {url}")
with urllib.request.urlopen(url) as url_data:
    data = json.load(url_data)
    row = data[0]
    
    datetime_string = row['date']
    datetime_object = datetime.strptime(datetime_string, '%Y-%m-%d %H:%M:%S')
    
    arrow_object = arrow.get(datetime_string, 'YYYY-MM-DD')
    
    print(f"Python datetime object: {datetime_object}")
    print(f"Python arrow object: {arrow_object}")
