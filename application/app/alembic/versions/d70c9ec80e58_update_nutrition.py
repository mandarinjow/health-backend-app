"""update_nutrition

Revision ID: d70c9ec80e58
Revises: 5c1c1fa1517c
Create Date: 2021-03-23 13:04:23.374099

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd70c9ec80e58'
down_revision = '5c1c1fa1517c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('FoodNutritionAssociation',
    sa.Column('food_nutrition_id', sa.Integer(), nullable=False),
    sa.Column('food_id', sa.String(), nullable=False),
    sa.Column('nutrition_value', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['food_id'], ['Food.food_id'], ),
    sa.ForeignKeyConstraint(['food_nutrition_id'], ['FoodNutrition.food_nutrition_id'], ),
    sa.PrimaryKeyConstraint('food_nutrition_id', 'food_id')
    )
    op.add_column('FoodNutrition', sa.Column('nutrition_code', sa.String(length=10), nullable=True))
    op.add_column('FoodNutrition', sa.Column('nutrition_measurement_suffix', sa.String(), nullable=True))
    op.drop_constraint('nutrition_type_food_id_unique', 'FoodNutrition', type_='unique')
    op.drop_constraint('FoodNutrition_food_id_fkey', 'FoodNutrition', type_='foreignkey')
    op.drop_column('FoodNutrition', 'nutrition_type')
    op.drop_column('FoodNutrition', 'food_id')
    op.drop_column('FoodNutrition', 'nutrition_value')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('FoodNutrition', sa.Column('nutrition_value', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('FoodNutrition', sa.Column('food_id', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('FoodNutrition', sa.Column('nutrition_type', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.create_foreign_key('FoodNutrition_food_id_fkey', 'FoodNutrition', 'Food', ['food_id'], ['food_id'])
    op.create_unique_constraint('nutrition_type_food_id_unique', 'FoodNutrition', ['nutrition_type', 'food_id'])
    op.drop_column('FoodNutrition', 'nutrition_measurement_suffix')
    op.drop_column('FoodNutrition', 'nutrition_code')
    op.drop_table('FoodNutritionAssociation')
    # ### end Alembic commands ###
