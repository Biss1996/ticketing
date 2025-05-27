"""Add users table

Revision ID: e2081dfb7665
Revises: 003563487fd3
Create Date: 2025-05-27 18:45:24.742360

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e2081dfb7665'
down_revision: Union[str, None] = '003563487fd3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
