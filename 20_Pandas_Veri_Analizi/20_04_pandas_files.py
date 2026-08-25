"""
Pandas kütüphanesinde dosya okuma çalışması
"""

import sqlite3
import pandas as pd

df = pd.read_csv("datasets/sample.csv")
df = pd.read_json("datasets/sample.json")
df = pd.read_excel("datasets/sample.xlsx")

# Database
connection = sqlite3.connect("datasets/sample.db")
df = pd.read_sql_query("SELECT *  FROM students", connection)

print(df)
