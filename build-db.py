import sqlite3

conn = sqlite3.connect('tweets.db')
c = conn.cursor()

# create table
c.execute('''CREATE TABLE tweets
             (id INTEGER PRIMARY KEY,
             text TEXT,
             user TEXT,
             timestamp INTEGER)''')

# insert sample data
tweets = [
    (1, 'Hello world!', 'JohnDoe', 1630194439),
    (2, 'Python is awesome!', 'JaneSmith', 1630194445),
    (3, 'Just ate a delicious pizza!', 'PizzaLover', 1630194452),
    (4, 'I love hiking!', 'NatureLover', 1630194460),
    (5, 'Working on a new project...', 'TechGuru', 1630194470)
]

c.executemany('INSERT INTO tweets VALUES (?,?,?,?)', tweets)

# commit changes and close connection
conn.commit()
conn.close()

