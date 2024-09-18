
from flask import request, jsonify, g
import datetime
from . import customer_bp

# Create Customer
@customer_bp.route('/', methods=["POST"])
def create_customer():
    data = request.get_json()
    connection = g.db_connection
    cursor = connection.cursor()


    try:
        sql = """
        INSERT INTO Customer (title, name, gender, phone_number, image, email, created_at, updated_at)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        now = datetime.datetime.now()
        cursor.execute(sql, (data['title'], data['name'], data['gender'], data['phone_number'],
                             data['image'], data['email'], now, now))
        connection.commit()
        return jsonify({'message': 'Customer created successfully!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        connection.close()