"""Initial Migration

Revision ID: d4b786027fd
Revises: None
Create Date: 2014-06-13 21:05:10.408036

"""

# revision identifiers, used by Alembic.
revision = 'd4b786027fd'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('username', sa.String(length=80), nullable=False),
                    sa.Column('email', sa.String(length=80), nullable=False),
                    sa.Column('password', sa.String(length=128), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('first_name', sa.String(length=30), nullable=True),
                    sa.Column('last_name', sa.String(length=30), nullable=True),
                    sa.Column('active', sa.Boolean(), nullable=True),
                    sa.Column('is_admin', sa.Boolean(), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'),
                    sa.UniqueConstraint('username')
                    )
    op.create_table('roles',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=80), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('name')
                    )


def downgrade():
    op.drop_table('roles')
    op.drop_table('users')
