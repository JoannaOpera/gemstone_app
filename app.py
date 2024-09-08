from flask import Flask, jsonify
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env


app = Flask(__name__)

# Function to connect to the PostgreSQL database
def connect_db():
    conn = psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT')
    )
    return conn


@app.route('/')
def home():
    return "Connected to Gemstone Properties Database!"

@app.route('/gemstones', methods=['GET'])
def get_gemstones():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM gemstones;")
    gemstones = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(gemstones)

if __name__ == '__main__':
    app.run(debug=True)

