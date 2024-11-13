from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ['DB_HOST'],
        database=os.environ['POSTGRES_DB'],
        user=os.environ['POSTGRES_USER'],
        password=os.environ['POSTGRES_PASSWORD']
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT 'Hello from PostgreSQL!' AS message;")
    message = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return jsonify(message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
