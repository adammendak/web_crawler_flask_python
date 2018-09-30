from db import db
from sqlalchemy.orm import relationship
from datetime import datetime
from model.single_element import SingleElement


class Domain(db.Model):
    """
    encja domeny internetowej
    """
    __tablename__ = 'domain'

    id = db.Column(db.Integer, primary_key=True)
    """ tylko jeden wpis w bazie na dana domene"""
    name = db.Column(db.String(2000), unique=True)
    count = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    elements = relationship("SingleElement", cascade="all,delete")

    def __init__(self, name):
        self.name = name
        self.count = 0  # ile razy crawler pobierał dane z tej strony
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update(self):
        self.count = self.count + 1
        self.updated_at = datetime.now()

    def json(self):
        elements_list = []
        for element in self.elements:
            elements_list.append(SingleElement.json(element))

        return {'name': self.name, 'count': self.count,
                'created_at': str(self.created_at), 'updated_at': str(self.updated_at),
                'elements': elements_list}

    @staticmethod
    def save_domain(domain):
        db.session.add(domain)
        db.session.commit()

    @staticmethod
    def find_by_name(name):
        return Domain.query.filter_by(name=name).first()

