# -*- coding: utf-8 -*-
"""User models."""
from AuctionBot.database import Column, Model, SurrogatePK, db, reference_col, relationship

class Bids(SurrogatePK, Model):
    """A role for a user."""

    __tablename__ = 'bids'
    price = Column(db.DECIMAL(12),nullable=False)
    timestamp = Column(db.DECIMAL(8), nullable=False)
    user_id = reference_col('users', nullable=True)
    user = relationship('User', backref='bids')

    item_id = reference_col('items', nullable=True)
    item = relationship('Items', backref='bids')

    def __init__(self, name, **kwargs):
        """Create instance."""
        db.Model.__init__(self, name=name, **kwargs)

    def to_dict(self):

        return {"id": self.id,
                "price": self.price,
                "timestamp": self.timestamp,
                "user_id": self.user_id,
                "item_id": self.item_id}

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<Bids({name})>'.format(name=self.id)