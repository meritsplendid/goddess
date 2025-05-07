import os
os.environ['SQLALCHEMY_SILENCE_UBER_WARNING'] = '1'

import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine, Column, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

# Create database engine
engine = create_engine('postgresql://postgres:goddesscode@localhost:5433/My_database')

# Create base class for declarative models
Base = declarative_base()

# Define Bank class
class Bank(Base):
    __tablename__ = 'banks'
    bank = Column(String, primary_key=True)
    market_cap_usd = Column(Float)
    market_cap_eur = Column(Float)
    market_cap_gbp = Column(Float)
    market_cap_inr = Column(Float)

# Create table
Base.metadata.create_all(engine)

# URL and currency rates
url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
rates = {'EUR': 0.93, 'GBP': 0.8, 'INR': 82.95}

# Function to scrape data
def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    tables = soup.find_all('table', class_='wikitable')
    data = []
    for table in tables:
        for row in table.find_all('tr')[1:]:
            cols = row.find_all('td')
            if len(cols) > 1:
                bank = cols[0].text.strip()
                market_cap = cols[1].text.strip().replace('$', '').replace(',', '')
                try:
                    market_cap = float(market_cap)
                    data.append((bank, market_cap))
                except ValueError:
                    pass  # Ignore rows with non-numeric market cap values
    return data

# Function to convert market capitalization
def convert_market_cap(data):
    converted_data = []
    for bank, market_cap in data:
        eur = round(market_cap * rates['EUR'], 2)
        gbp = round(market_cap * rates['GBP'], 2)
        inr = round(market_cap * rates['INR'], 2)
        converted_data.append((bank, market_cap, eur, gbp, inr))
    return converted_data

# Function to load data into database
def load_data(data):
    Session = sessionmaker(bind=engine)
    session = Session()
    for bank, market_cap_usd, eur, gbp, inr in data:
        bank_obj = Bank(bank=bank, market_cap_usd=market_cap_usd, market_cap_eur=eur, market_cap_gbp=gbp, market_cap_inr=inr)
        session.add(bank_obj)
    session.commit()

# Function to start scraping and loading data
def start_scraping():
    data = scrape_data(url)
    converted_data = convert_market_cap(data)
    load_data(converted_data)
    messagebox.showinfo('Success', 'Data scraped and loaded into database successfully.')

# Create GUI
root = tk.Tk()
root.title('Bank Scraper')
tk.Button(root, text='Start Scraping', command=start_scraping).pack(pady=20)
root.mainloop()