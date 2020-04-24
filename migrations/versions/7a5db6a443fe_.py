"""empty message

Revision ID: 7a5db6a443fe
Revises: 654eac861775
Create Date: 2020-04-24 12:26:27.762851

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a5db6a443fe'
down_revision = '654eac861775'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('games_cricket', sa.Column('confirmation_needed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('games_cricket', 'confirmation_needed')
    # ### end Alembic commands ###
