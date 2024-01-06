"""empty message

Revision ID: 5bdaf184e058
Revises: 
Create Date: 2024-01-06 22:37:07.353999

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5bdaf184e058'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('medicine_unit', schema=None) as batch_op:
        batch_op.drop_index('unit_name')

    op.drop_table('medicine_unit')
    op.drop_table('cashiers')
    with op.batch_alter_table('bills', schema=None) as batch_op:
        batch_op.drop_index('medical_bill_id')

    op.drop_table('bills')
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index('account_id')
        batch_op.drop_index('email')
        batch_op.drop_index('phone_number')

    op.drop_table('users')
    with op.batch_alter_table('medicine_type', schema=None) as batch_op:
        batch_op.drop_index('type_of_medicine')

    op.drop_table('medicine_type')
    op.drop_table('medicalbill_packages')
    op.drop_table('employees')
    op.drop_table('prescriptions')
    with op.batch_alter_table('medicines', schema=None) as batch_op:
        batch_op.drop_index('medicine_name')

    op.drop_table('medicines')
    op.drop_table('medicine_types')
    with op.batch_alter_table('regulations', schema=None) as batch_op:
        batch_op.drop_index('regulation_name')

    op.drop_table('regulations')
    with op.batch_alter_table('accounts', schema=None) as batch_op:
        batch_op.drop_index('username')

    op.drop_table('accounts')
    op.drop_table('examination_list')
    with op.batch_alter_table('packages', schema=None) as batch_op:
        batch_op.drop_index('packages_name')

    op.drop_table('packages')
    op.drop_table('examination_schedule')
    op.drop_table('doctors')
    op.drop_table('administrators')
    with op.batch_alter_table('patients', schema=None) as batch_op:
        batch_op.drop_index('insurance_id')

    op.drop_table('patients')
    op.drop_table('medical_bills')
    op.drop_table('nurses')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('nurses',
    sa.Column('id', mysql.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('educational_attainment', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=100), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['employees.id'], name='nurses_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('medical_bills',
    sa.Column('diagnostic', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=100), nullable=True),
    sa.Column('symptoms', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=100), nullable=True),
    sa.Column('examination_date', mysql.DATETIME(), nullable=False),
    sa.Column('patient_id', mysql.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('doctor_id', mysql.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('id', mysql.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('created_date', mysql.DATETIME(), nullable=False),
    sa.Column('updated_date', mysql.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['doctor_id'], ['doctors.id'], name='medical_bills_ibfk_2'),
    sa.ForeignKeyConstraint(['patient_id'], ['patients.id'], name='medical_bills_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('patients',
    sa.Column('id', mysql.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('insurance_id', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=20), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['users.id'], name='patients_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('patients', schema=None) as batch_op:
        batch_op.create_index('insurance_id', ['insurance_id'], unique=True)

    op.create_table('administrators',
    sa.Column('id', mysql.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('inauguration_day', mysql.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['employees.id'], name='administrators_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('doctors',
    sa.Column('id', mysql.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('specialist', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=100), nullable=False),
    sa.Column('years_of_experience', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['id'], ['employees.id'], name='doctors_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('examination_schedule',
    sa.Column('dob', mysql.DATETIME(), nullable=False),
    sa.Column('email', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=50), nullable=False),
    sa.Column('gender', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=10), nullable=False),
    sa.Column('address', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=100), nullable=False),
    sa.Column('last_name', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=50), nullable=False),
    sa.Column('first_name', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=50), nullable=False),
    sa.Column('phone_number', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=11), nullable=False),
    sa.Column('examination_date', mysql.DATETIME(), nullable=False),
    sa.Column('doctor_id', mysql.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('examination_list_id', mysql.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('patient_id', mysql.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('id', mysql.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('created_date', mysql.DATETIME(), nullable=False),
    sa.Column('updated_date', mysql.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['doctor_id'], ['doctors.id'], name='examination_schedule_ibfk_1'),
    sa.ForeignKeyConstraint(['examination_list_id'], ['examination_list.id'], name='examination_schedule_ibfk_2'),
    sa.ForeignKeyConstraint(['patient_id'], ['patients.id'], name='examination_schedule_ibfk_3', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('packages',
    sa.Column('packages_name', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=20), nullable=False),
    sa.Column('price', mysql.DOUBLE(asdecimal=True), nullable=False),
    sa.Column('id', mysql.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('created_date', mysql.DATETIME(), nullable=False),
    sa.Column('updated_date', mysql.DATETIME(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('packages', schema=None) as batch_op:
        batch_op.create_index('packages_name', ['packages_name'], unique=True)

    op.create_table('examination_list',
    sa.Column('examination_date', mysql.DATETIME(), nullable=False),
    sa.Column('nurse_id', mysql.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('id', mysql.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('created_date', mysql.DATETIME(), nullable=False),
    sa.Column('updated_date', mysql.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['nurse_id'], ['nurses.id'], name='examination_list_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('accounts',
    sa.Column('username', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=50), nullable=False),
    sa.Column('password', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=50), nullable=False),
    sa.Column('slug', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=50), nullable=False),
    sa.Column('active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.Column('is_confirmed', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.Column('confirmed_on', mysql.DATETIME(), nullable=True),
    sa.Column('avatar', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=255), nullable=True),
    sa.Column('role', mysql.ENUM('PATIENT', 'DOCTOR', 'NURSE', 'STAFF', 'ADMIN'), nullable=False),
    sa.Column('id', mysql.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('created_date', mysql.DATETIME(), nullable=False),
    sa.Column('updated_date', mysql.DATETIME(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('accounts', schema=None) as batch_op:
        batch_op.create_index('username', ['username'], unique=True)

    op.create_table('regulations',
    sa.Column('regulation_name', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=50), nullable=False),
    sa.Column('description', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=100), nullable=True),
    sa.Column('note', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=100), nullable=True),
    sa.Column('status', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.Column('admin_id', mysql.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('id', mysql.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('created_date', mysql.DATETIME(), nullable=False),
    sa.Column('updated_date', mysql.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['admin_id'], ['administrators.id'], name='regulations_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('regulations', schema=None) as batch_op:
        batch_op.create_index('regulation_name', ['regulation_name'], unique=True)

    op.create_table('medicine_types',
    sa.Column('medicine_id', mysql.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('medicine_type_id', mysql.BIGINT(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['medicine_id'], ['medicines.id'], name='medicine_types_ibfk_1'),
    sa.ForeignKeyConstraint(['medicine_type_id'], ['medicine_type.id'], name='medicine_types_ibfk_2'),
    sa.PrimaryKeyConstraint('medicine_id', 'medicine_type_id'),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('medicines',
    sa.Column('medicine_name', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=20), nullable=False),
    sa.Column('description', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=100), nullable=True),
    sa.Column('note', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=100), nullable=True),
    sa.Column('price', mysql.DOUBLE(asdecimal=True), nullable=False),
    sa.Column('amount', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('image', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=255), nullable=True),
    sa.Column('direction_for_use', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=100), nullable=True),
    sa.Column('medicine_unit_id', mysql.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('id', mysql.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('created_date', mysql.DATETIME(), nullable=False),
    sa.Column('updated_date', mysql.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['medicine_unit_id'], ['medicine_unit.id'], name='medicines_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('medicines', schema=None) as batch_op:
        batch_op.create_index('medicine_name', ['medicine_name'], unique=True)

    op.create_table('prescriptions',
    sa.Column('amount', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('note', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=100), nullable=True),
    sa.Column('medicine_id', mysql.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('medical_bill_id', mysql.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('id', mysql.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('created_date', mysql.DATETIME(), nullable=False),
    sa.Column('updated_date', mysql.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['medical_bill_id'], ['medical_bills.id'], name='prescriptions_ibfk_2'),
    sa.ForeignKeyConstraint(['medicine_id'], ['medicines.id'], name='prescriptions_ibfk_1'),
    sa.PrimaryKeyConstraint('id', 'medicine_id', 'medical_bill_id'),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('employees',
    sa.Column('id', mysql.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('salary', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('salary_coefficient', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['users.id'], name='employees_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('medicalbill_packages',
    sa.Column('medical_bill_id', mysql.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('packages_id', mysql.BIGINT(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['medical_bill_id'], ['medical_bills.id'], name='medicalbill_packages_ibfk_1'),
    sa.ForeignKeyConstraint(['packages_id'], ['packages.id'], name='medicalbill_packages_ibfk_2'),
    sa.PrimaryKeyConstraint('medical_bill_id', 'packages_id'),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('medicine_type',
    sa.Column('type_of_medicine', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=20), nullable=False),
    sa.Column('id', mysql.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('created_date', mysql.DATETIME(), nullable=False),
    sa.Column('updated_date', mysql.DATETIME(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('medicine_type', schema=None) as batch_op:
        batch_op.create_index('type_of_medicine', ['type_of_medicine'], unique=True)

    op.create_table('users',
    sa.Column('first_name', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=50), nullable=False),
    sa.Column('last_name', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=50), nullable=False),
    sa.Column('gender', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=10), nullable=True),
    sa.Column('dob', mysql.DATETIME(), nullable=True),
    sa.Column('address', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=100), nullable=True),
    sa.Column('phone_number', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=11), nullable=True),
    sa.Column('email', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=50), nullable=False),
    sa.Column('account_id', mysql.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('id', mysql.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('created_date', mysql.DATETIME(), nullable=False),
    sa.Column('updated_date', mysql.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['accounts.id'], name='users_ibfk_1', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_index('phone_number', ['phone_number'], unique=True)
        batch_op.create_index('email', ['email'], unique=True)
        batch_op.create_index('account_id', ['account_id'], unique=True)

    op.create_table('bills',
    sa.Column('medicine_money', mysql.DOUBLE(asdecimal=True), nullable=False),
    sa.Column('pre_examination', mysql.DOUBLE(asdecimal=True), nullable=False),
    sa.Column('total_price', mysql.DOUBLE(asdecimal=True), nullable=False),
    sa.Column('examination_date', mysql.DATETIME(), nullable=False),
    sa.Column('cashier_id', mysql.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('patient_id', mysql.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('medical_bill_id', mysql.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('id', mysql.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('created_date', mysql.DATETIME(), nullable=False),
    sa.Column('updated_date', mysql.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['cashier_id'], ['cashiers.id'], name='bills_ibfk_1'),
    sa.ForeignKeyConstraint(['medical_bill_id'], ['medical_bills.id'], name='bills_ibfk_3'),
    sa.ForeignKeyConstraint(['patient_id'], ['patients.id'], name='bills_ibfk_2'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('bills', schema=None) as batch_op:
        batch_op.create_index('medical_bill_id', ['medical_bill_id'], unique=True)

    op.create_table('cashiers',
    sa.Column('id', mysql.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('skills', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=100), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['employees.id'], name='cashiers_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('medicine_unit',
    sa.Column('unit_name', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=20), nullable=False),
    sa.Column('id', mysql.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('created_date', mysql.DATETIME(), nullable=False),
    sa.Column('updated_date', mysql.DATETIME(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('medicine_unit', schema=None) as batch_op:
        batch_op.create_index('unit_name', ['unit_name'], unique=True)

    # ### end Alembic commands ###
