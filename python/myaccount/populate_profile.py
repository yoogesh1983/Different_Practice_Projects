import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myaccount.settings')
import django
django.setup()

from twmprofile.models import Profile

from faker import Faker
from random import *
fake = Faker()

def populate(n):
    for i in range(n):
        username=fake.email()
        firstName = fake.name()
        lastName = fake.name()
        age = randint(20,45)
        student_record = Profile.objects.get_or_create(username=username,
                                                       firstName=firstName,
                                                       lastName=lastName,
                                                       age=age)

populate(10)


#Note: To execute this script, run a command 'python populate_profile.py' directly from the console

