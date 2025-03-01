"""Empty Init

Revision ID: 816aeecbb4b8
Revises: 53724cd15170
Create Date: 2025-03-01 18:19:33.369281

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '816aeecbb4b8'
down_revision: Union[str, None] = '53724cd15170'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
