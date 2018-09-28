from model import abstract_timestampable_entity
from db import db


class Domain(db.Model, abstract_timestampable_entity):
    """
    encja opisująca stronę internetową
    """
    __tablename__ = 'domain'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    count = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.count = 0  # ile razy crawler pobierał dane z tej strony

    def increment_count(self):
        self.count = self.count + 1

    def json(self):
        return {'id': self.id, 'name': self.name, 'count': self.count,
                'created_at': self.created_at, 'updated_at': self.updated_at}

    @staticmethod
    def save_domain(self, domain):
        db.session.add(domain)
        db.session.commit()

    @staticmethod
    def find_by_name(self, name):
        return Domain.query.filter_by(name=name).first()

