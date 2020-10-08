
# Currency 
#### Currency is a free and open-source currency data API that tracks reference exchange rates.

### Documentation:

1. [Django](https://docs.djangoproject.com/en/2.0/releases/2.0/)
2. [Django Rest Framework](https://www.django-rest-framework.org/)

### Relational database Is Sqlite3

### Installation Steps:
1. Install git on Linux:  
`sudo apt-get install -y git`
2. Clone or download this repo.
3. Install pip and vitualenv on Linux:  
`sudo apt-get install -y virtualenv`  
`sudo apt-get install -y python3-pip`

4. Create a virtual environment on Linux or Mac:  
`virtualenv -p python3 ~/.virtualenvs/currency`
5. Activate the virtual environment on Linux or Mac:  
`source ~/.virtualenvs/currency/bin/activate`

6. Install requirements in the virtualenv:  
`pip3 install -r requirements.txt`
8. Make Django database migrations:
`python manage.py makemigrations`
then: `python manage.py migrate`


### Create Superuser for Admin:
1. `python manage.py createsuperuser`
2. ADMIN USER
```
username: admin
password: 123
```

### Run Tests & Coverage:
1. `python manage.py test` or `coverage run --source='.' manage.py test`
2. `coverage report -m`

### Run Locally:
1. Run the project locally:  
`python manage.py runserver`
2. Navigate to: `http://localhost:8000/admin/`

### API Endpoints:
#### Main Url `http://localhost:8000`
#### Get Rate
1. Endpoint: `/rate`
2. Method: `GET`
3. Parameters: `?date=2020-10-07&from_currency=usd&to_currency=eur`
- Full Endpoint: `http://localhost:8000/rate/?date=2020-10-05&from_currency=usd&to_currency=eur`

### Templates Endpoints
- Full Endpoint: `http://localhost:8000/rates/?date=2020-10-5&from_currency=USD&to_currency=EUR`


#### Available Currencies

```
{
    "AUD": "Australian Dollar",
    "BGN": "Bulgarian Lev",
    "BRL": "Brazilian Real",
    "CAD": "Canadian Dollar",
    "CHF": "Swiss Franc",
    "CNY": "Chinese Renminbi Yuan",
    "CZK": "Czech Koruna",
    "DKK": "Danish Krone",
    "EUR": "Euro",
    "GBP": "British Pound",
    "HKD": "Hong Kong Dollar",
    "HRK": "Croatian Kuna",
    "HUF": "Hungarian Forint",
    "IDR": "Indonesian Rupiah",
    "ILS": "Israeli New Sheqel",
    "INR": "Indian Rupee",
    "ISK": "Icelandic Króna",
    "JPY": "Japanese Yen",
    "KRW": "South Korean Won",
    "MXN": "Mexican Peso",
    "MYR": "Malaysian Ringgit",
    "NOK": "Norwegian Krone",
    "NZD": "New Zealand Dollar",
    "PHP": "Philippine Peso",
    "PLN": "Polish Złoty",
    "RON": "Romanian Leu",
    "RUB": "Russian Ruble",
    "SEK": "Swedish Krona",
    "SGD": "Singapore Dollar",
    "THB": "Thai Baht",
    "TRY": "Turkish Lira",
    "USD": "United States Dollar",
    "ZAR": "South African Rand"
}
```