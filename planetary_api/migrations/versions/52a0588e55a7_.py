"""empty message

Revision ID: 52a0588e55a7
Revises: 
Create Date: 2020-03-26 17:38:13.995943

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52a0588e55a7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planets',
    sa.Column('planet_id', sa.Integer(), nullable=False),
    sa.Column('planet_name', sa.String(), nullable=True),
    sa.Column('planet_type', sa.String(), nullable=True),
    sa.Column('home_star', sa.String(), nullable=True),
    sa.Column('mass', sa.Float(), nullable=True),
    sa.Column('radius', sa.Float(), nullable=True),
    sa.Column('distance', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('planet_id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('planets')
    # ### end Alembic commands ###
