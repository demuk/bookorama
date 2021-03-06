"""Books table

Revision ID: ae002dc8ce73
Revises: a8ea318de985
Create Date: 2022-01-26 20:21:49.163717

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae002dc8ce73'
down_revision = 'a8ea318de985'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('author', sa.String(length=140), nullable=True),
    sa.Column('genre', sa.String(length=56), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_book_timestamp'), 'book', ['timestamp'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_book_timestamp'), table_name='book')
    op.drop_table('book')
    # ### end Alembic commands ###
