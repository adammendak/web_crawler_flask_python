from db import db
from datetime import datetime


class Domain(db.Model):
    """
    encja opisująca stronę internetową
    """
    __tablename__ = 'domain'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    count = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self, name):
        self.name = name
        self.count = 0  # ile razy crawler pobierał dane z tej strony
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def increment_count(self):
        self.count = self.count + 1

    def json(self):
        return {'id': self.id, 'name': self.name, 'count': self.count,
                'created_at': str(self.created_at), 'updated_at': str(self.updated_at)}

    @staticmethod
    def save_domain(domain):
        db.session.add(domain)
        db.session.commit()

    @staticmethod
    def find_by_name(name):
        return Domain.query.filter_by(name=name).first()

