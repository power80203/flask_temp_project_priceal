from flask import Flask, render_template, request
from models.item import Item
from views.items import item_blueprint
from views.users import user_blueprint

app = Flask(__name__)

app.register_blueprint(item_blueprint, url_prefix='/items')
app.register_blueprint(user_blueprint, url_prefix='/users')



if __name__ == '__main__':
    app.Debug = True
    app.run(port = 8150)