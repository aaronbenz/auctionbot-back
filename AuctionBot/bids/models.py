# -*- coding: utf-8 -*-
"""User models."""
from AuctionBot.database import Column, Model, SurrogatePK, db, reference_col, relationship
from time import time
class Bids(SurrogatePK, Model):
    """A role for a user."""

    __tablename__ = 'bids'
    price = Column(db.DECIMAL(12),nullable=False)
    timestamp = Column(db.DECIMAL(12), nullable=False, default=int(time()))
    user_id = reference_col('users', nullable=True)
    user = relationship('User', backref='bids')

    item_id = reference_col('items', nullable=True)
    item = relationship('Items', backref='bids')

    def __init__(self, **kwargs):
        """Create instance."""
        db.Model.__init__(self, **kwargs)

    def to_dict(self):
        return {"id": self.id,
                "price": self.price,
                "timestamp": self.timestamp,
                "user": self.user,
                "item_id": self.item_id}

    @staticmethod
    def current_item_bid(item_id):
        return Bids.query.filter(Bids.item_id==item_id).order_by(Bids.timestamp.desc()).first()


    def __repr__(self):
        """Represent instance as a unique string."""
        return '<Bids({name})>'.format(name=self.id)