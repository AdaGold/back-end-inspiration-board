"""adding models

Revision ID: 0998518428e5
Revises: 
Create Date: 2021-07-12 15:09:07.865089

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0998518428e5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('board',
    sa.Column('board_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('owner', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('board_id')
    )
    op.create_table('card',
    sa.Column('card_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('message', sa.String(), nullable=True),
    sa.Column('likes_count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('card_id')
    )
    op.drop_table('hotel_guests')
    op.drop_table('flowers')
    op.drop_table('reviews')
    op.drop_table('tags')
    op.drop_table('posts')
    op.drop_table('posts_tags')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts_tags',
    sa.Column('post_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('tag_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], name='posts_tags_post_id_fkey'),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], name='posts_tags_tag_id_fkey'),
    sa.PrimaryKeyConstraint('post_id', 'tag_id', name='posts_tags_pkey')
    )
    op.create_table('posts',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('title', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('body', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='posts_pkey')
    )
    op.create_table('tags',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('tagname', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='tags_pkey')
    )
    op.create_table('reviews',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('title', sa.VARCHAR(length=32), autoincrement=False, nullable=True),
    sa.Column('product_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('body', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('creator_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('stars', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='reviews_pkey')
    )
    op.create_table('flowers',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=32), autoincrement=False, nullable=True),
    sa.Column('soil_type', sa.VARCHAR(length=32), autoincrement=False, nullable=True),
    sa.Column('light_level', sa.VARCHAR(length=32), autoincrement=False, nullable=True),
    sa.Column('season', sa.VARCHAR(length=32), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='flowers_pkey')
    )
    op.create_table('hotel_guests',
    sa.Column('guest_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('guest_name', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('is_checked_in', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('guest_id', name='hotel_guests_pkey')
    )
    op.drop_table('card')
    op.drop_table('board')
    # ### end Alembic commands ###
