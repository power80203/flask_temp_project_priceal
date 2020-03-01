import uuid
from models.item import Item
from common.database import Database


class Alert:

    def __init__(self, item_id, price_limit, _id = None):
        self.item_id = item_id
        self.item = Item.get_by_id(item_id)
        self.price_limit = price_limit
        self.collection = "alerts"
        self._id = uuid.uuid4().hex if _id is None else _id

    def json(self):
        return {
            "_id":self._id,
            "item_id": self.item_id,
            "price_limit":self.price_limit
        }
        

    def saveToDb(self):
        Database.insert(self.collection, self.json())

    def load_item_price(self):
        return self.item.load_price()

    def notify_if_price_reached(self):
        if self.load_item_price() < self.price_limit:
            print("Item {} has reached a price under {}".format(self.item, self.price_limit))

    @classmethod    
    def all(cls):
        alert_from_db = Database.find("alerts", {})
        return[ cls(**alert) for alert in alert_from_db]


