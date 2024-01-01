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
