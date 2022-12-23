"""create sprocket table

Revision ID: 08daca05613f
Revises: 
Create Date: 2022-12-23 16:06:02.348491

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08daca05613f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'sprocket',
        sa.Column('id', sa.String, primary_key=True),
        sa.Column('teeth', sa.Integer),
        sa.Column('pitch_diameter', sa.Integer),
        sa.Column('outside_diameter', sa.Integer),
        sa.Column('pitch', sa.Integer),
    )


def downgrade() -> None:
    op.drop_table('sprocket')
