import sqlite3
import pandas as pd

conn = sqlite3.connect('ejemplo.db')
df = pd.read_sql("SELECT * FROM productos", conn)
print(df.head())


conn.close()