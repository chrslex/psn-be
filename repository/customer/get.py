from flask import jsonify, g
from repository.customer import customer_bp
from collections import OrderedDict

# READ all customers
@customer_bp.route('/', methods=["GET"])
def get_customers():
    connection  = g.db_connection
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM Customer")
    customers = cursor.fetchall()
    cursor.close()
    connection.close()

    if customers:
        data_dict = map_to_dict(customers)
        return jsonify(data_dict)
    else:
        return jsonify({"error": "User not found"}), 404
    
   


def map_to_dict(customers):
    res = []
    keys = [
        "id", "title", "name", "gender", "phone_number",
        "image", "email", "created_at", "updated_at"
    ]

    for c in customers:
        temp = OrderedDict(zip(keys, c))
        res.append(temp)

    return res