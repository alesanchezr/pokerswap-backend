"""empty message

Revision ID: 58200e166e4e
Revises: 70756e3f5d98
Create Date: 2019-10-04 23:26:44.796111

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '58200e166e4e'
down_revision = '70756e3f5d98'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('valid', sa.Boolean(), nullable=True))
    op.drop_column('users', 'validated')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('validated', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.drop_column('users', 'valid')
    # ### end Alembic commands ###
