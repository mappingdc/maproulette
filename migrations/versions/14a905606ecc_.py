"""adding indices on action table, adding metrics table

Revision ID: 14a905606ecc
Revises: 3115f24a7604
Create Date: 2014-07-02 07:30:37.625861

"""

# revision identifiers, used by Alembic.
revision = '14a905606ecc'
down_revision = '3115f24a7604'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('metrics',
                    sa.Column('timestamp', sa.DateTime(), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('challenge_slug', sa.String(), nullable=False),
                    sa.Column('status', sa.String(), nullable=False),
                    sa.Column('count', sa.Integer(), nullable=True),
                    sa.PrimaryKeyConstraint(
                        'timestamp', 'user_id', 'challenge_slug', 'status')
                    )
    op.create_index(
        'idx_metrics_challengeslug',
        'metrics',
        ['challenge_slug'],
        unique=False)
    op.create_index('idx_metrics_status', 'metrics', ['status'], unique=False)
    op.create_index('idx_metrics_userid', 'metrics', ['user_id'], unique=False)
    op.create_index('idx_action_status', 'actions', ['status'], unique=False)
    op.create_index('idx_action_taskid', 'actions', ['task_id'], unique=False)
    op.create_index(
        'idx_action_timestamp',
        'actions',
        ['timestamp'],
        unique=False)
    op.create_index('idx_action_userid', 'actions', ['user_id'], unique=False)
    op.create_index('idx_challenge_slug', 'challenges', ['slug'], unique=False)
    op.create_index(
        'idx_user_displayname',
        'users',
        ['display_name'],
        unique=False)


def downgrade():
    op.drop_index('idx_user_displayname', table_name='users')
    op.drop_index('idx_challenge_slug', table_name='challenges')
    op.drop_index('idx_action_userid', table_name='actions')
    op.drop_index('idx_action_timestamp', table_name='actions')
    op.drop_index('idx_action_taskid', table_name='actions')
    op.drop_index('idx_action_status', table_name='actions')
    op.drop_index('idx_metrics_userid', table_name='metrics')
    op.drop_index('idx_metrics_status', table_name='metrics')
    op.drop_index('idx_metrics_challengeslug', table_name='metrics')
    op.drop_table('metrics')
