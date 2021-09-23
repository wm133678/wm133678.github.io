import csv

"""
with open('AddressScrape.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'{", ".join(row)}')
            line_count += 1
        else:
            print(f'{row[0]} {row[1]}  {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
"""
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


#BuyAddress()
#DateAndAddress()
GetValueAtTime()