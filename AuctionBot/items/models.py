# -*- coding: utf-8 -*-
"""User models."""
import datetime as dt

from AuctionBot.database import Column, Model, SurrogatePK, db, reference_col, relationship
from AuctionBot.bids.models import Bids

#Status Enums
ACTIVE = 1
CLOSED = 2
HIDDEN = 3 #not started or not active, but not closed

class Items(SurrogatePK, Model):
    """A role for a user."""

    __tablename__ = 'items'
    name = Column(db.String(80), nullable=False)
    image_url = Column(db.String(100), nullable=False)
    expiration_time = Column(db.DECIMAL(16), nullable=False)
    min_bid = Column(db.DECIMAL(8), nullable=False)
    min_increment_bid = Column(db.DECIMAL(8), nullable=False)
    status = Column(db.Integer(), default=1, nullable=False)

    def __init__(self, **kwargs):
        """Create instance."""
        db.Model.__init__(self, **kwargs)


    def to_dict(self):
        bid = Bids.current_item_bid(self.id)
        return {"id": self.id,
                "title": self.name,
                "image_url": self.image_url,
                "expiration_time": self.expiration_time,
                "min_bid": self.min_bid,
                "min_increment_bid": self.min_increment_bid,
                "current_bid": bid,
                "status": self.status}

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<Items({name})>'.format(name=self.name)