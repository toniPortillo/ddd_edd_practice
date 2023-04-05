"""create_stocks_table

Revision ID: b1b2461786f6
Revises: 
Create Date: 2023-04-05 12:45:03.189585

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1b2461786f6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'stock_stock',
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("symbol", sa.String(),),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("currency", sa.String()),
        sa.Column("exchange", sa.String()),
        sa.Column("mic_code", sa.String()),
        sa.Column("type", sa.String()),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("stocks")
