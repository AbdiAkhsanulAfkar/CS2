"""Initial migration

Revision ID: dd8192516c8f
Revises: 
Create Date: 2020-04-22 18:14:24.082440

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'dd8192516c8f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.drop_index('NIM', table_name='mahasiswa')
    op.drop_table('mahasiswa')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mahasiswa',
    sa.Column('ID', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('NIM', mysql.CHAR(length=10), nullable=False),
    sa.Column('Nama', mysql.CHAR(length=100), nullable=False),
    sa.Column('Alamat', mysql.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('ID'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('NIM', 'mahasiswa', ['NIM'], unique=True)
    op.drop_table('user')
    # ### end Alembic commands ###