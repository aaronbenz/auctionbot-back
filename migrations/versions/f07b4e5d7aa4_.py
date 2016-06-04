"""empty message

Revision ID: f07b4e5d7aa4
Revises: d094feb62433
Create Date: 2016-06-04 16:18:07.097103

"""

# revision identifiers, used by Alembic.
revision = 'f07b4e5d7aa4'
down_revision = 'd094feb62433'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('price', table_name='bids')
    op.drop_index('timestamp', table_name='bids')
    op.drop_index('expiration_time', table_name='items')
    op.drop_index('image_url', table_name='items')
    op.drop_index('min_bid', table_name='items')
    op.drop_index('min_increment_bid', table_name='items')
    op.drop_index('name', table_name='items')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_index('name', 'items', ['name'], unique=True)
    op.create_index('min_increment_bid', 'items', ['min_increment_bid'], unique=True)
    op.create_index('min_bid', 'items', ['min_bid'], unique=True)
    op.create_index('image_url', 'items', ['image_url'], unique=True)
    op.create_index('expiration_time', 'items', ['expiration_time'], unique=True)
    op.create_index('timestamp', 'bids', ['timestamp'], unique=True)
    op.create_index('price', 'bids', ['price'], unique=True)
    ### end Alembic commands ###
