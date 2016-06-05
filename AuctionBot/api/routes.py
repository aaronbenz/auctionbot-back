# -*- coding: utf-8 -*-
"""User views."""
import pymysql
from flask import Blueprint, render_template, request, abort
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

def error_json(error_code, msg="An Error Occurred"):
    return responsify({"code": error_code,
                       "msg": msg})
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

@blueprint.route('/users/', methods=[POST])
def new_user():
    try:
        User.create(**request.json)
        return success_json
    except pymysql.IntegrityError:
        return error_json(405, "User already exists")
    except Exception, e:
        return error_json(101)

@blueprint.route('/bids/', methods=[POST])
def new_bid():
    fb_id = request.json.get("fb_id")
    item_id = request.json.get("item_id")
    price = request.json.get("price")

    #get current bid
    recent_bid = Bids.current_item_bid(item_id)
    assert isinstance(recent_bid, Bids) or recent_bid is None

    if recent_bid is not None:
        if recent_bid.user.fb_id == fb_id:
            return error_json(405, "User is already top bidder")
        if recent_bid.price > price:
            return error_json(405, "Bid is less than the current bid...aka... bring out the check book")
        if recent_bid.price + recent_bid.item.min_increment_bid > price:
            return error_json(405, "Bid is not high enough... more money please :)")

    usr = User.query.filter(User.fb_id==fb_id).first()

    if usr is None:
        abort(401)

    Bids.create(user_id=usr.id, item_id=item_id, price=price)

    return success_json



