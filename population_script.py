import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'boom_saloon.settings')
import django
import datetime
django.setup()
from home.models import Magazine, MagazineIssue,Hashtag


def add_magazine(mag_title, id, description_short, description_long, price, discount, cover, link_to_publishers_site):
    m = Magazine.objects.get_or_create(title = mag_title, description_long = description_long, description_short= description_short, price = price,
                                       discount = discount, cover=cover, link_to_publishers_site = link_to_publishers_site, id=id)[0]
    m.save()
    return m

def add_issue(magazine, cover, date, title):
    i = MagazineIssue.objects.get_or_create(date=date, cover=cover, magazine=magazine, title=title)[0]
    i.save()
    return i





def populate():
    mag1_issues = [{'cover': 'cover11.jpg', 'date': datetime.date.today(), 'title': "Issue title 1"},
                   {'cover': 'cover12.jpg', 'date': datetime.date(2002, 5, 1), 'title': "Issue title 2" }]

    mag2_issues = [{'cover': 'cover21.jpg', 'date': datetime.date.today(), 'title': "Issue title 3"},
                   {'cover': 'cover22.jpg', 'date': datetime.date(2003, 5, 1), 'title': "Issue title 4"}]

    mags = {'MagazineTitle1' : {'issues': mag1_issues, 'id' : 1, 'description_short': 'Lorem ipsum dolor sit amet, consectetur adipiscing' \
                                                                                     ' elit, sed do eiusmod tempor incididunt ut labore et ' \
                                                                                     'dolore magna aliqua. Ut enim ad minim veniam, quis' \
                                                                                     ' nostrud exercitation ullamco laboris nisi ut aliquip ' \
                                                                                     'ex ea commodo consequat. Duis aute irure dolor in reprehenderit ' 
                                                                                     'in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur ' \
                                                                                     'sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit ' \
                                                                                     'anim id est laborum.',
                               'description_long' : 'Lorem ipsum dolor sit amet, consectetur adipiscing' \
                                                                                     ' elit, sed do eiusmod tempor incididunt ut labore et ' \
                                                                                     'dolore magna aliqua. Ut enim ad minim veniam, quis' \
                                                                                     ' nostrud exercitation ullamco laboris nisi ut aliquip ' \
                                                                                     'ex ea commodo consequat. Duis aute irure dolor in reprehenderit ' 
                                                                                     'in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur ' \
                                                                                     'sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit ' \
                                                                                     'anim id est laborum.Lorem ipsum dolor sit amet, consectetur adipiscing' \
                                                                                     ' elit, sed do eiusmod tempor incididunt ut labore et ' \
                                                                                     'dolore magna aliqua. Ut enim ad minim veniam, quis' \
                                                                                     ' nostrud exercitation ullamco laboris nisi ut aliquip ' \
                                                                                     'ex ea commodo consequat. Duis aute irure dolor in reprehenderit ' 
                                                                                     'in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur ' \
                                                                                     'sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit ' \
                                                                                     'anim id est laborum.',
                               'price': 13,
                               'discount': 0.1,
                               'cover' : mag1_issues[0]['cover'],
                               'link_to_publishers_site' : 'www.mag1.com',},

            'MagazineTitle2': {'issues': mag2_issues, 'id': 2,
                               'description_short': 'Lorem ipsum dolor sit amet, consectetur adipiscing' \
                                                    ' elit, sed do eiusmod tempor incididunt ut labore et ' \
                                                    'dolore magna aliqua. Ut enim ad minim veniam, quis' \
                                                    ' nostrud exercitation ullamco laboris nisi ut aliquip ' \
                                                    'ex ea commodo consequat. Duis aute irure dolor in reprehenderit '
                                          
                                                    'in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur ' \
                                                    'sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit ' \
                                                    'anim id est laborum.',
                               'description_long': 'Lorem ipsum dolor sit amet, consectetur adipiscing' \
                                                   ' elit, sed do eiusmod tempor incididunt ut labore et ' \
                                                   'dolore magna aliqua. Ut enim ad minim veniam, quis' \
                                                   ' nostrud exercitation ullamco laboris nisi ut aliquip ' \
                                                   'ex ea commodo consequat. Duis aute irure dolor in reprehenderit '
                                                   'in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur ' \
                                                   'sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit ' \
                                                   'anim id est laborum.Lorem ipsum dolor sit amet, consectetur adipiscing' \
                                                   ' elit, sed do eiusmod tempor incididunt ut labore et ' \
                                                   'dolore magna aliqua. Ut enim ad minim veniam, quis' \
                                                   ' nostrud exercitation ullamco laboris nisi ut aliquip ' \
                                                   'ex ea commodo consequat. Duis aute irure dolor in reprehenderit '
                                                   'in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur ' \
                                                   'sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit ' \
                                                   'anim id est laborum.',
                               'price': 11,
                               'discount': 0.07,
                               'cover': mag2_issues[0]['cover'],
                               'link_to_publishers_site': 'www.mag2.com', }
            }





    for mag, mag_data in mags.items():
        m = add_magazine(mag_title=mag, id=mag_data['id'], description_short=mag_data['description_short'], description_long=mag_data['description_long'],
                         price=mag_data['price'], discount=mag_data['discount'], cover=mag_data['cover'], link_to_publishers_site=mag_data['link_to_publishers_site'])
        for i in mag_data['issues']:
            add_issue(magazine=m, cover=i['cover'], date=i['date'], title=i['title'])

    h1 = Hashtag.objects.get_or_create(text="#PhotoEssays")[0]
    h1.save()
    h1.magazines.add(1,2)
    h2 = Hashtag.objects.get_or_create(text="#Music")[0]
    h2.save()
    h2.magazines.add(1)
    h3 = Hashtag.objects.get_or_create(text="#Theatre")[0]
    h3.save()
    h3.magazines.add(2)



if __name__ == '__main__':
    print('Starting Clo population script...')
    populate()




