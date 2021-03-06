"""empty message

Revision ID: faec0204d7c9
Revises: 533b73ad96c3
Create Date: 2022-07-12 10:13:19.325447

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'faec0204d7c9'
down_revision = '533b73ad96c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('work_reports', sa.Column('clientEmailAddress', sa.String(length=30), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('work_reports', 'clientEmailAddress')
    # ### end Alembic commands ###
