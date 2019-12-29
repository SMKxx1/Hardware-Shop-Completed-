import pandas
import numpy
import pymysql
import os
from tabulate import tabulate
import time
import platform
import datetime

conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = '1234',
    database = 'hardware'
)

c = conn.cursor()

def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')



def main():
    clear()
    print("Welcome")
    time.sleep(0.5)
    clear()
    print("Welcome!")
    time.sleep(0.5)
    clear()
    print("Welcome!!")
    time.sleep(0.5)
    clear()
    print("Welcome!!!")
    time.sleep(0.5)
    print("You can build your own pc here.")
    time.sleep(2)
    print("Lets start with the processor")
    input()
    clear()
    display = pandas.read_sql("select * from processor;", conn)
    cart = pandas.DataFrame(columns=['Brand','Name','Price'])
    print(tabulate(
        display,
        headers=['No','Brand','Name','Chipset','Speed','# of cores','# of threads','Price'],
        tablefmt="fancy_grid",
        showindex=False))
    opt = int(input("Enter the processor no: "))
    dic = {
        'Brand': str(display.loc[opt - 1]['brand']),
        'Name': str(display.loc[opt - 1]['name']),
        'Price': int(display.loc[opt - 1]['price'])
    }
    cart = cart.append(dic, ignore_index=True, sort=False)
    print(tabulate(cart,
                   headers='keys',
                   tablefmt='fancy_grid',
                   showindex=False))
    input()
    clear()
    chipset = str(display.loc[opt - 1]['chipset'])
    display = pandas.read_sql(f"select * from motherboards where chipset = '{chipset}';", conn)
    print(tabulate(display,
                   headers=['No','Brand','Name','Chipset','# of ram sloths','Size','Price'],
                   tablefmt="fancy_grid",
                   showindex=False))
    display = pandas.read_sql(f"select * from motherboards;", conn)
    opt = int(input("Enter the motherboard no: "))
    dic = {
        'Brand': str(display.loc[opt - 1]['brand']),
        'Name': str(display.loc[opt - 1]['name']),
        'Price': int(display.loc[opt - 1]['price'])
    }
    cart = cart.append(dic, ignore_index=True, sort=False)
    print(tabulate(cart,
                   headers='keys',
                   tablefmt='fancy_grid',
                   showindex=False))
    input()
    clear()
    no_of_ram = int(display.loc[opt - 1]['ram_sloths'])
    display = pandas.read_sql(f"select * from ram;", conn)
    print(tabulate(display,
                   headers=['No','Brand','Name','Memory','# of rams','Speed','Price'],
                   tablefmt="fancy_grid",
                   showindex=False))
    opt = int(input("Enter the Ram no: "))
    dic = {
        'Brand': str(display.loc[opt - 1]['brand']),
        'Name': str(display.loc[opt - 1]['name']),
        'Price': int(display.loc[opt - 1]['price'])
    }
    cart = cart.append(dic, ignore_index=True, sort=False)
    print(tabulate(cart,
                   headers='keys',
                   tablefmt='fancy_grid',
                   showindex=False))
    input()
    clear()
    display = pandas.read_sql(f"select * from graphics_card;", conn)
    print(tabulate(display,
                   headers=['No','Brand','Name','VRAM','Price'],
                   tablefmt="fancy_grid",
                   showindex=False))
    opt = int(input("Enter the GPU no: "))
    dic = {
        'Brand': str(display.loc[opt - 1]['brand']),
        'Name': str(display.loc[opt - 1]['name']),
        'Price': int(display.loc[opt - 1]['price'])
    }
    cart = cart.append(dic, ignore_index=True, sort=False)
    print(tabulate(cart,
                   headers='keys',
                   tablefmt='fancy_grid',
                   showindex=False))
    input()
    clear()
    display = pandas.read_sql(f"select * from storage;", conn)
    print(tabulate(display,
                   headers=['No','Brand','Name','Type','Capacity','Price'],
                   tablefmt="fancy_grid",
                   showindex=False))
    opt = int(input("Enter the item no: "))
    dic = {
        'Brand': str(display.loc[opt - 1]['brand']),
        'Name': str(display.loc[opt - 1]['name']),
        'Price': int(display.loc[opt - 1]['price'])
    }
    cart = cart.append(dic, ignore_index=True, sort=False)
    print(tabulate(cart,
                   headers='keys',
                   tablefmt='fancy_grid',
                   showindex=False))
    input()
    clear()
    display = pandas.read_sql(f"select * from powersupply;", conn)
    print(tabulate(display,
                   headers=['No','Brand','Name','Watts','Modularity''Price'],
                   tablefmt="fancy_grid",
                   showindex=False))
    opt = int(input("Enter the PSU no: "))
    dic = {
        'Brand': str(display.loc[opt - 1]['brand']),
        'Name': str(display.loc[opt - 1]['name']),
        'Price': int(display.loc[opt - 1]['price'])
    }
    cart = cart.append(dic, ignore_index=True, sort=False)
    print(tabulate(cart,
                   headers='keys',
                   tablefmt='fancy_grid',
                   showindex=False))
    input()
    clear()
    display = pandas.read_sql(f"select * from cabinet;", conn)
    print(tabulate(display,
                   headers=['No','Brand','Name','Size','Price'],
                   tablefmt="fancy_grid",
                   showindex=False))
    opt = int(input("Enter the Cabinet no: "))
    dic = {
        'Brand': str(display.loc[opt - 1]['brand']),
        'Name': str(display.loc[opt - 1]['name']),
        'Price': int(display.loc[opt - 1]['price'])
    }
    cart = cart.append(dic, ignore_index=True, sort=False)
    print(tabulate(cart,
                   headers='keys',
                   tablefmt='fancy_grid',
                   showindex=False))
    print()
    grand_total = cart['Price'].sum()
    print(f"Your Grand Total will be: {grand_total}")
    confirmation = input("Do you want to confirm your purchase?[y/n] ")
    if confirmation == 'y':
        gst = lambda y: ((y/100) * 18)
        Tax = gst(cart['Price'])
        dic = {
            'Item Name': cart['Name'],
            'Price': cart['Price'],
            'Tax': Tax,
            'Final Price': cart['Price'] + Tax
        }
        receipt = pandas.DataFrame(dic)
        footer = {'Item Name': 'Total Price', 'Price': grand_total, 'Tax': sum(receipt['Tax']), 'Final Price': sum(receipt['Final Price'])}
        receipt = receipt.append(footer, ignore_index=True, sort=False)
        purchase(sum(receipt['Tax']), grand_total, sum(receipt['Final Price']))
        print("RECEIPT")
        print(tabulate(receipt,
                       headers='keys',
                       showindex=False,
                       tablefmt='grid',
                       numalign='right'))
        print("Purchase Completed!!!")

def purchase(tax, price, final_price):
    cdate = datetime.date.today()
    name = input("Please enter your full name: ")
    c.execute(f"INSERT INTO purchases VALUES(NULL, '{name}', {tax}, {price}, {final_price}, '{cdate}');")
    conn.commit()
    input()
    clear()

main()