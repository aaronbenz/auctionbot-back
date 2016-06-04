# -*- coding: utf-8 -*-
"""User models."""
import datetime as dt

from AuctionBot.database import Column, Model, SurrogatePK, db, reference_col, relationship

class Items(SurrogatePK, Model):
    """A role for a user."""

    __tablename__ = 'items'
    name = Column(db.String(80), nullable=False)
    image_url = Column(db.String(100), nullable=False)
    expiration_time = Column(db.DECIMAL(16), nullable=False)
    min_bid = Column(db.DECIMAL(8), nullable=False)
    min_increment_bid = Column(db.DECIMAL(8), nullable=False)

    def __init__(self, **kwargs):
        """Create instance."""
        db.Model.__init__(self, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<Items({name})>'.format(name=self.name)