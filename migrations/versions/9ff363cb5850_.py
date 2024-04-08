"""empty message

Revision ID: 9ff363cb5850
Revises: 
Create Date: 2024-04-04 20:46:34.368170

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ff363cb5850'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('prices')
    op.drop_table('ports')
    op.drop_table('regions')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('regions',
    sa.Column('slug', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('name', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('parent_slug', sa.TEXT(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['parent_slug'], ['regions.slug'], name='regions_parent_slug_fkey'),
    sa.PrimaryKeyConstraint('slug', name='regions_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('ports',
    sa.Column('code', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('name', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('parent_slug', sa.TEXT(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['parent_slug'], ['regions.slug'], name='ports_parent_slug_fkey'),
    sa.PrimaryKeyConstraint('code', name='ports_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('prices',
    sa.Column('orig_code', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('dest_code', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('day', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['dest_code'], ['ports.code'], name='prices_dest_code_fkey'),
    sa.ForeignKeyConstraint(['orig_code'], ['ports.code'], name='prices_orig_code_fkey')
    )
    # ### end Alembic commands ###