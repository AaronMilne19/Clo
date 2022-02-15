import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'boom_saloon.settings')
import django
import datetime
django.setup()
from home.models import Magazine, MagazineIssue,Hashtag


def add_magazine(mag_title, id, description_short, description_long, cover, link_to_publishers_site):
    m = Magazine.objects.get_or_create(title = mag_title, description_long = description_long, description_short= description_short,
                                         cover=cover, link_to_publishers_site = link_to_publishers_site, id=id)[0]
    m.save()
    return m

def add_issue(magazine, cover, date, title, description, price, discounted_price):
    i = MagazineIssue.objects.get_or_create(date=date, cover=cover, magazine=magazine,
                                            title=title, issue_description=description,
                                            price=price, discounted_price=discounted_price)[0]
    i.save()
    return i





def populate():
    mag1_issues = [{'cover': 'cover11.jpg', 'date': datetime.date.today(), 'title': "Issue title 1",
                    'price': 20, 'discounted_price': 15,
                    'issue_description': '''Lorem ipsum dolor sit amet, consectetur adipiscing' \
                     ' elit, sed do eiusmod tempor incididunt ut labore et ' \
                     'dolore magna aliqua. Ut enim ad minim veniam, quis' \
                     ' nostrud exercitation ullamco laboris nisi ut aliquip ' \
                     'ex ea commodo consequat. Duis aute irure dolor in reprehenderit '''},
                   {'cover': 'cover11.jpg', 'date': datetime.date.today(), 'title': "Issue title 2",
                    'price': 20, 'discounted_price': 15,
                    'issue_description': '''Lorem ipsum dolor sit amet, consectetur adipiscing' \
                         ' elit, sed do eiusmod tempor incididunt ut labore et ' \
                         'dolore magna aliqua. Ut enim ad minim veniam, quis' \
                         ' nostrud exercitation ullamco laboris nisi ut aliquip ' \
                         'ex ea commodo consequat. Duis aute irure dolor in reprehenderit '''},
                   {'cover': 'cover11.jpg', 'date': datetime.date.today(), 'title': "Issue title 3",
                    'price': 30, 'discounted_price': 15,
                    'issue_description': '''Lorem ipsum dolor sit amet, consectetur adipiscing' \
                         ' elit, sed do eiusmod tempor incididunt ut labore et ' \
                         'dolore magna aliqua. Ut enim ad minim veniam, quis' \
                         ' nostrud exercitation ullamco laboris nisi ut aliquip ' \
                         'ex ea commodo consequat. Duis aute irure dolor in reprehenderit '''},

                   {'cover': 'cover12.jpg', 'date': datetime.date(2002, 5, 1), 'title': "Issue title 4",
                    'price': 21, 'discounted_price': 16,
                    'issue_description': '''Lorem ipsum dolor sit amet, consectetur adipiscing' \
                     ' elit, sed do eiusmod tempor incididunt ut labore et ' \
                     'dolore magna aliqua. Ut enim ad minim veniam, quis' \
                     ' nostrud exercitation ullamco laboris nisi ut aliquip ' \
                     'ex ea commodo consequat. Duis aute irure dolor in reprehenderit '''
                    }]

    mag2_issues = [{'cover': 'cover21.jpg', 'date': datetime.date.today(), 'title': "Issue title 5",
                    'price': 10, 'discounted_price': 8,
                    'issue_description': '''Lorem ipsum dolor sit amet, consectetur adipiscing' \
                     ' elit, sed do eiusmod tempor incididunt ut labore et ' \
                     'dolore magna aliqua. Ut enim ad minim veniam, quis' \
                     ' nostrud exercitation ullamco laboris nisi ut aliquip ' \
                     'ex ea commodo consequat. Duis aute irure dolor in reprehenderit '''
                    },
                   {'cover': 'cover22.jpg', 'date': datetime.date(2003, 5, 1), 'title': "Issue title 6",
                    'price': 9, 'discounted_price': 7,
                    'issue_description': '''Lorem ipsum dolor sit amet, consectetur adipiscing' \
                     ' elit, sed do eiusmod tempor incididunt ut labore et ' \
                     'dolore magna aliqua. Ut enim ad minim veniam, quis' \
                     ' nostrud exercitation ullamco laboris nisi ut aliquip ' \
                     'ex ea commodo consequat. Duis aute irure dolor in reprehenderit '''
                    }]
    mag3_issues = [{'cover': 'cover21.jpg', 'date': datetime.date.today(), 'title': "Issue title 7",
                    'price': 10, 'discounted_price': 8,
                    'issue_description': '''Lorem ipsum dolor sit amet, consectetur adipiscing' \
                         ' elit, sed do eiusmod tempor incididunt ut labore et ' \
                         'dolore magna aliqua. Ut enim ad minim veniam, quis' \
                         ' nostrud exercitation ullamco laboris nisi ut aliquip ' \
                         'ex ea commodo consequat. Duis aute irure dolor in reprehenderit '''
                    },
                   {'cover': 'cover22.jpg', 'date': datetime.date(2003, 5, 1), 'title': "Issue title 8",
                    'price': 9, 'discounted_price': 7,
                    'issue_description': '''Lorem ipsum dolor sit amet, consectetur adipiscing' \
                         ' elit, sed do eiusmod tempor incididunt ut labore et ' \
                         'dolore magna aliqua. Ut enim ad minim veniam, quis' \
                         ' nostrud exercitation ullamco laboris nisi ut aliquip ' \
                         'ex ea commodo consequat. Duis aute irure dolor in reprehenderit '''
                    }]

    mag4_issues = [{'cover': 'cover21.jpg', 'date': datetime.date.today(), 'title': "Issue title 9",
                    'price': 10, 'discounted_price': 8,
                    'issue_description': '''Lorem ipsum dolor sit amet, consectetur adipiscing' \
                         ' elit, sed do eiusmod tempor incididunt ut labore et ' \
                         'dolore magna aliqua. Ut enim ad minim veniam, quis' \
                         ' nostrud exercitation ullamco laboris nisi ut aliquip ' \
                         'ex ea commodo consequat. Duis aute irure dolor in reprehenderit '''
                    },
                   {'cover': 'cover22.jpg', 'date': datetime.date(2003, 5, 1), 'title': "Issue title 10",
                    'price': 9, 'discounted_price': 7,
                    'issue_description': '''Lorem ipsum dolor sit amet, consectetur adipiscing' \
                         ' elit, sed do eiusmod tempor incididunt ut labore et ' \
                         'dolore magna aliqua. Ut enim ad minim veniam, quis' \
                         ' nostrud exercitation ullamco laboris nisi ut aliquip ' \
                         'ex ea commodo consequat. Duis aute irure dolor in reprehenderit '''
                    }]

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
                               'cover': mag2_issues[0]['cover'],
                               'link_to_publishers_site': 'www.mag2.com', },

            'MagazineTitle3': {'issues': mag3_issues, 'id': 3,
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
                               'cover': mag3_issues[0]['cover'],
                               'link_to_publishers_site': 'www.mag3.com', },

            'MagazineTitle4': {'issues': mag4_issues, 'id': 4,
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
                               'cover': mag4_issues[0]['cover'],
                               'link_to_publishers_site': 'www.mag4.com', }
            }





    for mag, mag_data in mags.items():
        m = add_magazine(mag_title=mag, id=mag_data['id'], description_short=mag_data['description_short'], description_long=mag_data['description_long'],
                         cover=mag_data['cover'], link_to_publishers_site=mag_data['link_to_publishers_site'])
        for i in mag_data['issues']:
            add_issue(magazine=m, cover=i['cover'], date=i['date'], title=i['title'], description=i['issue_description'],
                      price=i['price'], discounted_price=i['discounted_price'])

    h1 = Hashtag.objects.get_or_create(text="#PhotoEssays")[0]
    h1.save()
    h1.magazines.add(1,2,4)
    h2 = Hashtag.objects.get_or_create(text="#Music")[0]
    h2.save()
    h2.magazines.add(1,4,3)
    h3 = Hashtag.objects.get_or_create(text="#Theatre")[0]
    h3.save()
    h3.magazines.add(2,4)



if __name__ == '__main__':
    print('Starting Clo population script...')
    populate()
    print('Population script OK ')




