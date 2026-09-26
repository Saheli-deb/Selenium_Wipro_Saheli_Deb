import sqlite3
import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1",
    timeout=10
)
assert response.status_code == 200
post = response.json()

conn = sqlite3.connect("api_results.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY,
    title TEXT,
    user_id INTEGER
)
""")

cur.execute(
    "INSERT OR REPLACE INTO posts VALUES (?, ?, ?)",
    (post["id"], post["title"], post["userId"])
)
conn.commit()

cur.execute(
    "SELECT id, title, user_id FROM posts WHERE id = ?",
    (post["id"],)
)
row = cur.fetchone()

assert row[0] == post["id"]
assert row[2] == post["userId"]

print("API + SQLite validation: PASS")
conn.close()
