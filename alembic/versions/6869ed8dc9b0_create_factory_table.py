"""create factory table

Revision ID: 6869ed8dc9b0
Revises: 08daca05613f
Create Date: 2022-12-23 16:08:39.802747

"""
from alembic import op
import sqlalchemy as sa

from orm import uuid_gen

# revision identifiers, used by Alembic.
revision = '6869ed8dc9b0'
down_revision = '08daca05613f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    factory_table = op.create_table(
        'factory',
        sa.Column('id', sa.String, primary_key=True),
        sa.Column('chart_data', sa.JSON)
    )

    op.bulk_insert(factory_table,
                   [
                       {
                           "id": uuid_gen(),
                           "chart_data": {
                               "sprocket_production_actual": [
                                   32,
                                   29,
                                   31,
                                   30,
                                   32,
                                   32,
                                   29,
                                   31,
                                   30,
                                   32,
                                   32,
                                   29,
                                   31,
                                   30,
                                   32,
                                   32,
                                   29,
                                   31,
                                   30,
                                   32
                               ],
                               "sprocket_production_goal": [
                                   32,
                                   30,
                                   31,
                                   29,
                                   32,
                                   32,
                                   30,
                                   31,
                                   29,
                                   32,
                                   32,
                                   30,
                                   31,
                                   29,
                                   32,
                                   32,
                                   30,
                                   31,
                                   29,
                                   32
                               ],
                               "time": [
                                   1611194818,
                                   1611194878,
                                   1611194938,
                                   1611194998,
                                   1611195058,
                                   1611195118,
                                   1611195178,
                                   1611195238,
                                   1611195298,
                                   1611195358,
                                   1611195418,
                                   1611195478,
                                   1611195538,
                                   1611195598,
                                   1611195658,
                                   1611195718,
                                   1611195778,
                                   1611195838,
                                   1611195898,
                                   1611195958
                               ]
                           }
                       },
                       {
                           "id": uuid_gen(),
                           "chart_data": {
                               "sprocket_production_actual": [
                                   32,
                                   28,
                                   31,
                                   30,
                                   30,
                                   32,
                                   29,
                                   28,
                                   30,
                                   32,
                                   32,
                                   29,
                                   31,
                                   30,
                                   31,
                                   32,
                                   29,
                                   29,
                                   33,
                                   30
                               ],
                               "sprocket_production_goal": [
                                   31,
                                   33,
                                   29,
                                   29,
                                   32,
                                   30,
                                   30,
                                   31,
                                   29,
                                   31,
                                   31,
                                   30,
                                   28,
                                   29,
                                   32,
                                   29,
                                   30,
                                   31,
                                   28,
                                   32
                               ],
                               "time": [
                                   1611204818,
                                   1611204878,
                                   1611204938,
                                   1611204998,
                                   1611205058,
                                   1611205118,
                                   1611205178,
                                   1611205238,
                                   1611205298,
                                   1611205358,
                                   1611205418,
                                   1611205478,
                                   1611205538,
                                   1611205598,
                                   1611205658,
                                   1611205718,
                                   1611205778,
                                   1611205838,
                                   1611205898,
                                   1611205958
                               ]
                           }
                       },
                       {
                           "id": uuid_gen(),
                           "chart_data": {
                               "sprocket_production_actual": [
                                   32,
                                   29,
                                   31,
                                   30,
                                   30,
                                   32,
                                   29,
                                   29,
                                   30,
                                   32,
                                   32,
                                   29,
                                   31,
                                   30,
                                   30,
                                   32,
                                   29,
                                   29,
                                   33,
                                   31
                               ],
                               "sprocket_production_goal": [
                                   31,
                                   31,
                                   29,
                                   30,
                                   32,
                                   30,
                                   30,
                                   31,
                                   29,
                                   31,
                                   30,
                                   30,
                                   28,
                                   29,
                                   32,
                                   29,
                                   31,
                                   31,
                                   28,
                                   32
                               ],
                               "time": [
                                   1611304818,
                                   1611304878,
                                   1611304938,
                                   1611304998,
                                   1611305058,
                                   1611305118,
                                   1611305178,
                                   1611305238,
                                   1611305298,
                                   1611305358,
                                   1611305418,
                                   1611305478,
                                   1611305538,
                                   1611305598,
                                   1611305658,
                                   1611305718,
                                   1611305778,
                                   1611305838,
                                   1611305898,
                                   1611305958
                               ]
                           }
                       }
                   ]
                   )


def downgrade() -> None:
    op.drop_table('factory')
