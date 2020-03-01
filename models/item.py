import requests
from bs4 import BeautifulSoup
import re
import uuid
from common.database import Database


class Item:

    def __init__(self, url, tag_name, query, _id = None):
        self.url = url
        self.tag_name = tag_name
        self.query = query
        #
        self.collection = "items"
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "Item {} ".format(self.url)

    def load_price(self):
        res = requests.get(self.url)

        content = res.content

        soup = BeautifulSoup(content, 'html.parser')

        element = soup.find(self.tag_name, self.query).text.strip()


        pattern = re.compile(r"(\d?,?\d\d\d.\d\d)") #加上?代表說是不一定要有
        match = pattern.search(element)

        self.price = float(match.group(1).replace(",",""))

        return self.price

    def saveToDb(self):
        Database.insert(self.collection, self.json())


    def json(self):
        return {
            "_id" : self._id,
            "url" : self.url,
            "tag_name" : self.tag_name,
            "query" : self.query,
        }


    @classmethod
    def get_all(cls):
        items_from_db = Database.find('items', {})
        return [cls(**item) for item in items_from_db] 

    @classmethod
    def get_by_id(cls, id):
        item_json = Database.find_one("items", {"_id":id})
        return cls(**item_json)



"""
#########################################################
#add comment#
#########################################################

url = 'https://www.johnlewis.com/john-lewis-partners-frame-leather-office-chair-natural-oak/p4273087'

Tag_name = "p"
Query = {'class':'price price--large'}

res = requests.get(url)

content = res.content

soup = BeautifulSoup(content, 'html.parser')

element = soup.find(Tag_name, Query).text.strip()


pattern = re.compile(r"(\d?,?\d\d\d.\d\d)") #加上?代表說是不一定要有
match = pattern.search(element)

price = float(match.group(1).replace(",",""))

"""
