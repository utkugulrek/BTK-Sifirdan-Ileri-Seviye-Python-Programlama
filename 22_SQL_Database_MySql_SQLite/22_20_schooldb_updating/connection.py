"""
Database bağlantısı
"""

import mysql.connector

connection = mysql.connector.connect(
    host="localhost", user="root", password="1234", use_pure=True, database="school_db"
)
