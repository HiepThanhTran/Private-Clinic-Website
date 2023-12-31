from urllib.parse import urlparse

from flask_mail import Message

from private_clinic import dao
from private_clinic.app import app, mail


def is_safe_url(url, allowed_hosts):
    url_info = urlparse(url)
    return url_info.netloc in allowed_hosts


def send_email(to, subject, template):
    return mail.send(Message(subject=subject, recipients=[to], html=template, sender=app.config['MAIL_DEFAULT_SENDER']))


def authenticate(username, password):
    return dao.authenticate(username=username, password=password)


def check_examination_schedule_by_time(time):
    return dao.check_examination_schedule_by_time(time=time)


def check_duplicate_email(email, current_user_id):
    return dao.check_duplicate_email(email=email, current_user_id=current_user_id)


def check_duplicate_phone_number(phone_number, current_user_id):
    return dao.check_duplicate_phone_number(phone_number=phone_number, current_user_id=current_user_id)


def check_duplicate_insurance_id(insurance_id, current_user_id):
    return dao.check_duplicate_insurance_id(insurance_id=insurance_id, current_user_id=current_user_id)


def count_examination_schedule_by_date(date):
    return dao.count_examination_schedule_by_date(date=date)


def create_account(username, password, **kwargs):
    return dao.create_account(username=username, password=password, **kwargs)


def create_user(first_name, last_name, email, account_id):
    return dao.create_user(first_name=first_name, last_name=last_name, email=email, account_id=account_id)


def create_patient(patient_id):
    return dao.create_patient(patient_id=patient_id)


def create_employee(employee_id):
    return dao.create_employee(employee_id=employee_id)


def create_administrator(administrator_id, inauguration_day):
    return dao.create_administrator(administrator_id=administrator_id, inauguration_day=inauguration_day)


def create_cashier(cashier_id):
    return dao.create_cashier(cashier_id=cashier_id)


def create_nurse(nurse_id):
    return dao.create_nurse(nurse_id=nurse_id)


def create_doctor(doctor_id):
    return dao.create_doctor(doctor_id=doctor_id)


def create_examination_schedule(patient_id, examination_date, **kwargs):
    return dao.create_examination_schedule(patient_id=patient_id, examination_date=examination_date, **kwargs)


def create_examination_list(examination_date, nurse_id, examination_schedule_id_list):
    return dao.create_examination_list(examination_date=examination_date, nurse_id=nurse_id,
                                       examination_schedule_id_list=examination_schedule_id_list)


def create_medicine(**kwargs):
    return dao.create_medicine(**kwargs)


def create_medical_bill(symptoms, diagnostic, examination_date, patient_id, doctor_id, packages_id, amount, medicine_id_list):
    return dao.create_medical_bill(
        symptoms=symptoms,
        diagnostic=diagnostic,
        examination_date=examination_date,
        patient_id=patient_id,
        doctor_id=doctor_id,
        packages_id=packages_id,
        amount=amount,
        medicine_id_list=medicine_id_list)


def update_account_password(account_id, new_password):
    return dao.update_account_password(account_id=account_id, new_password=new_password)


def update_profile_user(user, **kwargs):
    return dao.update_profile_user(user=user, **kwargs)


def update_examination_schedule(examination_schedule_id, **kwargs):
    return dao.update_examination_schedule(examination_schedule_id=examination_schedule_id, **kwargs)


def get_role_list():
    return dao.get_role_list()


def get_medicine_type_list():
    return dao.get_medicine_type_list()


def get_medicine_unit_list():
    return dao.get_medicine_unit_list()


def get_packages_list():
    return dao.get_packages_list()


def get_examination_schedules_list():
    return dao.get_examination_schedules_list()


def get_medical_bills_list():
    return dao.get_medical_bills_list()


def get_medicine_list():
    return dao.get_medicine_list()


def get_patients_list():
    return dao.get_patients_list()


def get_examination_schedules_list_by_date(date):
    return dao.get_examination_schedules_list_by_date(date=date)


def get_account_by_id(account_id):
    return dao.get_account_by_id(account_id=account_id)


def get_account_by_username(username):
    return dao.get_account_by_username(username=username)


def get_account_by_email(email):
    return dao.get_account_by_email(email=email)


def get_account_by_phone_number(phone_number):
    return dao.get_account_by_phone_number(phone_number=phone_number)


def get_user_by_id(user_id):
    return dao.get_user_by_id(user_id=user_id)


def get_user_by_email(email):
    return dao.get_user_by_email(email=email)
