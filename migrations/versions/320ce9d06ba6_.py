"""empty message

Revision ID: 320ce9d06ba6
Revises: 544bc9ea420e
Create Date: 2019-09-19 17:31:24.974012

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '320ce9d06ba6'
down_revision = '544bc9ea420e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('profiles', sa.Column('first_name', sa.String(length=100), nullable=False))
    op.add_column('profiles', sa.Column('hendon_url', sa.String(length=200), nullable=True))
    op.add_column('profiles', sa.Column('last_name', sa.String(length=100), nullable=False))
    op.add_column('profiles', sa.Column('profile_picture_url', sa.String(length=200), nullable=True))
    op.add_column('profiles', sa.Column('user_id', sa.Integer(), nullable=True))
    op.add_column('profiles', sa.Column('username', sa.String(length=100), nullable=True))
    op.create_foreign_key(None, 'profiles', 'users', ['user_id'], ['id'])
    op.add_column('users', sa.Column('email', sa.String(length=100), nullable=False))
    op.add_column('users', sa.Column('password', sa.String(length=100), nullable=False))
    op.create_unique_constraint(None, 'users', ['password'])
    op.create_unique_constraint(None, 'users', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'password')
    op.drop_column('users', 'email')
    op.drop_constraint(None, 'profiles', type_='foreignkey')
    op.drop_column('profiles', 'username')
    op.drop_column('profiles', 'user_id')
    op.drop_column('profiles', 'profile_picture_url')
    op.drop_column('profiles', 'last_name')
    op.drop_column('profiles', 'hendon_url')
    op.drop_column('profiles', 'first_name')
    # ### end Alembic commands ###
