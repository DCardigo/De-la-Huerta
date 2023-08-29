"""empty message

Revision ID: 72a8a9e0e476
Revises: 6d86c87c2d7b
Create Date: 2023-08-29 09:45:14.975601

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72a8a9e0e476'
down_revision = '6d86c87c2d7b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pedidos', schema=None) as batch_op:
        batch_op.drop_column('fecha_recogida')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pedidos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('fecha_recogida', sa.DATE(), autoincrement=False, nullable=True))

    # ### end Alembic commands ###
