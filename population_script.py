import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'boom_saloon.settings')

import django
django.setup()

from django.contrib.auth.models import User
from home.models import Magazine, UserProfile

def populate():
    user_profiles = [
        {
            'email' : "janedoe33@gmail.com",
            'username' : "janedoe33",
            'picture' :  "stock.jpg",

        },

        {
            'email' : "foobar@gmail.com",
            'username' : "foobar",

        },
        ]

    magazines =[
        {
            'title': 'Counterpoint',
            'description_short' : 'Lorem ipsum dolor sit amet, consectetur adipiscing'
                                   'elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',

            'description_long' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit,'
                                 ' sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
                                 ' Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris'
                                 ' nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in '
                                 'reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla'
                                 ' pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa '
                                 'qui officia deserunt mollit anim id est laborum.',

            'price': 13,
            'discount' : 20,
            'photo1' : 'mag_pic1.jpg',
            'photo2' : 'mag_pic2.jpg',
            'link_to_publishers_site' : 'https://www.counterpointmag.co.uk/'



        }
    ]

    for user in user_profiles:
        add_userprofile(user["username"])

    for magzine in magazines:
        add_magazine(magzine["title"])


def add_userprofile( username):
    u = User.objects.get_or_create(username=username)[0]
    u.save()
    return u

def add_magazine( title ):
    m = Magazine.objects.get_or_create(title = title)[0]
    m.save()
    return m



if __name__ == '__main__':
    print("Starting Campus population script...")
    populate()