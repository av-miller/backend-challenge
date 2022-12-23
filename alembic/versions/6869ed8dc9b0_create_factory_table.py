"""create factory table

Revision ID: 6869ed8dc9b0
Revises: 08daca05613f
Create Date: 2022-12-23 16:08:39.802747

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6869ed8dc9b0'
down_revision = '08daca05613f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'factory',
        sa.Column('id', sa.String, primary_key=True),
        sa.Column('chart_data', sa.JSON)
    )


def downgrade() -> None:
    op.drop_table('factory')

