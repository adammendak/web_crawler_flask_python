from db import db


class SingleElement(db.Model):
    """
    pojedynczy element na stronie (tekst albo obrazek)
    """
    __tablename__ = 'single_element'

    id = db.Column(db.Integer, primary_key=True)
    """ typ elementu -> 0 = text, 1 = obrazek"""
    type = db.Column(db.Integer)
    text = db.Column(db.String)
    src = db.Column(db.String)

    def __init__(self, type, text, src):
        self.type = type
        self.text = text
        self.src = src
