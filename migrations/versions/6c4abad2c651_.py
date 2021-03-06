"""empty message

Revision ID: 6c4abad2c651
Revises: faec0204d7c9
Create Date: 2022-07-12 13:09:48.637200

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c4abad2c651'
down_revision = 'faec0204d7c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hypervisor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('createTime', sa.DateTime(), nullable=True),
    sa.Column('customer', sa.String(length=20), nullable=True),
    sa.Column('ip_address', sa.String(length=20), nullable=True),
    sa.Column('type', sa.String(length=30), nullable=True),
    sa.Column('status', sa.String(length=25), nullable=True),
    sa.Column('ilo_address', sa.String(length=20), nullable=True),
    sa.Column('brand', sa.String(length=15), nullable=True),
    sa.Column('model', sa.String(length=15), nullable=True),
    sa.Column('warranty', sa.String(length=15), nullable=True),
    sa.Column('physical_ram_in_GB', sa.String(length=15), nullable=True),
    sa.Column('numberOfProcessors', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hypervisor')
    # ### end Alembic commands ###
