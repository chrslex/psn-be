from flask import Flask,request, jsonify, make_response
from repository.db.conn import get_db_connection

app = Flask(__name__)

@app.route('/')
def index():
    db_conn = get_db_connection()
    cursor = db_conn.cursor()
    cursor.execute("SELECT DATABASE();")
    db_name = cursor.fetchone()
    cursor.close()
    db_conn.close()
    return jsonify({"message": f"Connected to {db_name[0]}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0')