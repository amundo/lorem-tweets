from http.server import HTTPServer, BaseHTTPRequestHandler
import sqlite3
import json
import re

DATABASE = 'tweets-1m.db'

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        query_match = re.match('/tweets/query/(.*)', self.path)
        if query_match:
            query = query_match.group(1)
            results = self.search_tweets(query)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(results).encode('utf-8'))
        else:
            self.send_error(404, 'Not Found')

    def search_tweets(self, query):
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute("SELECT * FROM tweets WHERE text LIKE ?", ('%'+query+'%',))
        rows = c.fetchall()
        results = []
        for row in rows:
            result = {
                'id': row[0],
                'text': row[1],
                'user': row[2],
                'timestamp': row[3]
            }
            results.append(result)
        conn.close()
        return results

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyRequestHandler)
    httpd.serve_forever()
