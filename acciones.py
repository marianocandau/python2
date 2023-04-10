from sys import argv
import pandas as pd
import yfinance as yf
import sqlite3

con = sqlite3.connect("market_data.sqlite")