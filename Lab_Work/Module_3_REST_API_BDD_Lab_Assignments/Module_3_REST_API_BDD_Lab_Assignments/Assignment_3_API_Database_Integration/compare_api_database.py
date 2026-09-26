import sqlite3
import requests

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute(
    "CREATE TABLE expected_posts (id INTEGER, title TEXT)"
)
cur.execute(
    "INSERT INTO expected_posts VALUES (?, ?)",
    (1, "sunt aut facere repellat provident occaecati")
)
conn.commit()

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1",
    timeout=10
)
assert response.status_code == 200

cur.execute(
    "SELECT title FROM expected_posts WHERE id = ?",
    (1,)
)
expected = cur.fetchone()[0]

assert response.json()["title"] == expected
print("API/database comparison: PASS")
conn.close()
