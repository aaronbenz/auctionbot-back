# -*- coding: utf-8 -*-
"""User models."""
from AuctionBot.database import Column, Model, SurrogatePK, db, reference_col, relationship

class Bids(SurrogatePK, Model):
    """A role for a user."""

    __tablename__ = 'bids'
    price = Column(db.DECIMAL(12), unique=True, nullable=False)
    timestamp = Column(db.DECIMAL(8), unique=True, nullable=False)
    user_id = reference_col('users', nullable=True)
    user = relationship('User', backref='bids')

    item_id = reference_col('items', nullable=True)
    item = relationship('Item', backref='bids')

    def __init__(self, name, **kwargs):
        """Create instance."""
        db.Model.__init__(self, name=name, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<Role({name})>'.format(name=self.name)