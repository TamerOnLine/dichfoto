# alembic revision -m "add photographer_url to albums"
# ثم في ملف المايغريشن:
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.add_column('albums', sa.Column('photographer_url', sa.String(length=255), nullable=True))

def downgrade():
    op.drop_column('albums', 'photographer_url')
