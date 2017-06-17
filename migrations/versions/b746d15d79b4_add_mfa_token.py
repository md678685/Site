"""Add MFA token

Revision ID: b746d15d79b4
Revises: e6937aa2f743
Create Date: 2017-05-07 15:45:58.743751

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b746d15d79b4'
down_revision = 'e6937aa2f743'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('mfa_token', sa.String(length=16), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'mfa_token')
    # ### end Alembic commands ###
