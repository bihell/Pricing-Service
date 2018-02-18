from flask import Blueprint, render_template, request, session

from src.models.alerts.alert import Alert
from src.models.items.item import Item

alert_blueprint = Blueprint('alerts', __name__)


@alert_blueprint.route('/')
def index():
    return "This is the alerts index"


@alert_blueprint.route('/new', methods=['GET', 'POST'])
# @user_decorators.requires_login
def create_alert():
    if request.method == 'POST':
        name = request.form['name']
        url = request.form['url']
        price_limit = float(request.form['price_limit'])

        item = Item(name, url)
        item.save_to_mongo()

        alert = Alert(session['email'], price_limit, item._id)
        alert.load_item_price()  # This already saves to MongoDB

    # What happens if it's a GET request
    return render_template("alerts/new_alert.jinja2")  # Send the user an error if their login was invalid


@alert_blueprint.route('/deactivate/<string:alert_id>')
def deactivate_alert(alert_id):
    pass


@alert_blueprint.route('/<string:alert_id>')
# @user_decorators.requires_login
def get_alert_page(alert_id):
    return render_template('alerts/alert.jinja2', alert=Alert.find_by_id(alert_id))


@alert_blueprint.route('/for_user/<string:user_id>')
def get_alerts_for_user(user_id):
    pass
