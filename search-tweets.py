from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import sqlite3

DATABASE = 'tweets-1m.db'

class MyHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path.startswith('/tweets/query/'):
            query = self.path.split('/tweets/query/')[1]
            result = self.search_tweets(query)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(result).encode())
        elif self.path == '/tweets':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('tweets.html', 'r') as f:
                self.wfile.write(f.read().encode())
        else:
            self.send_error(404)

    def search_tweets(self, query):
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute("SELECT * FROM tweets WHERE text LIKE ?", ('%{}%'.format(query),))
        rows = c.fetchall()
        tweets = []
        for row in rows:
            tweet = {
                'id': row[0],
                'text': row[1],
                'user': row[2],
                'timestamp': row[3]
            }
            tweets.append(tweet)
        conn.close()
        return {'tweets': tweets}

if __name__ == '__main__':
    httpd = HTTPServer(('localhost', 8000), MyHTTPRequestHandler)
    print('Server running on localhost:8000')
    httpd.serve_forever()
