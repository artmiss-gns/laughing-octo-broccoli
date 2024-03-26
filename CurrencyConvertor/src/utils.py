import os 

def get_env_value(key, filename=".env"):
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            k, v = line.strip().split("=")
            if k == key :
                return v 
            

def get_currencies() :
    return [
        'AUD',
        'BGN',
        'BRL',
        'CAD',
        'CHF',
        'CNY',
        'CZK',
        'DKK',
        'EUR',
        'GBP',
        'HKD',
        'HRK',
        'HUF',
        'IDR',
        'ILS',
        'INR',
        'ISK',
        'JPY',
        'KRW',
        'MXN',
        'MYR',
        'NOK',
        'NZD',
        'PHP',
        'PLN',
        'RON',
        'RUB',
        'SEK',
        'SGD',
        'THB',
        'TRY',
        'USD',
        'ZAR'
    ]
