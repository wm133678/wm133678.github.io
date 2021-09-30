import csv


def DateScrape():
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

def GetValueAtTime():
    with open('AddressScrape.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if row[8] != "":
                address = row[8]
                print("Address = " + address)
                etherscanLink = "https://etherscan.io/address/" + address
                print(etherscanLink)

def preventRepeats():
    address = 0
    array = []
    if address in array:
        pass
    elif address not in array:
        array.append(address)
    else:
        pass

#BuyAddress()
#DateAndAddress()
GetValueAtTime()
