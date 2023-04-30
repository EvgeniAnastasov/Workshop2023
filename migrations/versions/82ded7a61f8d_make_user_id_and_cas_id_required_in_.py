"""make user_id and cas_id required in Repairs model

Revision ID: 82ded7a61f8d
Revises: 27cf65fd53ad
Create Date: 2023-04-11 09:36:59.249941

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82ded7a61f8d'
down_revision = '27cf65fd53ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('repairs', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('car_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('repairs', schema=None) as batch_op:
        batch_op.alter_column('car_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
