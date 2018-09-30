from db import db
from sqlalchemy.orm import relationship


class SingleElement(db.Model):
    """
    pojedynczy element na stronie (tekst albo obrazek)
    """
    __tablename__ = 'single_element'

    id = db.Column(db.Integer, primary_key=True)
    """ typ elementu -> 0 = text, 1 = obrazek, taki enum"""
    type = db.Column(db.Integer)
    text = db.Column(db.String)
    src = db.Column(db.String)
    domain_id = db.Column(db.Integer, db.ForeignKey('domain.id'))
    domain = relationship("Domain", back_populates="elements")

    def __init__(self, type, text, src, domain):
        self.type = type
        self.text = text
        self.src = src
        self.domain = domain

    @classmethod
    def delete_all_elements_for_domain(cls, domain):
        list_of_elements = cls.query.filter_by(domain=domain).all()
        for element in list_of_elements:
            db.session.delete(element)
        db.session.commit()

    def json(self):
        if self.type == 0:
            item_type = "text"
            return {"type": item_type, "text": self.text}
        else:
            item_type = "image"
            return {"type": item_type, "img_src": self.src}

