import psycopg2

import string
import random

import os
import django

import sys
from pathlib import Path
sys.path.append(Path(__file__).resolve().parent.parent.__str__())

from configs.remote_db_settings import *
from db_exports.export_context_and_general_data import context_db_connection

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'esbs.settings')
django.setup()

from context.models.role_classes import RoleClasses
from context.models.role_types import RoleTypes
from context.models.rms_user_types import RmsUserTypes
from general.models.organisations import Organisations
from users.models.users import Users
from users.models.profiles import UserProfiles


rms_db_connection = psycopg2.connect(
    user=REMOTE_DB_USER,
    password=REMOTE_DB_PASSWORD,
    host=REMOTE_DB_HOST,
    port=REMOTE_DB_PORT,
    database=REMOTE_RMS_DB_NAME
)


def get_data_from_table(schema: str, table_name: str):
    try:
        if rms_db_connection.closed:
            context_db_connection.reset()
        if not rms_db_connection.closed:
            cursor = rms_db_connection.cursor()
            cursor.execute(f"select * from {schema}.{table_name}")
            return cursor.fetchall()

    except Exception as error:
        print(f"failed: {error}")


def import_users():
    records = get_data_from_table('rms', 'people')
    for record in records:
        if Users.objects.filter(email=record[7]).exists():
            break

        organisation = Organisations.objects.get(default_name=record[6])

        password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        user = Users(
            username=record[7],
            first_name=record[2],
            last_name=record[3],
            email=record[7],
            is_active=True,
            is_superuser=True,
            is_staff=True,
        )

        user.set_password(password)
        user.save()

        profile = UserProfiles(
            user=user,
            prof_title=record[1],
            designation=record[4],
            organisation=organisation,
        )
        profile.save()

    print("done")


#import_users()
