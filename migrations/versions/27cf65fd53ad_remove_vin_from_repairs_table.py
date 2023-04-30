"""remove VIN from repairs table

Revision ID: 27cf65fd53ad
Revises: d89441071f23
Create Date: 2023-04-11 09:01:07.355356

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27cf65fd53ad'
down_revision = 'd89441071f23'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('repairs', schema=None) as batch_op:
        batch_op.drop_column('VIN')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('repairs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('VIN', sa.VARCHAR(length=100), autoincrement=False, nullable=False))

    # ### end Alembic commands ###