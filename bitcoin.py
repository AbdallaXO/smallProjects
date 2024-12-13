import requests
import json
import sys
def main():
     users_request = return_argv()
     bitcoin_price = get_api()
     bitcoin_requested = return_btc(users_request, bitcoin_price)
     print(bitcoin_requested)
    
     
    

def get_api():
    """ gets current bitcoin price by using the coindesk api then converting it into 
    json and indexing into bitcoins price in USD and returning that"""
    try:
        response = requests.get(" https://api.coindesk.com/v1/bpi/currentprice.json")
        o = response.json()
        bitcoin_index = o['bpi']
        btc = bitcoin_index.get("USD").get('rate_float')
        return btc
    except requests.RequestException:
        sys.exit(1)

    

def return_argv():
    """ checks that user has put a valid input in CLI and validating it a number then returning it
    or exiting the program if not"""
    try:
        if len(sys.argv) >=1 and not sys.argv[1].isalpha():
            sys.argv[1] = float(sys.argv[1])
            return sys.argv[1]
        else:
            print("Command-line argument is not a number")
    except IndexError:
        print("Missing command-line argument")

def return_btc(btc_requested, btc_price):
    """ gets current btc price from the api + how many coins user wants to get
    and returning how many btcs that will be in USD value"""
    try:
        if btc_requested > 0:
            btc = float(btc_price) * float(btc_requested)
            return f"${btc:,.4f}"
    except TypeError:
        sys.exit(1)
if __name__ == "__main__":
    main()
