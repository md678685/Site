"""Celery tasks

Revision ID: 6f2212bbc07b
Revises: 2118624d84d9
Create Date: 2017-06-26 10:42:58.253693

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f2212bbc07b'
down_revision = '2118624d84d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('celery_task',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('task_id', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('args', sa.JSON(), nullable=True),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('task_id')
    )
    op.create_unique_constraint('_product_branch_uc', 'product_branch', ['product_id', 'name'])
    op.create_foreign_key(None, 'product_branch', 'product', ['product_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'product_branch', type_='foreignkey')
    op.drop_constraint('_product_branch_uc', 'product_branch', type_='unique')
    op.drop_table('celery_task')
    # ### end Alembic commands ###
