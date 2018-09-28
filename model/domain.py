from model import abstract_timestampable_entity
from db import db


class Domain(db.Model, abstract_timestampable_entity):
    """
    encja opisująca stronę internetową
    """
    __tablename__ = 'domain'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    count = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self, name):
        #  co z id ? ogarnac
        self.name = name
        self.count = 0  # ile razy crawler pobierał dane z tej strony

    def increment_count(self):
        self.count = self.count + 1
