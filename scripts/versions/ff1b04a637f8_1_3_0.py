"""1.3.0

Revision ID: ff1b04a637f8
Revises: 7c14267ffbe4
Create Date: 2023-09-17 09:35:42.773359

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff1b04a637f8'
down_revision = '7c14267ffbe4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('CONFIG_SYNC_PATHS', sa.Column('LOCATING', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('CONFIG_SYNC_PATHS', 'LOCATING')
    # ### end Alembic commands ###
