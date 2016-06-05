from AuctionBot.items.models import Items
from AuctionBot.bids.models import Bids
from AuctionBot import communications
from AuctionBot import utils
import flask
import requests
class Notifications(object):
    def __init__(self, users, msg=communications.BASE_NOTIFICATION, items=None):
        self.users = users
        self.msg = msg
        self.items = items

    def to_dict(self):
        if not isinstance(self.users, list):
            self.users = [self.users]
        if not isinstance(self.items, list):
            self.items = [self.items]


        return {"users": self.users,
                "msg": self.msg,
                "items": self.items}

    def send_post(self):
        #probably should check response of this
        response = requests.post(flask.current_app.config.get("BOT_WEB_URI"), data=utils.jsonify(self), headers={'content-type': "application/json"})
        print "Response from Web Bot: {0} : {1}".format(response.status_code, response.text)

    @staticmethod
    def notify_all_bidders_of_item(item_id, msg=communications.BASE_NOTIFICATION_TO_ALL_BIDDERS_OF_ITEM):
        all_unique_bids = Bids.query.filter(Bids.item_id==item_id).distinct(Bids.user_id).all()

        item = None if len(all_unique_bids) == 0 else all_unique_bids[0].item

        return Notifications(users=[i.user for i in all_unique_bids],
                             items=item,
                             msg=msg)

    @staticmethod
    def notifiy_recent_loser(item_id, not_user_id, msg=communications.USER_JUST_GOT_OUTBID):
        last_bid = Bids.query.filter(Bids.item_id==item_id).filter(Bids.user_id!=not_user_id).order_by(Bids.timestamp.desc()).first()
        if last_bid is None:
            return None

        return Notifications(users=last_bid.user,
                             items=last_bid.item,
                             msg=msg)