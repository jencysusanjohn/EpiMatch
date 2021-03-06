"""add password_reset_otp_secret field

Revision ID: 7c16ee96b7df
Revises: 7a0292a80606
Create Date: 2020-07-11 17:29:39.667837

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c16ee96b7df'
down_revision = '7a0292a80606'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_table', sa.Column(
        'password_reset_otp_secret', sa.String(length=16), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_table', 'password_reset_otp_secret')
    # ### end Alembic commands ###
