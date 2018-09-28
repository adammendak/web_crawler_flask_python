from model import abstract_timestampable_entity
from db import db


class SingleElement(db.Model, abstract_timestampable_entity):
    """
    pojedynczy element na stronie (tekst albo obrazek)
    """

    __tablename__ = 'single_element'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer)
    text = db.Column(db.String)
    src = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self, type, text, src):
        super().__init__()
        self.type = type
        self.text = text
        self.src = src
