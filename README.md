![Static Badge](https://img.shields.io/badge/frequency-daily-purple) ![Dynamic JSON Badge](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2FDataGrazr%2FRedditSubreddits%2Fmain%2Fdata%2Fproject_stats.json&query=%24%5B%3A1%5D.num_rows&label=num%20records&color=blue) ![Dynamic JSON Badge](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2FDataGrazr%2FRedditSubreddits%2Fmain%2Fdata%2Fproject_stats.json&query=%24%5B%3A1%5D.min_date&label=min%20date&color=white) ![Dynamic JSON Badge](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2FDataGrazr%2FRedditSubreddits%2Fmain%2Fdata%2Fproject_stats.json&query=%24%5B%3A1%5D.max_date&label=max%20date&color=white)


# DataGrazr Dataset: Reddit - Subreddits

This `Reddit - Subreddits` dataset represents all "top" subreddits (as defined by the Reddit API) with information about subscribers, id, created date, and more. This dataset typically includes around 4,300 rows of data per time period and data is collected every day.

> **A DataGrazr Dataset**  
> This dataset is part of the DataGrazr family of datasets. DataGrazr is an effort to provide data in a highly usable, portable, and accessible format for any use-case. DataGrazr provides many free (forever) datasets, as well as premium (paid) datasets, and consulting services for custom dataset creation.
> 
> Other datasets in this family include:
> * [Reddit - Subreddits](https://github.com/DataGrazr/RedditSubreddits) -- 🚀 You Are Here
> * [Reddit - Posts](https://github.com/DataGrazr/RedditPosts)
> 
> For more information visit our website.

**Useful Reference URLs (from these docs):**
* [Python peewee documentation](https://docs.peewee-orm.com/en/latest/)
* [sqlite3 command line interface documentation](https://sqlite.org/cli.html)
* [Google Sheets IMPORTDATA documentation](https://support.google.com/docs/answer/3093335?hl=en)
* [Datawrapper 3rd party visualization tool](https://www.datawrapper.de/charts)

## 🛠️ Schema

Each row in this dataset represents a single Subreddit at a single point in time using daily granularity. 

| Field                 | Description |
| -----                 | -----------|
| `date`                | The UTC datetime that the row was collected, formatted as `YYYY-MM-DD`. |
| `id`                  | The id of the Subreddit. |
| `display_name`        | The Subreddit display name. |
| `num_subscribers`     | Number of subscribers at the time of collection. |
| `nsfw`                | Whether or not the subreddit is marked over18, `0` represents False and `1` represents True. |
| `created`             | The Unix timestamp of the subreddit creation. |
| `created_date`        | The created date formatted as a `YYYY-MM-DDTHH:mm:ssZ` string. |


## 📖 Contents

The contents of this dataset are published in sqlite3, JSON, and CSV formats for various purposes.

| Item | Description  |
| ----- | -----------|
| `data.db` | There is a single sqlite3 binary at `./data/data.db` with a single `core_data` table. This table contains all of the core data for the data set in its raw form, as defined by the schema above. |
| `core_data.csv (.json)` | The entirety of the core data table is exported to `./data/core_data.csv` and `./data/core_data.json` whenever the dataset is updated. This is useful if you'd like to skip mounting a sqlite3 binary to leverage this data. |
| `num_subreddits.csv (.json)` | This export simply counts the number of subreddits counted during each day. This dataset isn't super interesting and is generally used to track the health of the data set over time. It's expected to be around 4,300 tracked per day. |
| `project_stats.csv (.json)` | This is another metadata export that shows high level project statistics, including the total number of rows contained in the dataset, the earliest date, and the latest date. |
| `change_in_subscribers.csv (.json)` | This is a derivative dataset that tracks subscriber changes over times. The intervals supported are `24 hours`, `3 days`, `7 days`, `14 days`, `30 days`, `3 months`, `6 months`, and `1 year`. Each of these is tracked in a separate column next to the date, display_name, and subscriber count on the date listed in the date column. |
| `YYYY/MM/DD/core_data.csv (.json)` | In addition to the master data sets, there is a time filtered copy of core_data at each year, month, and day. This serves as a much smaller dataset that can be used in cases where the entire set is not required. |

Here are some example paths that cover most of the exported data:

* `./data/data.db`
* `./data/core_data.csv (.json)`
* `./data/change_in_subscribers.csv (.json)`
* `./data/num_subreddits.csv (.json)`
* `./data/latest/core_data.csv (.json)`
* `./data/2023/core_data.csv (.json)`
* `./data/2023/12/core_data.csv (.json)`
* `./data/2023/12/29/core_data.csv (.json)`

## 🥼 Example Uses

This dataset contains many different ways to use the data that's included, here are a few visual examples of how this dataset can be leveraged.

### Changes in Rank of Top 10 Subreddits (24h)

> Coming Soon

### Changes in Subscribers for Top 15 Subreddits (24h)

![Alt text](img/subscriber_changes.png)

## 🧑‍🏫 How to Use

There are three recommended ways to consume this dataset:
1. Cloning this repository and using the sqlite3 CLI directly
2. Cloning this repository and programmatically mounting the data.db sqlite3 database
3. Using GitHub's raw endpoints to ingest the data into tools and/or code

### Linux sqlite3 Command Line

The simplest way to consume the `data.db` artifact is via the [sqlite3 command line interface](https://sqlite.org/cli.html) that can be installed in Linux via `apt-get install sqlite3` or `yum install sqlite3`. This provides a flexible and direct interface to the dataset, but requires the Linux CLI to execute. This method is a great intermediate step that can be used to export the data to whatever format you'd like, or run whatever custom query you want.

#### Example Command: Export All Data as CSV

```
$ sqlite3 -header -csv ./data/data.db 'select * from core_data ORDER BY date DESC;'
```

```
date,id,display_name,num_subscribers,nsfw,created,created_date
2023-12-30,zxc8e,mendrawingwomen,78113,0,1555534688,2019-04-17T08:58:08+0000
2023-12-30,zvcd0,ShitpostBR,96577,0,1555449287,2019-04-16T09:14:47+0000
2023-12-30,zqoj7,Whatisthisplane,3846,0,1555258890,2019-04-14T04:21:30+0000
2023-12-30,zna4k,truenas,29836,0,1555098655,2019-04-12T07:50:55+0000
2023-12-30,zioft,sunraybee,105238,0,1554880563,2019-04-10T07:16:03+0000
```

#### Example Command: Export All Data as JSON

```
$ sqlite3 -json ./data/data.db 'select * from core_data ORDER BY date DESC;'
```

```
[
  {
    "date": "2023-12-30",
    "id": "zxc8e",
    "display_name": "mendrawingwomen",
    "num_subscribers": 78113,
    "nsfw": 0,
    "created": 1555534688,
    "created_date": "2019-04-17T00:00:00+0000"
  },
  ...
]
```

#### Example Command: Export All Data for a Single Subreddit as CSV

```
sqlite3 -header -csv ./data/data.db 'select * from core_data WHERE display_name = "pics" ORDER BY date DESC;'
```

```
date,id,display_name,num_subscribers,nsfw,created,created_date
2023-12-30,2qh0u,pics,30408428,0,1201221069,2008-01-25T00:00:00+0000
2020-06-16,2qh0u,pics,30408389,0,1201221069,2008-01-25T00:00:00+0000
2007-12-27,2qh0u,pics,30408390,0,1201221069,2008-01-25T00:00:00+0000
```

### Using GitHub's Raw URLs

Another way to consume this dataset is via raw URLs. GitHub provides a raw URL to all artifacts in a repository which looks like `https://raw.githubusercontent.com/DataGrazr/RedditSubreddits/main/data/latest/core_data.json`. Data from these URLs can be retrieved programmatically as though it were a standard JSON endpoint which cuts the need for server infrastructure in simple cases. This can also be used as an ingestion method, or direct access method using some of the methods explained below.


#### Example Command: Retrieve Raw Data via Requests

An example script can be found in `examples/raw_data_requests.py` and demonstrates how easy it is to pull data into a Python (or other) script using simple requests. This script can be run via `python ./examples/raw_data_requests.py`

```Python
import urllib.request
import json
from pprint import pprint

url = "https://raw.githubusercontent.com/DataGrazr/RedditSubreddits/main/data/latest/core_data.json"

print(f"Retrieving data from {url}")
with urllib.request.urlopen(url) as url_data:
    data = json.load(url_data)
    print(f"Got {len(data)} records back, printing the first 10...")
    pprint(data[0:10])
```

#### Using Raw Data as Sources in 3rd Party Tooling

Many 3rd party tools allow linking to web hosted CSV or JSON files, which is a perfect usecase for these raw URLs. Here are a few examples of tools that support this type of importing.

##### Google Sheets

Google Sheets has an `IMPORTDATA(url)` function that can be used to pull a CSV file from a raw URL into a live Google Sheet. Google's documentation on this function is [here](https://support.google.com/docs/answer/3093335?hl=en).

![](./img/google_sheets_import.png)

This will import the CSV as a table, which can be used for charting, formatting, parsing, etc. This URL is _live_, which means that auto-refreshing dashboards and visualizations can be built in Sheets using this method.

![](./img/google_sheets_data.png)

##### Datawrapper

Datawrapper is a web based visualization tool that can be seen at https://www.datawrapper.de/charts. Within the chart builder an external URL can be used as a data source.

![](./img/datawrapper.png)

### Python peewee

Another, more advanced method to programmatically leverage this dataset is via Python's peewee module. Python peewee is an excellent ORM module that works out of the box with sqlite3 (which is what the `data.db` artifact is built with). 

Python peewee provides Python "wrappers" around the sqlite3 .db file and will handle connecting and generating SQL for you. This can dramatically simplify the complexity of a database centered application. Included below is the model that is used within this data set. Additionally an example script is provided at `examples/peewee.py` as a starting point for using peewee in concert with this dataset. 

_Make sure you pip install peewee before attempting to run this example script._

```Python
class Subreddit(Model):
    date = DateTimeField()
    id = CharField()
    display_name = CharField()
    num_subscribers = IntegerField()
    nsfw = BooleanField()
    created = IntegerField()
    created_date = DateTimeField()
    
    class Meta:
        db_table = "core_data"
        database = database
        
        indexes = (
            (('date', 'id'), True),
        )
```

This example script can be run with `python examples/peewee.py` from the root of this dataset.

```Python
import os
from peewee import *

# We have to do this path detection because we don't know whether
# the example script will be run from within /examples or from the 
# root of the repository.
file_path = os.path.abspath(os.path.dirname(__file__))
db = SqliteDatabase(f'{file_path}/../data/data.db')
db.connect()

# This class can be pasted into any Python script which leverages peewee
class Subreddit(Model):
    date = DateTimeField()
    id = CharField()
    display_name = CharField()
    num_subscribers = IntegerField()
    nsfw = BooleanField()
    created = IntegerField()
    created_date = DateTimeField()
    
    class Meta:
        db_table = "core_data"
        database = db
        
        indexes = (
            (('date', 'id'), True),
        )

# Print out some details from the top 100 rows when ordered by date (descending)
for subreddit in Subreddit.select().order_by(Subreddit.date.desc()).limit(100):
    print(f"[{subreddit.date}] {subreddit.display_name} ({subreddit.num_subscribers})")
```


### Parsing sqlite3 Dates With This Dataset

sqlite3 doesn't actually store data as a datetime object, instead it supports a few different integer or string formats, which are [documented here](https://www.sqlite.org/lang_datefunc.html). The dates in all DataGrazr projects are stored in a UTC-only string sortable format, but doing anything beyond sorting requires additional logic.

The `arrow` module is a great datetime library available for Python, but not everyone wants to rely on an additional module for their project. Here's an example script that contains both native datetime parsing of these date fields as well as arrow parsing. This example can be run with `python ./examples/using_dates.py` from the root of this dataset.

```Python
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
```
