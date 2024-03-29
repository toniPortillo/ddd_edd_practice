"""forex_pairs

Revision ID: da376e0b5a50
Revises: b1b2461786f6
Create Date: 2023-05-20 00:00:18.489544

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'da376e0b5a50'
down_revision = 'b1b2461786f6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stock_stock')
    op.drop_table('forex_pairs')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('forex_pairs',
    sa.Column('id', postgresql.UUID(), autoincrement=False, nullable=False),
    sa.Column('symbol', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('currency_group', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('currency_base', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='forex_pairs_pkey')
    )
    op.create_table('stock_stock',
    sa.Column('id', postgresql.UUID(), autoincrement=False, nullable=False),
    sa.Column('symbol', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('currency', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('exchange', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('mic_code', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('country', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('type', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='stock_stock_pkey')
    )
    # ### end Alembic commands ###
