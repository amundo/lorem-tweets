# a lorem ipsum tweet search engine

This began on a fluke, I was messing around with ChatGPT to see if it could help me write a JSON-based search interface to a sqlite database. The conversation is included in `ChatGPT_20230328T000113443Z_PythonserverforSQLite.md`.

Suffice it to say it didn't take long to get it running, so I figured I’d amp it up to 1million lines and see how that went.

That worked too, amazingly enough.

To try it, do this:

0. make sure you have python3, sqlite3, and the lorem package installed.
1. run `build-1m-db.py`. this will create a 150MB file called `tweets-1m.db`.
2. run `python3 search-tweets.py`
3. go to http://localhost/tweets/ in your browser, and search. 
4. the results should render.

There is no pagination, so if your browser starts smoking, don’t blame me!

🐍
