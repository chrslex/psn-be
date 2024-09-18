from flask import Blueprint
customer_bp = Blueprint('customer_bp', __name__)

from repository.customer.create import *
from repository.customer.get import *