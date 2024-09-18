from flask import jsonify, g
from repository.customer import customer_bp
from collections import OrderedDict

# READ all customers
@customer_bp.route('/', methods=["GET"])
def get_customers():
    connection = g.db_connection
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute("SELECT ID, title, name, gender, phone_number, image, email, created_at, updated_at FROM Customer")
    customers = cursor.fetchall()
    cursor.close()
    connection.close()

    return jsonify(customers)

@customer_bp.route("/<int:id>", methods=["GET"])
def get_customer_detail(id):
    connection = g.db_connection
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM Customer WHERE ID = %s", (id,))
    customer = cursor.fetchone()
    cursor.close()
    connection.close()

    if customer:
        return jsonify(customer)
    else:
        return jsonify({'error': 'Customer not found'}), 404