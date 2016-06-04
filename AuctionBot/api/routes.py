# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template, jsonify, request
# from flask_login import login_required
from AuctionBot.items.models import Items
from AuctionBot.bids.models import Bids
blueprint = Blueprint('routes', __name__, url_prefix='/api')

GET = "GET"
PUT = "PUT"
POST = "POST"
DELETE = "DELETE"

@blueprint.route('/')
def test():
    return "Team AuctionBot Succa"

@blueprint.route('/items/')
def get_items():
    """List members."""
    return jsonify({"item": "test"})

@blueprint.route('/items/', methods=[POST])
def new_items():
    item = Items.create(**request.json)
    return jsonify({"id": item.id})
    # js = Items(**request.json)
    # return jsonify({"item": "test"})





