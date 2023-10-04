"""add credit_cards table

Revision ID: ec7174f45f0c
Revises: 557167338140
Create Date: 2023-10-03 12:02:42.204579

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ec7174f45f0c'
down_revision: Union[str, None] = '557167338140'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('credit_cards',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('exp_date', sa.Date(), nullable=False),
                    sa.Column('holder', sa.String(), nullable=False),
                    sa.Column('number', sa.String(), nullable=False),
                    sa.Column('cvv', sa.Integer(), nullable=True),
                    sa.Column('brand', sa.String(), nullable=False),
                    sa.Column('encryption_key', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade() -> None:
    op.drop_table('credit_cards')
