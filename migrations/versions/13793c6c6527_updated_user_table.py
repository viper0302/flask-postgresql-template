"""updated User table

Revision ID: 13793c6c6527
Revises: 4c0e1dacad90
Create Date: 2016-01-15 17:33:51.288663

"""

# revision identifiers, used by Alembic.
revision = '13793c6c6527'
down_revision = '4c0e1dacad90'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'temp')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('temp', sa.VARCHAR(), autoincrement=False, nullable=True))
    ### end Alembic commands ###