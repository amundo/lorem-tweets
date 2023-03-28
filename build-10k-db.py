import sqlite3
import random
import lorem
import uuid


conn = sqlite3.connect('tweets.db')
c = conn.cursor()

# create table
c.execute('''CREATE TABLE tweets
             (id TEXT PRIMARY KEY,
             text TEXT,
             user TEXT,
             timestamp INTEGER)''')


# insert 10,000 randomly generated tweets
for i in range(10000):
    tweet = (
        str(uuid.uuid4()),  # generate a unique UUID for the tweet ID,
        lorem.sentence(),
        'user{}'.format(random.randint(1, 100)),
        random.randint(1617206400, 1648742400)  # random timestamp between 2021-04-01 and 2023-03-30
    )
    c.execute('INSERT INTO tweets VALUES (?,?,?,?)', tweet)

# commit changes and close connection
conn.commit()
conn.close()

