from flask import Flask, request, jsonify
import pymysql
import os

app = Flask(__name__)

DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'project01-mysql-db.ct4u2y42s7n0.ap-south-1.rds.amazonaws.com'),
    'user': os.getenv('DB_USER', 'admin'),
    'password': os.environ['DB_PASSWORD'],
    'db': os.getenv('DB_NAME', 'feedbackdb'),
    'cursorclass': pymysql.cursors.DictCursor
}

@app.route('/')
def health():
    return jsonify({'status': 'Flask is running'})

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    conn = pymysql.connect(**DB_CONFIG)
    with conn.cursor() as cur:
        cur.execute(
            'INSERT INTO feedback (name, email, feedback) VALUES (%s, %s, %s)',
            (data['name'], data['email'], data['feedback'])
        )
    conn.commit()
    conn.close()
    return jsonify({'message': 'Feedback submitted successfully!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
