from flask import Flask, render_template, request, Blueprint
from models.item import Item


item_blueprint = Blueprint('items', __name__)

@item_blueprint.route('/')
def index():
    items = Item.get_all()
    return render_template('items/index.html', items=items)


@item_blueprint.route('/new', methods =['GET', 'POST'])
def new_item():
    if request.method == 'POST':
        url = request.form['url']
        tag_name = request.form['tag_name']
        query = request.form['query']
        Item(url, tag_name, query).saveToDb()

    return render_template('items/newitem.html')