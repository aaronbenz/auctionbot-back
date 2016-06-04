# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template, request
# from flask_login import login_required
from AuctionBot.items.models import Items
from AuctionBot.bids.models import Bids
from AuctionBot.user.models import User
from AuctionBot.utils import responsify
from time import time
blueprint = Blueprint('routes', __name__, url_prefix='/api')
from AuctionBot.extensions import db
GET = "GET"
PUT = "PUT"
POST = "POST"
DELETE = "DELETE"

success_json = responsify({"success": True})

@blueprint.route('/')
def test():
    return "Team AuctionBot Succa"

@blueprint.route('/items/')
def get_items():
    """List members."""
    items = Items.query.filter(Items.expiration_time >= int(time())).limit(10).all()
    return responsify({"items": items})

@blueprint.route('/items/', methods=[POST])
def new_items():
    item = Items.create(**request.json)
    return responsify({"id": item.id})
    # js = Items(**request.json)
    # return jsonify({"item": "test"})

@blueprint.route('/users/', methods=[POST])
def new_user():
    User.create(**request.json)
    return success_json



