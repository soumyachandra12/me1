import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','temp.settings')

import django
django.setup()

import random
from firstapp.models import User
from faker import Faker

fakegen=Faker()
topics=['first_name','last_name','email']

def add_topic():
    t=User.objects.get_or_create(first_name=random.choice(topics))[0]
    t.save()
    return t
def populate(N=5):
    for entry in range(N):
        top=add_topic()
        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.company()

if __name__=='__main__':
    print("Populating Script")
    populate(20)
    print("Populating Complete")
