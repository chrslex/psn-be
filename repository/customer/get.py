from flask import jsonify, g
from repository.customer import customer_bp

# READ all customers
@customer_bp.route('/', methods=["GET"])
def get_customers():
    connection  = g.db_connection
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM Customer")
    customers = cursor.fetchall()
    cursor.close()
    connection.close()

    return jsonify(customers)