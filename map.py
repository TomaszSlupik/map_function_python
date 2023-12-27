# użycie funkcji map 
# Zamiana liczb na int 
# Zamiana adresów e-mail na małe litery 

users = [
    {'name': 'Alice', 'age': 25, 'email': 'alice@EXAMPLE.com'},
    {'name': 'Bob', 'age': '35', 'email': 'bob@example.com'},
    {'name': 'Charlie', 'age': 45.0, 'email': 'CHARLIE@example.com'},
]

def int_users(number):
    number['age'] = int(number['age'])
    return  number

def lowerCase (user):
    user['email'] = user['email'].lower()
    return user

result_users = list(map(int_users, users))
email_users = list(map(lowerCase, users))

for user in email_users:
    print(user)

print('---')

airports = [
    (
        'JFK',
        'John F. Kennedy International Airport',
        (40.6413, -73.7781),
        3,
    ),
    (
        'EWR',
        'Newark Liberty International Airport',
        (40.6895, -74.1745),
        6,
    ),
    (
        'LAX',
        'Los Angeles International Airport',
        (33.9416, -118.4085),
        38,
    ),
    (
        'SFO',
        'San Francisco International Airport',
        (37.6213, -122.3790),
        4,
    ),
    (
        'ORD',
        'Chicago O\'Hare International Airport',
        (41.9742, -87.9073),
        204,
    ),
]

#  wyodrębnić kody IATA
def myIata (iata):
    return iata[0]

iata = list(map(myIata, airports))

print(sorted(iata))

print('---')

places = [
    ('Paris', (48.8566, 2.3522), 100),
    ('London', (51.5072, -0.1276), 120),
    ('Rome', (41.9028, 12.4964), 90),
    ('Barcelona', (41.3851, 2.1734), 80),
    ('Krakow', (50.0647, 19.9450), 60),
    ('Amsterdam', (52.3667, 4.8945), 110),
]

EURUSD = 1.09

"""
Wyodrębnij ceny za nocleg z tej listy i obliczyć 
je w dolarze amerykańskim (USD) korzystając z funkcji map(). 
Do obliczeń przyjmij kurs EURUSD = 1.09
"""

def pricePlace (price):
    return price[2] * EURUSD


priceForAccommodation = list(map(pricePlace, places))
floatPriceForAccommodation = []

for price in priceForAccommodation:
    floatPriceForAccommodation.append(round(price, 2))

print(floatPriceForAccommodation)

print('---')

# Podana jest cena netto. Oblicz brutto 
net_prices = [
    (100, 'Europe'),
    (120, 'Asia'),
    (80, 'North America'),
    (90, 'South America'),
]
taxes = {
    'Europe': 0.23,
    'Asia': 0.2,
    'North America': 0.18,
    'South America': 0.15,
}

def calculate_gross_price(price, tax_rate):
    return price * (1 + tax_rate)

gross = list(map(lambda x: calculate_gross_price(x[0], taxes[x[1]]), net_prices))

float_gross = [round(item, 1) for item in gross ]
takes_country = [country for country in taxes.keys()]

print(list(zip(float_gross, takes_country)))

print('---')

# 
inch = 2.54
inch_lengths = [2.5, 3.5, 1.8, 2.5, 3.5]

def calc (length):
    return inch * length

cm_lengths = list(map(lambda x: calc(x), inch_lengths))

print(cm_lengths)