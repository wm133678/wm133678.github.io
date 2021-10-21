import csv
import pandas as pd
import requests
from requests.exceptions import HTTPError
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#driver = webdriver.Chrome('<path_to>/chromedriver')
# Need to find path for Chromedriver

WhaleWallet = "0xae4d837caa0c53579f8a156633355df5058b02f3"
"""
Functions to create:

Find purchase date of token and what token it is.
Then find token price at the time compared to current value.

https://etherscan.io/tokencheck-tool
token quantity website

"""

def tokenScrape():
    # This function returns a list of Send / Recieve / Contract calls from Transaction list
    with open('AddressScrape.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            # Date of Transaction
            print(f'{row[2]}')




def DateScrape():
    # This function returns the dates for each transaction from the wallet
    with open('AddressScrape.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            # Date of Transaction
            print(f'{row[0]}')

def BuyAddress():
    with open('AddressScrape.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            # Buy address
            if row[8] != "":
                print(f'{row[8]}')

def DateAndAddress():
    with open('AddressScrape.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            # Buy address
            if row[8] != "" and row[2] == "Receive":
                print(f'{row[0]} {row[8]}  {row[7]} ')

def ContractAddressOfTokenBought():
    with open('AddressScrape.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        outF = open("AddressAndDateBought.txt", "w")

        for row in csv_reader:
            if row[8] != "":
                address = row[8]
                print("Address = " + address)
                date = (f'{row[0]}')
                print("Date = " + date)
                etherscanLink = "https://etherscan.io/address/" + address
                outF.write(address + " | " + date)
                outF.write("\n")

        outF.close()
                #print(etherscanLink)



def preventRepeats():
    address = 0
    array = []
    if address in array:
        pass
    elif address not in array:
        array.append(address)
    else:
        pass

def pandaViewing():
    data = pd.read_csv(r'AddressScrape.csv')
    df = pd.DataFrame(data)
    print(df)

def GetUSDValueAtDate(tokenName, date):

    #tokenName = "unfederalreserve"
    #date = "05-05-2021"

    r = requests.get("http://api.coingecko.com/api/v3/coins/" + tokenName + "/history?date=" + date + "&localization=false")
    #print(r.status_code)
    print(r.text)
    jsonResponse = r.json()
    getUSDPrice = {'key1': 'value1', 'key2': 'value2'}
    value = jsonResponse["market_data"]["current_price"]["usd"]
    print("Token " + tokenName + " was worth " + str(value) + " on " + date)




def checkIfValidAPI():
    r = requests.get("http://api.coingecko.com/api/v3/coins/unfederalreserve/history?date=05-05-2021&localization=false")
    if r.status_code == requests.codes.ok:
        pass
    else:
        print("here")

def PriceAtDateToken():
    with open('AddressScrape.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if row[8] != "":
                address = row[8]
                print("Address = " + address)
                date = (f'{row[0]}')
                print("Date = " + date)

                # turn token address into token name
                TokenInfo = requests.get("http://api.coingecko.com/api/v3/coins/ethereum/contract/" + address)
                Tjson = TokenInfo.json()
                tokenName = Tjson["id"]


                etherscanLink = "https://etherscan.io/address/" + address
                #print(etherscanLink)
                r = requests.get("http://api.coingecko.com/api/v3/coins/" + tokenName + "/history?date=" + date + "&localization=false")
                # print(r.status_code)
                # print(r.text)
                jsonResponse = r.json()
                getUSDPrice = {'key1': 'value1', 'key2': 'value2'}
                value = jsonResponse["market_data"]["current_price"]["usd"]
                print("Token " + tokenName + " was worth " + str(value) + " on " + date)

def PriceAtDateForOneToken():

    address = "0xfe3e6a25e6b192a42a44ecddcd13796471735acf"
    print("Address = " + address)
    date = "01-11-2021"
    print("Date = " + date)

    # turn token address into token name
    TokenInfo = requests.get("http://api.coingecko.com/api/v3/coins/ethereum/contract/" + address)
    Tjson = TokenInfo.json()
    tokenName = Tjson['id']
    print(tokenName)

    r = requests.get("http://api.coingecko.com/api/v3/coins/" + tokenName + "/history?date=" + date + "&localization=false")
    # print(r.status_code)
    print(r.text)
    jsonResponse = r.json()
    print(jsonResponse)
    #value = jsonResponse["market_data"]["current_price"]["usd"]
    #print("Token " + tokenName + " was worth " + str(value) + " on " + date)

def RecentCops():
    # This function will return recent purchases from a wallet
    # if date is "recent", past week
    from datetime import date
    today = date.today()
    d3 = today.strftime("%m/%d/%Y")

    dateRange = d3[0]
    print(dateRange)

    print("Today's date:", d3)
    with open('AddressScrape.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            # Date of Transaction
            print(f'{row[0]}')


#BuyAddress()
#DateAndAddress()
#GetValueAtTime()

"""
Historical price call to CoinGecko

api.coingecko.com/api/v3/coins/unfederalreserve/history?date=05-05-2021&localization=false
api.coingecko.com/api/v3/coins/ethereum/contract


"""
RecentCops()
#DateScrape()
#ContractAddressOfTokenBought()
#GetUSDValueAtDate(tokenName="Ethereum", date="01-01-2021")
#PriceAtDateForOneToken()
