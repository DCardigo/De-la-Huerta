"""empty message

Revision ID: 79479c3c5745
Revises: 
Create Date: 2023-09-04 09:14:19.740855

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79479c3c5745'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('productoNombres',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('perfil_productores',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('nombre_huerta', sa.String(length=250), nullable=True),
    sa.Column('nombre', sa.String(length=20), nullable=False),
    sa.Column('apellido', sa.String(length=50), nullable=False),
    sa.Column('direccion', sa.String(length=120), nullable=False),
    sa.Column('telefono', sa.Integer(), nullable=False),
    sa.Column('codigo_postal', sa.Integer(), nullable=False),
    sa.Column('comunidad_autonoma', sa.String(length=80), nullable=True),
    sa.Column('provincia', sa.String(length=80), nullable=True),
    sa.Column('foto_portada', sa.String(length=250), nullable=True),
    sa.Column('foto_perfil', sa.String(length=250), nullable=True),
    sa.Column('problemas', sa.String(length=250), nullable=True),
    sa.Column('descripcion', sa.String(length=400), nullable=True),
    sa.Column('donde_encontrar', sa.String(length=250), nullable=True),
    sa.Column('latitud', sa.Float(), nullable=True),
    sa.Column('longitud', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('telefono')
    )
    op.create_table('productos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('productor_id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=True),
    sa.Column('variedad', sa.String(length=250), nullable=True),
    sa.Column('cantidad', sa.Integer(), nullable=True),
    sa.Column('unidad_medida', sa.String(length=250), nullable=True),
    sa.Column('precio', sa.Float(), nullable=True),
    sa.Column('tipo_produccion', sa.String(length=250), nullable=True),
    sa.Column('recogida', sa.String(length=250), nullable=True),
    sa.ForeignKeyConstraint(['productor_id'], ['perfil_productores.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_productor',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('productor_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['productor_id'], ['perfil_productores.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )
    op.create_table('pedidos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('producto_id', sa.Integer(), nullable=False),
    sa.Column('cantidad_solicitada', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['producto_id'], ['productos.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pedidos')
    op.drop_table('user_productor')
    op.drop_table('productos')
    op.drop_table('perfil_productores')
    op.drop_table('users')
    op.drop_table('productoNombres')
    # ### end Alembic commands ###