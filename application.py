import os
from glob import glob
from subprocess import call

from flask_migrate import Migrate, MigrateCommand
from flask_script import Command, Manager, Option, Server, Shell
from flask_script.commands import Clean, ShowUrls

from AuctionBot.app import create_app
from AuctionBot.database import db
from AuctionBot.settings import DevConfig, ProdConfig
from AuctionBot.user.models import User

CONFIG = ProdConfig if os.environ.get('AUCTIONBOT_ENV') == 'prod' else DevConfig
HERE = os.path.abspath(os.path.dirname(__file__))
# TEST_PATH = os.path.join(HERE, 'tests')

app = create_app(CONFIG)
# manager = Manager(app)
# migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run()
