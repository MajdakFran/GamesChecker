from pushbullet import PushBullet
import requests
import re
from bs4 import BeautifulSoup
import lxml
# Lists____________________________________
g2a_title = []
g2a_price = []
g2a_link = []
ig_price = []
ig_title = []
ig_link = []
# _________________________________________

query = input("Name of the game: ")
# kinguin_source = requests.get(
#    'https://www.kinguin.net/catalogsearch/result/index/?q=' + str(query).replace(' ', '+'))
g2a_source = requests.get(
    'https://www.g2a.com/en-us/search?query=' + str(query).replace(' ', '%20'))
ig_source = requests.get(
    'https://www.instant-gaming.com/en/search/?&query=' + str(query).replace(' ', '+'))
# humble_source = requests.get(
#    'https://www.humblebundle.com/store/search?sort=bestselling&search=' + str(query).replace(' ', '%20'))


g2a_soup = BeautifulSoup(g2a_source.text, 'lxml')
ig_soup = BeautifulSoup(ig_source.text, 'lxml')
#kinguin_soup = BeautifulSoup(kinguin_source.text, 'lxml')

# G2A_____________________________________________________________________
for price in g2a_soup.findAll('span', class_='Card__price-cost price'):
    g2a_price += re.findall(r'\d+\.\d+', str(price))

for title in g2a_soup.findAll('div', class_='Card__headings'):
    ttl = title.text
    g2a_title.append(ttl)

for link in g2a_soup.findAll('div', class_='Card__headings'):
    g2a_link.append(link.a.get('href'))
# _________________________________________________________________________

# IG________________________________________________________________________
for price in ig_soup.findAll('div', class_='price'):
    ig_price += re.findall(r'\d+\.\d+\€', str(price))

for title in ig_soup.findAll('div', class_='name'):
    ttl = title.string
    ig_title.append(ttl)

for link in ig_soup.findAll('div', class_='item mainshadow'):
    ig_link.append(link.a.get('href'))
# ___________________________________________________________________________

# Humble______________________________________________________________________
'''for price in humble_soup.findAll('span', class_='price'):
    print(price)
'''
# ____________________________________________________________________________

# Variables__________________________________
n = 0
ming2 = min(g2a_price)
minig = min(ig_price)
index_ming2 = g2a_price.index(ming2)
index_minig = ig_price.index(minig)
# ____________________________________________

for i in g2a_title:
    if str(g2a_title[0]).split()[0] not in str(i):
        pass
    else:
        try:
            print('G2A.COM')
            print(g2a_title[n])
            print(g2a_price[n] + '€')
            print('https://www.g2a.com/' + g2a_link[n] + '\n')
            n += 1
        except IndexError:
            pass
n = 0
if str(ig_title[0]) == 'None':
    print('INSTANT GAMING')
    print('No match!')
else:
    for i in ig_title:
        if str(ig_title[0]).split()[0] not in str(i):
            pass
        else:
            try:
                print('INSTANT GAMING')
                print(ig_title[n])
                print(ig_price[n])
                print(ig_link[n] + '\n')
                n += 1
            except IndexError:
                pass
print('\nLowest price G2A:\n' + g2a_title[index_ming2], '\n' +
      str(ming2) + '€' + '\nhttps://www.g2a.com/' + g2a_link[index_ming2] + '\n')
if str(ig_title[0]) == 'None':
    pass
else:
    print('Lowest Price IG:\n' + str(ig_title[index_minig]),
          '\n' + str(minig) + '\n' + str(ig_link[index_minig]))
print('\nCreated by Sud0nim')
input('press ENTER to exit: ')

# Todo:
# add humble-bundle and kinguin
# add sorting by price
# add better game recognition
