"""empty message

Revision ID: 6ccb2d66fe64
Revises: b6f5de8a6bb0
Create Date: 2020-04-14 11:08:23.907383

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ccb2d66fe64'
down_revision = 'b6f5de8a6bb0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('webcam_settings', sa.Column('mobile_follower_mode', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('webcam_settings', 'mobile_follower_mode')
    # ### end Alembic commands ###
