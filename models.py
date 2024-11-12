
from database import db

class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    price = db.Column(db.Float, nullable=False)
    inventory_count = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    popularity_score = db.Column(db.Float, default=0.0)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
