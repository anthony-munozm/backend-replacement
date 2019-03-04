"""Add sorting price to Orders

Revision ID: 5e9be84a782f
Revises: e032ff832b82
Create Date: 2019-03-04 07:40:25.232335

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, Numeric

# revision identifiers, used by Alembic.
revision = '5e9be84a782f'
down_revision = 'e032ff832b82'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("orders", Column("sorting_price", Numeric))
    op.create_index("index_orders_on_sorting_price", "orders",
                    ["sorting_price"])


def downgrade():
    op.drop_column("orders", "sorting_price")
