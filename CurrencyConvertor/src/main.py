import json
from src.get_data import get_data
from cachetools import cached, TTLCache

cache = TTLCache(maxsize=100, ttl=60)

@cached(cache)
def convert_currency(currency_inp, currency_inp_value, currency_out, data):
    if currency_inp == currency_out:
        return currency_inp_value  # No conversion needed if both currencies are the same

    # Get the exchange rates for input and output currencies
    try :
        rate_inp = json.loads(data.text)["data"][currency_inp]
        rate_out = json.loads(data.text)["data"][currency_out]
    except json.JSONDecodeError or KeyError:
        raise Exception("the currency you entered was not found!")

    # Perform the conversion
    converted_value = currency_inp_value * (rate_out / rate_inp)
    return converted_value


if __name__ == "__main__" :
    data = get_data()
    
    converted_value = convert_currency(
        currency_inp=input("Enter the input currency: "),
        currency_out=input("Enter the output currency: "),
        currency_inp_value=float(input("Enter the amount of money you have: ")),
        data=data,
    )
    print(converted_value)