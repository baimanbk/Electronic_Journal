"""Add subject column to scores table

Revision ID: ca48720931c7
Revises: 
Create Date: 2024-05-30 19:51:28.789002

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ca48720931c7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_scores_id', table_name='scores')
    op.drop_table('scores')
    op.drop_index('ix_students_id', table_name='students')
    op.drop_index('ix_students_name', table_name='students')
    op.drop_table('students')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('age', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_students_name', 'students', ['name'], unique=False)
    op.create_index('ix_students_id', 'students', ['id'], unique=False)
    op.create_table('scores',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('value', sa.INTEGER(), nullable=True),
    sa.Column('student_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_scores_id', 'scores', ['id'], unique=False)
    # ### end Alembic commands ###
